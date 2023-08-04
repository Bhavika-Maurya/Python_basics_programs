class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

# Creating three objects of the Student class
student1 = Student(101, "John Doe", 18, "A")
student2 = Student(102, "Alice Smith", 17, "B")
student3 = Student(103, "Bob Johnson", 19, "A+")

# Accessing the attributes of each student
print("Student 1:")
print("Roll Number:", student1.roll_number)
print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)

print("\nStudent 2:")
print("Roll Number:", student2.roll_number)
print("Name:", student2.name)
print("Age:", student2.age)
print("Grade:", student2.grade)

print("\nStudent 3:")
print("Roll Number:", student3.roll_number)
print("Name:", student3.name)
print("Age:", student3.age)
print("Grade:", student3.grade)
