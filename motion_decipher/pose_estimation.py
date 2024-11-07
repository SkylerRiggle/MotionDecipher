import cv2 as cv
import mediapipe as mp
from motion_decipher.triangle import Triangle


class HandPose:
    __min_x: float
    __max_x: float
    __min_y: float
    __max_y: float

    __palm_triangle: Triangle

    def __init__(
        self,
        min_x: float,
        min_y: float,
        max_x: float,
        max_y: float,

        a_x: float,
        b_x: float,
        c_x: float,

        a_y: float,
        b_y: float,
        c_y: float,
    ):
        self.__min_x = min_x
        self.__max_x = max_x
        self.__min_y = min_y
        self.__max_y = max_y

        self.__palm_triangle = Triangle(
            a_x, a_y,
            b_x, b_y,
            c_x, c_y,
        )

    def get_triangle(self) -> Triangle:
        return self.__palm_triangle

def __drawn_estimation__(
    frames: list[cv.Mat],
    draw_save_path: str
) -> list[tuple[HandPose | None, HandPose | None]]:
    left_label: str = "Left"
    point_a: int = 0
    point_b: int = 5
    point_c: int = 17

    point_connections = [
        (0, 1),
        (0, 5),
        (0, 17),
        (1, 2),
        (2, 3),
        (3, 4),
        (5, 6),
        (5, 9),
        (6, 7),
        (7, 8),
        (9, 10),
        (9, 13),
        (10, 11),
        (11, 12),
        (13, 17),
        (13, 14),
        (14, 15),
        (15, 16),
        (17, 18),
        (18, 19),
        (19, 20),
    ]

    height, width, _ = frames[0].shape
    video_writer = cv.VideoWriter(
        draw_save_path,
        cv.VideoWriter_fourcc(*"MP4V"),
        30,
        (width, height)
    )
    hand_poses: list[tuple[HandPose | None, HandPose | None]] = [
        (None, None) for _ in frames
    ]

    with mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.3,
            min_tracking_confidence=0.3
    ) as hand_model:
        for frame_idx in range(len(frames)):
            frame = frames[frame_idx]
            results = hand_model.process(frame)

            draw_frame = frame.copy() if draw_save_path is not None else None

            if not results.multi_hand_landmarks:
                continue

            for hand_idx in range(len(results.multi_hand_landmarks)):
                landmarks = results.multi_hand_landmarks[hand_idx].landmark

                min_x: float = float("inf")
                max_x: float = float("-inf")
                min_y: float = float("inf")
                max_y: float = float("-inf")

                for landmark in landmarks:
                    min_x = min(min_x, landmark.x)
                    max_x = max(max_x, landmark.x)
                    min_y = min(min_y, landmark.y)
                    max_y = max(max_y, landmark.y)

                new_pose = HandPose(
                    min_x,
                    min_y,
                    max_x,
                    max_y,

                    landmarks[point_a].x,
                    landmarks[point_b].x,
                    landmarks[point_c].x,

                    landmarks[point_a].y,
                    landmarks[point_b].y,
                    landmarks[point_c].y,
                )

                if results.multi_handedness[hand_idx].classification[0].label == left_label:
                    hand_poses[frame_idx] = (new_pose, hand_poses[frame_idx][1])
                else:
                    hand_poses[frame_idx] = (hand_poses[frame_idx][0], new_pose)

                if draw_save_path is not None:
                    for connection in point_connections:
                        draw_1 = landmarks[connection[0]]
                        draw_2 = landmarks[connection[1]]

                        draw_frame = cv.line(
                            draw_frame,
                            (
                                int(draw_1.x * width),
                                int(draw_1.y * height)
                            ),
                            (
                                int(draw_2.x * width),
                                int(draw_2.y * height)
                            ),
                            (0, 255, 0),
                            1
                        )

                    for landmark in landmarks:
                        draw_frame = cv.circle(
                            draw_frame,
                            (
                                int(landmark.x * width),
                                int(landmark.y * height)
                            ),
                            4,
                            (255, 0, 0),
                            -1
                        )

            video_writer.write(cv.cvtColor(draw_frame, cv.COLOR_RGB2BGR))

    video_writer.release()
    return hand_poses

def pose_estimation(
    frames: list[cv.Mat],
    draw_save_path: str | None,
) -> list[tuple[HandPose | None, HandPose | None]]:
    if len(frames) == 0:
        return []

    if draw_save_path is not None:
        return __drawn_estimation__(frames, draw_save_path)

    left_label: str = "Left"
    point_a: int = 0
    point_b: int = 5
    point_c: int = 17

    hand_poses: list[tuple[HandPose | None, HandPose | None]] = [
        (None, None) for _ in frames
    ]

    with mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.3,
            min_tracking_confidence=0.3
    ) as hand_model:
        for frame_idx in range(len(frames)):
            frame = frames[frame_idx]
            results = hand_model.process(frame)

            if not results.multi_hand_landmarks:
                continue

            for hand_idx in range(len(results.multi_hand_landmarks)):
                landmarks = results.multi_hand_landmarks[hand_idx].landmark

                min_x: float = float("inf")
                max_x: float = float("-inf")
                min_y: float = float("inf")
                max_y: float = float("-inf")

                for landmark in landmarks:
                    min_x = min(min_x, landmark.x)
                    max_x = max(max_x, landmark.x)
                    min_y = min(min_y, landmark.y)
                    max_y = max(max_y, landmark.y)

                new_pose = HandPose(
                    min_x,
                    min_y,
                    max_x,
                    max_y,

                    landmarks[point_a].x,
                    landmarks[point_b].x,
                    landmarks[point_c].x,

                    landmarks[point_a].y,
                    landmarks[point_b].y,
                    landmarks[point_c].y,
                )

                if results.multi_handedness[hand_idx].classification[0].label == left_label:
                    hand_poses[frame_idx] = (new_pose, hand_poses[frame_idx][1])
                else:
                    hand_poses[frame_idx] = (hand_poses[frame_idx][0], new_pose)

    return hand_poses