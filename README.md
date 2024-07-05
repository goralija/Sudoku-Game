# Sudoku Game

## Overview

Sudoku Game is a Python-based application that allows users to play Sudoku, register, log in, and track their game statistics. The game features a graphical interface built with Pygame and uses SQLite for user data management.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Descriptions](#file-descriptions)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

To get started with the Sudoku Game, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/Sudoku-Game.git
    cd Sudoku-Game
    ```

2. **Create a Virtual Environment and Install Dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python main.py
    ```

## Usage

1. **Login or Register:**
    - Upon starting the application, you will be prompted to log in or register.
    - If you are a new user, select "Register" and provide a username and password.
    - If you are an existing user, select "Login" and enter your credentials.

2. **Select Difficulty and Play:**
    - After logging in, choose the difficulty level (Easy, Medium, Hard) to start playing.
    - The game board will be displayed, and you can start solving the Sudoku puzzle.

3. **Tracking Statistics:**
    - Your game statistics (wins and losses) will be tracked and displayed in the menu.

## Features

- **Graphical Interface:** Built with Pygame for an interactive user experience.
- **User Authentication:** Register and log in to track your personal game statistics.
- **Dynamic Difficulty Levels:** Choose from Easy, Medium, and Hard puzzles.
- **Game Statistics:** Track your wins and losses.
- **Popup Messages:** Informative messages for invalid moves and game status.

## The Most Important File Descriptions

- **main.py:** Entry point for the application. Manages the main game loop and integrates other modules.
- **login.py:** Handles user login and registration, interacts with the SQLite database.
- **database.py:** Contains functions for setting up and interacting with the SQLite database.
- **menu.py:** Displays the main menu and difficulty selection screen.
- **handle_events.py:** Manages user inputs and game events.
- **draw_the_board.py:** Renders the Sudoku board and user interface components.
- **input_field.py:** Manages input fields for text input in the registration and login forms.
- **form_handle.py:** Handles form submissions for login and registration.
- **sudoku_solver.py:** Contains the logic for solving Sudoku puzzles.

## Technologies Used

- **Python:** The core programming language used for the application.
- **Pygame:** Used for creating the graphical user interface.
- **SQLite:** A lightweight database to manage user data.
- **PyInstaller:** To create standalone executables for distribution.

---

### Technical Overview

#### Graphical Interface
The graphical interface is built using Pygame, a powerful library for creating games and multimedia applications. The board and UI elements are drawn dynamically, and user interactions are handled through event loops.

#### User Authentication
User registration and login functionalities are implemented using SQLite. The `login.py` and `database.py` modules handle the creation of user accounts, authentication, and statistics tracking.

#### Sudoku Solver
The `sudoku_solver.py` module contains the backtracking algorithm for solving Sudoku puzzles. This ensures that the puzzles presented to the users are solvable, and it also validates user moves during the game.

#### Event Handling
User inputs and game events are managed by the `handle_events.py` module. This module captures mouse clicks, key presses, and other interactions, updating the game state accordingly.

#### Modular Design
The project is structured into multiple modules, each responsible for a specific functionality. This modular approach ensures maintainability and scalability, making it easier to extend the game's features in the future.

---

Feel free to modify the content as needed to better fit your project and preferences.
