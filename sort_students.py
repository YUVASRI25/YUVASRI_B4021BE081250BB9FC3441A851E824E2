class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    student_list.sort(key=lambda x: x.cgpa, reverse=True)

# Create a list of student objects
students = [
    Student("Alice", "101", 3.9),
    Student("Bob", "102", 3.7),
    Student("Charlie", "103", 3.5),
    Student("David", "104", 3.8),
]

# Sort the list based on CGPA in descending order
sort_students(students)

# Print the sorted list
for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
  