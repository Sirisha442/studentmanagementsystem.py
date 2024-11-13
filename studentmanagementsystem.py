# Student Management System

# Define a dictionary to store student data
students = {}

# Function to add a student
def add_student(rollnumber, name, age, DOB, address, course, fee, collegename):
    if rollnumber in students:
        print("Roll Number already exists.")
    else:
        students[rollnumber] = {
            'Name': name, 
            'Age': age, 
            'DOB': DOB, 
            'Address': address, 
            'Course': course, 
            'Fee': fee, 
            'CollegeName': collegename
        }
        print(f"Student {name} added successfully.")

# Function to view all students
def view_students():
    if not students:
        print("No students found.")
    else:
        for student_id, details in students.items():
            print(f"Rollnumber: {student_id}, Name: {details['Name']}, Age: {details['Age']}, DOB: {details['DOB']}, Address: {details['Address']}, Course: {details['Course']}, Fee: {details['Fee']}, College: {details['CollegeName']}")

# Function to update a student's details
def update_student(rollnumber, name=None, age=None, DOB=None, address=None, course=None, fee=None, collegename=None):
    if rollnumber in students:
        if name:
            students[rollnumber]['Name'] = name
        if age:
            students[rollnumber]['Age'] = age
        if DOB:
            students[rollnumber]['DOB'] = DOB
        if address:
            students[rollnumber]['Address'] = address
        if course:
            students[rollnumber]['Course'] = course
        if fee:
            students[rollnumber]['Fee'] = fee
        if collegename:
            students[rollnumber]['CollegeName'] = collegename

        print(f"Student_ID {rollnumber} updated successfully.")
    else:
        print("Student ID not found.")

# Function to delete a student
def delete_student(rollnumber):
    if rollnumber in students:
        del students[rollnumber]
        print(f"Student ID {rollnumber} deleted successfully.")
    else:
        print("Student ID not found.")

# Function to search for a student by ID
def search_student(rollnumber):
    if rollnumber in students:
        details = students[rollnumber]
        print(f"ID: {rollnumber}, Name: {details['Name']}, Age: {details['Age']}, DOB: {details['DOB']}, Address: {details['Address']}, Course: {details['Course']}, Fee: {details['Fee']}, CollegeName: {details['CollegeName']}")
    else:
        print("Student ID not found.")

# Main menu function
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rollnumber = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
            address = input("Enter Address: ")
            course = input("Enter Course: ")
            fee = input("Enter Fee: ")
            collegename = input("Enter College Name: ")
            add_student(rollnumber, name, age, DOB, address, course, fee, collegename)
        
        elif choice == '2':
            view_students()
        
        elif choice == '3':
            student_id = input("Enter Roll Number to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            age = input("Enter new Age (leave blank to keep current): ")
            DOB = input("Enter new DOB (leave blank to keep current): ")
            address = input("Enter new Address (leave blank to keep current): ")
            course = input("Enter new Course (leave blank to keep current): ")
            fee = input("Enter new Fee (leave blank to keep current): ")
            collegename = input("Enter new College Name (leave blank to keep current): ")
            update_student(
                student_id, 
                name if name else None, 
                int(age) if age else None, 
                DOB if DOB else None, 
                address if address else None, 
                course if course else None, 
                int(fee) if fee else None, 
                collegename if collegename else None
            )
        
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        
        elif choice == '5':
            student_id = input("Enter Student ID to search: ")
            search_student(student_id)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
