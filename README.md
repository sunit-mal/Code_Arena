# Code_Arena

![Logo](https://github.com/sunit-mal/Code_Arena/assets/110469858/49d6d256-9f85-4cb2-882b-e8a2ed7cdc8a)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation Process](#installation-process)
- [Usage](#usage)
- [Exam Cell](#exam-cell)
- [Contributing](#contributing)
- [Project Creators](#project-creators)
- [License](#license)

## Introduction

Code Arena is a web-based platform that provides an environment for executing programs in various programming languages such as C, C++, Python, and Java. This project includes a built-in online compiler that allows users to compile and run their code within an online terminal. Additionally, it offers the capability to verify whether the program works correctly using test cases submitted by the user.

## Features

- **Online Code Execution**: Write, compile, and run code in languages like C, C++, Python, and Java directly in your web browser.
- **Interactive Terminal**: Utilize an online terminal to see program output and interact with your code.
- **Code Testing**: Validate the functionality of your code by running it against provided test cases.
- **User Authentication**: Secure access with user authentication for tracking user activity.
- **Exam Cell**: Organize and manage exams, check results, and download results as Excel files.
- **Face Recognition**: During exam time student under AI base face recognition system.
- **Tech Stack**: Built using Python, Django (Backend), HTML, CSS, and JavaScript (Frontend).
- **Database Options**: Supports SQLite (also MySQL and MongoDB can be used) for data storage.
- **Easy Installation**: Quick setup process for getting the project up and running.

## Tech Stack

- **Python**: Used as the primary programming language.
- **Django Backend**: Implements the backend logic following the MVT architecture.
- **SQLite Database**: Default database for data storage (also supports MySQL and MongoDB).
- **HTML, CSS, JavaScript Frontend**: Provides the user interface and interactivity.

## Installation Process

To set up Code_Arena on your local machine, follow these steps:

1. **Download the Project Files**: Clone or download the project files to your computer.

2. **Activate Your Virtual Environment (if you're using one)**:
   ```bash
   source <path_to_virtualenv>/bin/activate
3. Navigate to Your Project Directory:
    `cd Code_Arena`
4. Install Project Dependencies from requirements.txt:
    `pip install -r requirements.txt`
5. Create Database Migrations:
    `python manage.py makemigrations`
6. Apply Database Migrations:
    `python manage.py migrate`
7. Create a Superuser (for Administrative Access):
    `python manage.py createsuperuser`
8. Start the Django Development Server:
    `python manage.py runserver`
9. If There's an Issue Related to Static Files:
    `python manage.py collectstatic`

## Usage
Here's how you can use Code_Arena:

  Register and Log In: Create an account or log in to your existing one.
  Choose a Programming Language: Select the programming language in which you want to write code.
  Write and Test Code: Use the online editor to write your code, and run it to see the output. You can also test your code against provided test cases.

View Results: Review the results of your code execution.

## Exam Cell
Organize Exams: Teachers can organize and manage exams within the platform.
Check Results: View and verify the results of exams conducted.
Download Results: Download exam results as Excel files for further analysis.
Face Recognition: During Exam period student are not allow try cheating. It has AI base Face Recognition system and also disable visiting inspect mode.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and test thoroughly.
Create a pull request with a clear description of your changes.

## Project Creators

- [Sunit Mal](https://github.com/sunit-mal)
- [Samapon Ghosh](https://github.com/samaponghosh)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
