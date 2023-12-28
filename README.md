# Car Tracking with OpenCV

This simple Python script uses the OpenCV library to perform car tracking and stop sign detection in a video stream. It utilizes Haar cascades for both cars and stop sign detection.

## Dependencies

- OpenCV: `pip install opencv-python`

## Usage

1. Download the pre-trained Haar cascade XML files for vehicle and stop sign detection and place them in the "CarTracking" directory.

    - [vehicle_haarcascades.xml]([path/to/vehicle_haarcascades.xml](https://github.com/amendahawi/VehicleDetection/blob/main/stop_sign_haarcascade.xml))
    - [stop_sign_haarcascade.xml]([path/to/stop_sign_haarcascade.xml](https://github.com/amendahawi/VehicleDetection/blob/main/vehicle_haarcascades.xml))

2. Update the video file path in the script:

    ```python
    vid = cv2.VideoCapture("video/file.mp4")
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. The script will display the video stream with rectangles around detected cars and stop signs.

## Script Explanation

- The script initializes Haar cascade classifiers for car and stop sign detection.
- It reads frames from the specified video file and converts them to grayscale.
- Car and stop sign detection is performed using `detectMultiScale` method.
- Rectangles are drawn around detected cars and stop signs, and labels are added.
- The processed frames are displayed in a window named "Face Detector app."
- Press 'q' to exit the application.

## Author

Abdulrahman Mendahawi

Feel free to modify and extend this script according to your requirements.
