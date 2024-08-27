# ASSIGNMENT-TWO

# Student Management System
    This project is a simple Student Management System implemented in Python. It allows users to add, delete, update, view, and search for student records. The system is designed to be run from the command line and provides a menu-driven interface for interacting with the student database.

# Features
    Add a Student: Add a new student to the system with an ID, name, age, and major.
    Delete a Student: Remove a student from the system using their ID.
    Update Student Information: Update the name, age, or major of an existing student.
    View All Students: Display all students currently in the system.
    Search for a Student: Search for a student by their ID.
    Exit: Exit the application.

# Requirements
    Python 3.x

# Usage
    1. Clone the repository:
        git clone <repository-url>
        cd <repository-directory>
    2. Run the application:
         python assignment1.py
    3. Follow the on-screen menu to interact with the system.

# Code Overview
Student Class
  Attributes:

    id: Integer, unique identifier for the student.
    name: String, name of the student (stored in uppercase).
    age: Integer, age of the student (must be greater than zero).
    major: String, major of the student.
  Methods:

    __init__(self, id, name, age, major): Initializes a new student.
    update_student(self, name=None, age=None, major=None): Updates the student's information.
    display_student(self): Displays the student's details.

StudentManagementSystem Class
  Attributes:

    students: List, stores all student objects.
  
  Methods:

    add_new_student(self, id, name, age, major): Adds a new student to the system.
    delete_student(self, student_id): Deletes a student by ID.
    update_student_info(self, student_id, name=None, age=None, major=None): Updates a student's information.
    is_student_id_exists(self, student_id): Checks if a student ID exists in the system.
    show_all_students(self): Displays all students.
    search_student(self, student_id): Searches for a student by ID.
    
    main() Function
    Provides a menu-driven interface for interacting with the student management system.
    Handles user input and calls the appropriate methods from the StudentManagementSystem class.
    Example
    Menu:
      1. Add a student
      2. Delete a student
      3. Update student information
      4. View all students
      5. Search for a student
      6. Exit
      Enter your choice: 1
      Enter student ID: 123456
      Enter student name: John Doe
      Enter student age: 20
      Enter student major: Computer Science

# Contributing
    Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes

# Known Issues
    Still updating menu bugs...

# Contact
    For any questions or suggestions, please contact Lucky Matale at luckymatale03@gmail.com.
