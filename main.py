from sys import argv
from os import listdir, mkdir
from test_labels import get_label
from os.path import join, exists, isdir
from motion_decipher import MotionDecipher, META_QUEST_3_KEYPAD


def run_test(test_folder_path: str, test_video_name: str):
    if not test_video_name.endswith(".mp4"):
        return

    case_title = test_video_name.replace(".mp4", "").strip()

    test_case = MotionDecipher(
        input_video_path = join(test_folder_path, test_video_name),
        input_video_save_path = None,
        camera_index = 0,
        hand_image_save_path = None,
        save_segments = False,
        plot_estimated_points = False,
        target_keypad = META_QUEST_3_KEYPAD,
        angle_ambiguous_region = 22.5,
        distance_ambiguous_region = (0.75, 0.5),
        camera_view_angle = 90.0,

        TMP_SEGMENT_INDICES = get_label(case_title)
    )

    if not (exists("./output") and isdir("./output")):
        mkdir("./output")

    out_file = open(f"./output/{case_title}.txt", "w")
    sequences, errors = test_case.run()
    sequences.sort(key=lambda x : errors[x])
    for sequence in sequences:
        out_file.write(f"{sequence}, {errors[sequence]}\n")
    out_file.close()

def run_all_tests(test_folder_path: str):
    counter: int = 0
    in_files = listdir(test_folder_path)
    for file in in_files:
        counter += 1
        print(f"Processing File {counter} of {len(in_files)}.")
        try:
            run_test(test_folder_path, file)
        except Exception as e:
            print(f"An error has occurred...\n{e}")

if __name__ == '__main__':
    test_directory: str | None = None
    test_filename: str | None = None

    for arg in argv:
        if arg.startswith("dir="):
            test_directory = arg.replace("dir=", "").strip()
        elif arg.startswith("file="):
            test_filename = arg.replace("file=", "").strip()

    if test_directory is None:
        print("No Input Directory Specified...")
        quit(-1)

    if test_filename is not None:
        run_test(test_directory, test_filename)
    else:
        run_all_tests(test_directory)