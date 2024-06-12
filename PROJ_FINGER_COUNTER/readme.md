# Hand Tracking Gesture Recognition

Welcome to the Hand Tracking Gesture Recognition project! This project uses computer vision to track hand movements and
recognize hand gestures to display the corresponding number of fingers being held up.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This project leverages OpenCV and MediaPipe to detect hand landmarks and count the number of fingers being held up. It
uses simple hand gestures to recognize the number of fingers and display the count on the video feed.

## Features

- Real-time hand detection and tracking using OpenCV and MediaPipe.
- Gesture recognition to count the number of fingers being held up.
- Visual feedback with FPS and finger count display.
- Easy to use and extend for other hand gesture-based applications.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

## Usage

1. Run the script

  ```bash
   python name_of_your_file.py
   ```

2. The script will open your webcam and start detecting your hand movements. Show different numbers of fingers to see
   the corresponding number displayed on the video feed.

3. Press q to exit the application.

## Project Structure

```bash
PROJ_FINGER_COUNTER/
│
├── HANDTRACKING/
│   └── handtracking_module.py  # Contains the hand tracking module
│
├── main.py  # Main script to run the project
│
├── readme.md  # Project documentation  # List of required packages
```