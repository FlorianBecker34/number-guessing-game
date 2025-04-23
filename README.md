# Number Guessing Game

A simple command-line number guessing game written in Python.

## Description

This script implements a classic number guessing game. The computer selects a random number, and the player tries to guess it. Hints are provided whether the guessed number is too high or too low. The game includes a simple highscore system.

## Features

* Two difficulty levels:
    * Level 1: Guess an integer between 0 and 20.
    * Level 2: Guess a floating-point number (with one decimal place) between 0.0 and 20.0.
* Feedback on whether the guessed number is higher or lower than the target number.
* Simple highscore system: +20 points for a correct answer, -5 points for a wrong answer.
* Option to cancel guessing or difficulty selection by entering `999`.
* Basic error handling for invalid inputs.

## Prerequisites

* Python 3.6

## Installation

No special installation is required. You just need Python 3 on your system. Download the `zahlen_raten.py` file or clone the repository.

## Usage

1.  Open a terminal or command prompt.
2.  Navigate to the directory where the `zahlen_raten.py` file is located.
3.  Start the game using the command:
    ```bash
    python zahlen_raten.py
    ```
4.  Follow the in-game instructions: Select a difficulty level (1 or 2) and enter your guesses. Enter `999` to exit a guessing round or the difficulty selection.


## Author

Florian Becker
