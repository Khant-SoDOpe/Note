# Note Login Application

This is a simple Note Login application built using Python and Tkinter. The application allows users to sign up and log in using a username and password. Once logged in, users can create, view, and save notes.

## Features

- User Signup
- User Login
- Create and Save Notes
- View Existing Notes

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Files

- `note.py`: The main application file containing the code for the Note Login application.
- `username-password.csv`: A CSV file to store usernames and passwords.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the `note.py` file in your desired directory.
3. Open a terminal or command prompt and navigate to the directory containing `note.py`.
4. Run the application using the command:
    ```bash
    python note.py
    ```

## Usage

1. **Signup**: Enter a username and password, then click the "Signup" button. If the username is already taken, an error message will be displayed.
2. **Login**: Enter your username and password, then click the "Login" button. If the credentials are correct, you will be taken to the note-taking interface.
3. **Create and Save Notes**: Once logged in, you can create notes in the text area provided. Click the "Save" button to save your notes. Click the "Quit" button to exit the application.

## Code Overview

- **Main Class**: Contains all the methods and functionalities for the application.
  - `append_data()`: Appends the username and password to the CSV file.
  - `filecheck()`: Checks if the CSV file exists and creates it if not.
  - `check()`: Checks the username and password for signup and login.
  - `signup()`: Handles the signup process.
  - `login()`: Handles the login process.
  - `Start()`: Initializes the GUI components.
  - `printle()`: Reads and displays the note for the logged-in user.
  - `savefile()`: Saves the note for the logged-in user.
  - `pp()`: Helper method to save the note.
  - `quit()`: Quits the application.
  - `notess()`: Manages the note-taking interface.

## Note

- Ensure that the `username-password.csv` file is in the same directory as `note.py`.
- Passwords are stored in plain text in the CSV file. For a production application, consider using a more secure method for storing passwords.
