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
    for sequence in test_case.run():
        out_file.write(sequence + "\n")
    out_file.close()

def run_all_tests(test_folder_path: str):
    counter: int = 0
    in_files = listdir(test_folder_path)
    for file in in_files:
        counter += 1
        print(f"Processing File {counter} of {len(in_files)}.")
        run_test(test_folder_path, file)

if __name__ == '__main__':
    # run_test("./tests/4-Key", "0119.mp4")
    run_all_tests("./tests/5-Key")