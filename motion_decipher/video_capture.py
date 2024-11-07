import cv2 as cv


def capture_video_file(file_path: str) -> list[cv.Mat]:
    frames: list[cv.Mat] = []
    video_capture = cv.VideoCapture(file_path)

    while video_capture.isOpened():
        has_data, frame = video_capture.read()
        if not has_data:
            break

        frames.append(cv.cvtColor(frame, cv.COLOR_BGR2RGB))

    video_capture.release()

    return frames

def capture_video_realtime(cam_idx: int) -> list[cv.Mat]:
    frames: list[cv.Mat] = []
    video_capture = cv.VideoCapture(cam_idx)
    window_name: str = "Motion Decipher Capture"

    cv.namedWindow(window_name)

    while video_capture.isOpened():
        has_data, frame = video_capture.read()
        if not has_data:
            break

        frames.append(frame)
        cv.imshow(window_name, frame)

        if (
            cv.waitKey(1) == ord("q") or
            cv.getWindowProperty(window_name, cv.WND_PROP_VISIBLE) < 1
        ):
            break

    cv.destroyAllWindows()
    video_capture.release()

    for idx in range(len(frames)):
        frames[idx] = cv.cvtColor(frames[idx], cv.COLOR_BGR2RGB)

    return frames