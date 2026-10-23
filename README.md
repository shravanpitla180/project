# Daily Habit Tracker

A simple command-line application for keeping track of daily habits. Add habits, mark them complete for today, view their status, and see your progress as a summary and pie chart.

## Features

- Add habits and prevent duplicate names.
- View each habit’s status for today.
- Mark a habit as completed once per day.
- See today’s completion count, pending count, and completion rate.
- Display a pie chart of completed and pending habits.
- Remove habits you no longer want to track.
- Save habits between runs in a local `habits.txt` file.

## How It Works

When the program starts, it reads saved habits from `habits.txt`. Each habit is stored on its own line using this format:

```text
Habit name|Completion date
For example:
Read for 20 minutes|2026-10-23
Exercise|
The program keeps the habit data in a list while it runs. Adding, completing, or removing a habit updates that list and saves it back to habits.txt.
Completion dates use the YYYY-MM-DD format. When you view habits or progress, the program compares each saved completion date with today’s date to determine whether the habit is completed or pending. Marking a habit complete records today’s date, so it cannot be marked complete again on the same day.
For the progress view, the program uses Pandas to organize the habits into a table, NumPy to calculate the completion totals and percentage, and Matplotlib to draw the pie chart.
Requirements
- Python 3
- NumPy
- Pandas
- Matplotlib
Installation
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required packages:
   pip install numpy pandas matplotlib
Run the Program
Run the Python file containing the tracker:
python habit_tracker.py
Replace habit_tracker.py with the name of your Python file if it differs.
Use the menu to add, view, complete, or remove habits, view your progress, or exit.
Project Structure
.
├── habit_tracker.py   # Main application
├── habits.txt         # Created automatically to store habits
└── README.md          # Project documentation
Data and Privacy
Habit data is stored locally in habits.txt in the folder where the program runs. The program does not require an account or send this data to an online service.
Possible Improvements
- Track completion history and streaks.
- Add weekly or monthly progress reports.
- Allow users to edit habit names.
- Add automated tests.
