# Pomodoro Timer

The Pomodoro Timer is a Python application that helps you manage your time effectively using the Pomodoro Technique. It utilizes the tkinter and pygame libraries to create a simple graphical user interface (GUI) for the timer.

## Usage

1. Make sure you have Python installed on your machine.

2. Clone this repository to your local machine or download the source code.

3. Install the required dependencies by running the following command:
`pip install pygame`

4. Run the program by executing the `main.py` script:
`python main.py`

5. The GUI window will appear, displaying a timer with a tomato image.

6. Click the "Start" button to begin the Pomodoro timer. The timer will run for 25 minutes by default, followed by a 5-minute short break. After completing four cycles (25 minutes of work and 5 minutes of short break), a longer break of 20 minutes will be scheduled.

7. The timer will count down the time, and the label above the timer will display the current phase (work or break).

8. When the timer reaches zero, it will automatically transition to the next phase. The number of completed work sessions will be displayed with checkmarks below the timer.

9. You can click the "Reset" button at any time to reset the timer and start a new session.

## Sound

The application plays a ringing sound at the end of each work session. The sound file `bell.mp3` is included in the resources folder.

## Resource Path

The `get_resource_path` function is used to retrieve the absolute path to resource files. It takes a relative path as an argument and returns the absolute path to the file.

## Screenshot

## Game Screenshot

<img src="screenshot.png" alt="Game Screenshot" width="400">



