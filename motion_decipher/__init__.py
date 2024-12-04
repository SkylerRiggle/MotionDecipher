from os import mkdir, rmdir
from matplotlib import pyplot as plt
from motion_decipher.logger import log_info
from motion_decipher.pose_estimation import pose_estimation
from motion_decipher.keypad import Keypad, META_QUEST_3_KEYPAD
from motion_decipher.exporting import export_video, export_image
from motion_decipher.video_capture import capture_video_file, capture_video_realtime


class MotionDecipher:
    __input_video_path: str | None
    __input_video_save_path: str | None
    __camera_device_index: int
    __hand_image_save_path: str | None
    __save_segments: bool
    __plot_estimated_points: bool
    __keypad: Keypad
    __target_string: str
    __angle_ambiguous_regions: list[float]
    __distance_ambiguous_regions: list[tuple[float, float]]
    __view_angle: float

    # TODO: Remove Once Guanchong's Model Is Ready
    __TMP_SEGMENT_INDICES: list[tuple[int, int, bool]]

    def __init__(
        self,
        # TODO: Remove Once Guanchong's Model Is Ready
        TMP_SEGMENT_INDICES: list[tuple[int, int, bool]],

        input_video_path: str | None = None,
        input_video_save_path: str | None = None,
        camera_index: int = 0,
        hand_image_save_path: str | None = None,
        save_segments: bool = False,
        plot_estimated_points: bool = False,
        target_keypad: Keypad = META_QUEST_3_KEYPAD,
        target_string: str = '0000',
        angle_ambiguous_regions: list[float] | None = None,
        distance_ambiguous_regions: list[tuple[float, float]] = None,
        camera_view_angle: float = 90
    ):
        self.__input_video_path = input_video_path
        self.__input_video_save_path = input_video_save_path
        self.__camera_device_index = camera_index
        self.__hand_image_save_path = hand_image_save_path
        self.__save_segments = save_segments
        self.__plot_estimated_points = plot_estimated_points
        self.__keypad = target_keypad
        self.__target_string = target_string
        self.__angle_ambiguous_regions = (
            angle_ambiguous_regions if angle_ambiguous_regions is not None
            else [15.0]
        )
        self.__distance_ambiguous_regions = (
            distance_ambiguous_regions if distance_ambiguous_regions is not None
            else [0.5, 1/3]
        )
        self.__view_angle = camera_view_angle

        while self.__view_angle < 0.0:
            self.__view_angle += 360.0
        self.__view_angle %= 180.0

        # TODO: Remove Once Guanchong's Model Is Ready
        self.__TMP_SEGMENT_INDICES = TMP_SEGMENT_INDICES

    def run(self) -> list[str]:
        log_info("Gathering Input Frames.")
        frames = (
            capture_video_file(self.__input_video_path)
            if self.__input_video_path is not None
            else capture_video_realtime(self.__camera_device_index)
        )

        if (
            self.__input_video_save_path is not None
            and self.__input_video_path is not None
        ):
            log_info(f"Saving Input Frames to Path: {self.__input_video_save_path}")
            export_video(frames, self.__input_video_save_path)

        log_info("Estimating Hand Pose Information.")
        hand_poses = pose_estimation(frames, self.__hand_image_save_path)

        log_info("Detecting Keypress Event Segments.")
        # TODO: Remove Once Guanchong's Model Is Ready
        segments = self.__TMP_SEGMENT_INDICES

        if self.__save_segments:
            log_info("Saving Keypress Event Frames.")

            rmdir("./segments")
            mkdir("./segments")

            for seg_idx in range(len(segments)):
                rmdir(f"./segments/{seg_idx}")
                rmdir(f"./segments/{seg_idx}/normal")
                rmdir(f"./segments/{seg_idx}/triangles")

                mkdir(f"./segments/{seg_idx}")
                mkdir(f"./segments/{seg_idx}/normal")
                mkdir(f"./segments/{seg_idx}/triangles")

                segment = segments[seg_idx]
                for frame_idx in range(segment[0], segment[1] + 1):
                    frame = frames[frame_idx]
                    pose = hand_poses[frame_idx]

                    export_image(
                        frame,
                        f"./segments/{seg_idx}/normal/{frame_idx}.jpg"
                    )

                    export_image(
                        pose[
                            0 if segment[2] else 1
                        ].get_triangle().draw(frame),
                        f"./segments/{seg_idx}/triangles/{frame_idx}.jpg"
                    )

        x_min = float("inf")
        x_max = float("-inf")
        y_min = float("inf")
        y_max = float("-inf")
        z_min = float("inf")
        z_max = float("-inf")

        x_influence = abs(self.__view_angle - 90.0) / 90.0
        z_influence = 1.0 - x_influence

        x_values: list[float] = []
        y_values: list[float] = []
        z_values: list[float] = []

        for segment in segments:
            tri = hand_poses[segment[0]][0 if segment[2] else 1].get_triangle()
            cur_x = tri.get_x()
            cur_y = tri.get_y()
            cur_z = tri.get_area()

            x_values.append(cur_x)
            y_values.append(cur_y)
            z_values.append(cur_z)

            x_min = min(x_min, cur_x)
            x_max = max(x_max, cur_x)
            y_min = min(y_min, cur_y)
            y_max = max(y_max, cur_y)
            z_min = min(z_min, cur_z)
            z_max = max(z_max, cur_z)

        input_points: list[tuple[float, float]] = []

        for idx in range(len(x_values)):
            x_values[idx] = 1.0 - (x_values[idx] - x_min) / (x_max - x_min)
            y_values[idx] = 1.0 - (y_values[idx] - y_min) / (y_max - y_min)
            z_values[idx] = 1.0 - (z_values[idx] - z_min) / (z_max - z_min)

            input_points.append((
                x_values[idx] * x_influence +
                z_values[idx] * z_influence,
                y_values[idx]
            ))

        if self.__plot_estimated_points:
            plot_x = []
            plot_y = []

            for point in input_points:
                plot_x.append(point[0])
                plot_y.append(point[1])

            plt.title("Estimated Points")
            plt.xlabel("X Position")
            plt.ylabel("Y Position")
            plt.scatter(plot_x, plot_y)
            plt.plot(plot_x, plot_y)
            plt.show()

        min_list: list[str] | None = None

        for distance_ambiguous_region in self.__distance_ambiguous_regions:
            for angle_ambiguous_region in self.__angle_ambiguous_regions:
                cur_list = self.__keypad.infer_candidates(
                    input_points,
                    angle_ambiguous_region,
                    distance_ambiguous_region
                )

                if self.__target_string not in cur_list:
                    continue

                if min_list is None or len(cur_list) < len(min_list):
                    min_list = cur_list

        return min_list if min_list is not None else []