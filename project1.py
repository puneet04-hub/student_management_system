def display_menu():
    print("\n1. Study Management System")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")

def add_student(student_data):
    roll_number = input("Enter Your Roll Number: ")
    if roll_number in student_data:
        print("Student Data Already Exists!")
        return

    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    course = input("Enter Your Course: ")

    student_data[roll_number] = (name, age, course)
    print(f"Student {name} added successfully!")

def delete_student(student_data):
    roll_number = input("Enter Your Roll Number: ")
    if roll_number in student_data:
        del student_data[roll_number]
        print("Student Data Deleted Successfully!")
    else:
        print("Student Not Found!")

def search_student(student_data):
    roll_number = input("Enter Your Roll Number: ")
    if roll_number in student_data:
        name, age, course = student_data[roll_number]
        print(f"Roll Number: {roll_number}, Name: {name}, Age: {age}, Course: {course}")
    else:
        print("Student Not Found!")

def display_students(student_data):
    if not student_data:
        print("No Student Data Available!")
        return

    print("\nAll Students:")
    for roll_number, (name, age, course) in student_data.items():
        print(f"Roll Number: {roll_number}, Name: {name}, Age: {age}, Course: {course}")

def main():
    student_data = {}
    while True:
        display_menu()
        choice = input("Enter Your Choice: ")

        if choice == '1':
            print("Welcome to the Study Management System!")
        elif choice == '2':
            add_student(student_data)
        elif choice == '3':
            delete_student(student_data)
        elif choice == '4':
            search_student(student_data)
        elif choice == '5':
            display_students(student_data)
        elif choice == '6':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
main()
