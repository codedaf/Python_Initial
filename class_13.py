"""
In this example, both the Student and Teacher classes inherit from the Person class. 
They each have their own additional attributes ('student_id' for Student and 'subject' for Teacher)
 while also inheriting the 'name' and 'age' attributes from the Person class. 
 Instances of these subclasses can access both their specific 
 attributes as well as those inherited from the Person superclass.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

# Example usage
person1 = Person("John", 30)
student1 = Student("Alice", 25, "S12345")
teacher1 = Teacher("Mr. Smith", 40, "Math")

print(person1.name, person1.age)
print(student1.name, student1.age, student1.student_id)
print(teacher1.name, teacher1.age, teacher1.subject)




