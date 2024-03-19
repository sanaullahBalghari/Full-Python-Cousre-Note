class StudentRecord:
    def __init__(self):
        self.boys = []

    def add_student(self):
        name = input("Enter Name: ")
        _class = input("Enter Class: ")
        dob = input("Enter Date of Brith: ")
        email = input("Enter Email: ")


        student_data = {
            'name': name,
            'class': _class,
            'DOB': dob,
            'email': email
        }
        self.boys.append(student_data)
        self.display_students() 

    def search_student(self):
        search_name = input("Enter the name of the student to search: ")
        found = False

        for student_data in self.boys:
            if student_data['name'] == search_name:
                print("Student Details:")
                print(f"Name: {student_data['name']}")
                print(f"Class: {student_data['class']}")
                print(f"Date of Birth: {student_data['DOB']}")
                print(f"Email: {student_data['email']}")
                found = True

        if not found:
            print(f" '{search_name}' not found.")

    def remove_student(self):
        search_name = input("Enter the name of the student to remove: ")

        for student_data in self.boys[:]:
            if student_data['name'] == search_name:
                self.boys.remove(student_data)
                print(f"'{search_name}' are removed.")

    def display_students(self):
        if self.boys:
            print("\n========Student Detial=========")
            for student_data in self.boys:
                print(f"Name: {student_data['name']}")
                print(f"Class: {student_data['class']}")
                print(f"Date of Birth: {student_data['DOB']}")
                print(f"Email: {student_data['email']}")
        else:
            print("No student data available.")


if __name__ == "__main__":
    p1 = StudentRecord()

    while True:
      
        print("==============wellcome===============")
        print("press 1 for add\npress 2 for search\npress 3 for Remove\npress 4 for stop")
        print("=====================================")
        choice = input("Enter your choice: ")

        if choice == '1':
            p1.add_student()
        elif choice == '2':
            p1.search_student()
        elif choice == '3':
            p1.remove_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
