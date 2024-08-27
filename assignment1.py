# PURPOSE: STUDENT MANANGEMENT SYSTEM
# AUTHOR LUCKY MATALE
# 27/08/2024

class Student:
    def __init__(self, id, name, age, major):
        if not isinstance(id, int) or len(str(id)) > 6:
            raise ValueError("ID must be a number and not exceed ten digits.")  # Ensure ID is a number and not exceed ten digits
        if age <= 0:
            raise ValueError("Age must be greater than zero.")  # Ensure age is greater than zero
        self.id = id
        self.name = name.upper()  # Ensure name is always uppercase
        self.age = age
        self.major = major

    def update_student(self, name=None, age=None, major=None):
        if name:
            self.name = name.upper()  # Ensure name is always uppercase
        if age is not None:
            if age <= 0:
                raise ValueError("Age must be greater than zero.")  # Ensure age is greater than zero
            self.age = age 
        if major:
            self.major = major

    def display_student(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")  # Display student details

class StudentManagementSystem:
    def __init__(self): 
        self.students = []  # Initialize an empty list to store students

    def add_new_student(self, id, name, age, major):
        student = Student(id, name, age, major)  # Create a new student object
        self.students.append(student)  # Add the student to the system

    def delete_student(self, student_id):
        self.remove_student(student_id)  # Remove the student from the system

    def update_student_info(self, student_id, name=None, age=None, major=None):
        for student in self.students:
            if student.id == student_id:
                student.update_student(name, age, major)  # Update student information

    def is_student_id_exists(self, student_id):  # Checks if student ID exists
        return any(student.id == student_id for student in self.students)

    def show_all_students(self):
        for student in self.students:
            student.display_student()  # Display all students

    def search_student(self, student_id):  # Searches for student using ID
        for student in self.students:  # Uses loop to search through self.students
            if student.id == student_id:  # Compares if student ID matches any ID in the student list
                student.display_student()  # Display the found student
                break
        else:
            print("Student not found")  # Inform if student is not found

# Defines the main function, and entry point of executable code
def main():
    
    system = StudentManagementSystem()  # Create an instance of StudentManagementSystem

    # Menu Loop
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Update student information")
        print("4. View all students")
        print("5. Search for a student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:  # Ensure ID is a number and not exceed six digits
                try:
                    id = int(input("Enter student ID: ")) 
                    if len(str(id)) > 6:  # Check if ID exceeds six digits
                        raise ValueError("ID must be a number and not exceed six digits.")
                    break
                except ValueError as e:
                    print(f"Invalid ID: {e}. Please try again.")  # Inform user of invalid ID

            name = input("Enter student name: ").upper()  # Ensure name is always uppercase

            while True:  # Ensure age is greater than zero
                try:
                    age = int(input("Enter student age: "))
                    if age <= 0:
                        raise ValueError("Age must be greater than zero.")
                    break
                except ValueError as e:
                    print(f"Invalid age: {e}. Please try again.")  # Inform user of invalid age

            major = input("Enter student major: ").upper()  # Ensure major is always uppercase
            system.add_new_student(id, name, age, major)  # Add new student to the system

        elif choice == '2':  # Deletes a student ID from student database
            if not system.students:  # Checks if there are students available to delete
                print("No students available to delete.")
                continue  # Skips the rest of the loop and goes back to the start
            while True:
                try:
                    student_id = int(input("Enter student ID to delete: "))
                    if not system.is_student_id_exists(student_id):  # Checks if student ID is available
                        raise ValueError("Student ID does not exist.")
                    system.delete_student(student_id)  # Delete the student
                    break
                except ValueError as message:
                    print(f"Invalid ID: {message}. Please try again")  # Inform user of invalid ID

        elif choice == '3':  # Updates student information
            if not system.students:  # Checks if there are students available to update
                print("No students available to update.")
                continue
            while True:  # Ensures student ID entered exists
                try:
                    student_id = int(input("Enter student ID to update: "))
                    if not system.is_student_id_exists(student_id):  # Checks if student ID is available
                        raise ValueError("Student ID does not exist.")
                    break
                except ValueError as message:
                    print(f"Invalid ID: {message}. Please try again.")  # Inform user of invalid ID

            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            major = input("Enter new major (leave blank to keep current): ")
            system.update_student_info(student_id, name or None, int(age) if age else None, major or None)  # Update student info

        elif choice == '4':  # Displays all available students
            if not system.students:
                print("No students available.")
                continue
            system.show_all_students()  # Show all students

        elif choice == '5':  # Searches for students
            if not system.students:
                print("No students available.")
                continue
            student_id = int(input("Enter student ID to search: "))
            system.search_student(student_id)  # Search for the student by ID

        elif choice == '6':  # Exits menu loop
            break
        else:
            print("Invalid choice. Please try again.")  # Inform user of invalid choice

if __name__ == "__main__":
    main()  # Calls the main function to run the program
