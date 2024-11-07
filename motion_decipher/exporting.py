import cv2 as cv


def export_image(frame: cv.Mat, save_path: str):
    cv.imwrite(save_path, cv.cvtColor(frame, cv.COLOR_RGB2BGR))

def export_video(frames: list[cv.Mat], save_path: str):
    if len(frames) == 0:
        return

    height, width, _ = frames[0].shape

    writer = cv.VideoWriter(
        save_path,
        cv.VideoWriter_fourcc(*"MP4V"),
        30,
        (width, height)
    )

    for frame in frames:
        writer.write(cv.cvtColor(frame, cv.COLOR_RGB2BGR))

    writer.release()