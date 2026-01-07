# Hand-Gestures-Volume-Controller-

Hand Gesture Volume Controller 🖐️🔊

A contactless system volume controller that uses computer vision to track hand gestures in real-time. Built with OpenCV and MediaPipe, this project allows users to control their computer's master volume simply by pinching their thumb and index finger.

📝 Description

This project leverages the power of Google's MediaPipe framework for robust hand tracking and OpenCV for image processing. It captures video from the webcam, detects hand landmarks, calculates the distance between the thumb and index finger, and maps that distance to the system's volume range.

It provides a hygienic, futuristic, and convenient way to control media without touching a keyboard or mouse.

✨ Key Features

Real-time Tracking: High-speed hand detection and landmark tracking.

Smooth Control: Linear interpolation maps finger distance to volume levels accurately.

Visual Feedback: On-screen volume bar and percentage indicator.

One-Handed Operation: Works with a single hand (left or right).

OS Compatible: Instructions included for both Windows (Pycaw) and macOS (AppleScript).

🛠️ Tech Stack

Language: Python 3.x

Computer Vision: OpenCV (cv2)

Hand Tracking: MediaPipe

Math: NumPy

Audio Control: * pycaw / comtypes (Windows) / osascript (macOS)



⚙️ How It Works

Capture: The webcam feeds frames to the OpenCV module.

Detection: MediaPipe processes the frame to find 21 hand landmarks.

Calculation: The script isolates the coordinates of the Thumb Tip (Landmark 4) and Index Finger Tip (Landmark 8).Distance: The Euclidean distance between these two points is calculated using the formula:  $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Mapping: This distance is interpolated (mapped) to the system's volume range (e.g., distance 50-300 maps to volume 0%-100%).

Execution: The system volume is updated in real-time.



 
