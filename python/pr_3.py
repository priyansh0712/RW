class Student:
    student=[]
    def setdata(self, name, dob, age, grade, subject,std_id):
        self.student.append({
            "name": name,
            "grade": grade,
            "subject":subject,
            "info":(dob,age,std_id)
        })

    def getdata(self):
        name = input("Enter your name: ")
        dob = input("Enter your date of birth: ")
        age = input("Enter your age: ")
        grade = input("Enter your grade: ")
        subject = input("Enter your subject: ")
        std_id = input("Enter your student ID: ")
        return name, dob, age, grade, subject,std_id
    
    def update(self, std_id):
        for student in self.student:
            if student["info"][2] == std_id:
                name = input("Enter your name: ")
                grade = input("Enter your grade: ")
                subject = input("Enter your subject: ")
                student["name"] = name
                student["grade"] = grade
                student["subject"] = subject
                print("Student updated successfully!")
                return
        print("Student not found.")

def main():
    print('Welcome to the student data Organizer!')
    while True:
        print("\nSelect the option :")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. update student")
        print("5. delete student")
        print("6. display subject offered")
        print("7. Exit")
        option = int(input("Enter your choice (1-7): "))
        match option:
            case 1:
                name, dob, age, grade, subject,std_id = Student().getdata()
                Student().setdata(name, dob, age, grade, subject,std_id)
                print("Student added successfully!")
            case 2:
                print("Displaying all students...")
                for student in Student.student:
                    print(f"Name: {student.get('name')}, Grade: {student.get('grade')}, Subject: {student.get('subject')}, DOB: {student.get('info')[0]}, Age: {student.get('info')[1]}, Student ID: {student.get('info')[2]}")
            case 3:                
                std_id = input("Enter the student ID to search: ")
                for student in Student.student:
                    if student["info"][2] == std_id:
                        print(student)
                        break
                    else:
                        print("Student not found.")       
            case 4:
                std_id = input("Enter the student ID to update: ")
                Student().update(std_id)
            case 5:
                std_id = input("Enter the student ID to delete: ")  
                for student in Student.student:
                    if student["info"][2] == std_id:
                        Student.student.remove(student)
                        print("Student deleted successfully!")
                        break
                    else:
                        print("Student not found.")
            case 6:
                subjects = set(student["subject"] for student in Student.student)
                for s in subjects:
                    print(s,end=", ")    
            case 7:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")
main()