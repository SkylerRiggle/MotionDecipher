# Motion Decipher

## Motion Decipher Arguments

The Motion Decipher class takes in a number of arguments to its constructor that dictate whether intermediate steps are output, as well as determine how the keypress inference occurs. The constructor takes the following form in the *main.py* file:

```python
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
```

The arguments are detailed as follows:

- **input_video_path**: The string representation of the path on your machine to the prerecorded input video file. If this field is *None*, the test defaults to realtime capture.
- **input_video_save_path**: If no input video file path is provided and this variable is set, the resulting realtime capture will be saved to the path specified here.
- **camera_index**: When using realtime capture, this index tells Motion Decipher which camera to use.
- **hand_image_save_path**: If not set to None, this variable indicates the location on disk that the annotated hand images should be saved. Usually used for debugging reasons.
- **save_segments**: This variable indicates whether the keypress segment frames should be saved and labelled in chronological order. Usually used for debugging reasons.
- **plot_estimated_points**: This variable indicates whether the estimated points on the keypad should be plotted, usually for debugging purposes.
- **target_keypad**: The known keypad used by the victim in the video.
- **angle_ambiguous_region**: The ambiguous tolerance for the angle between two estimated points and its correspondence between the angle of two keys.
- **distance_ambiguous_region**: The ambiguous tolerance for the distance between an estimated point and the target key. This is usually set as some percentage of a key's width.
- **camera_view_angle**: An angle between 0 and 90 degrees corresponding to the view angle between the camera and the victim.
- **TMP_SEGMENT_INDICES**: A temporary variable that tells Motion Decipher which frames of the video are keypress events. (***Will be removed once the model is installed into the process.***)

## Running The Example

OUTDATED WILL REWRITE

### Running Single Tests

OUTDATED WILL REWRITE

### Running Multiple Tests

OUTDATED WILL REWRITE

### Finding Output

Once the test case(s) have concluded, the results will be saved to a text file under the same name as the input video file in a folder in the current working directory called *output*. This file will contain a list containing all the inferred candidates for the completed test case.

### Labelling Video Frames (TEMPORARY)

In the file *test_label.py* ensure that all the tests cases you intend to run have been properly added to the *get_label* method with the correct keypress event frames returned in chronological order.

## Gathering Results

OUTDATED WILL REWRITE