class Person:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name

    def return_name(self):
        return self.name

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    def printNameSubject(self):
        print(f'{self.name}, {self.subject}')

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        super().__init__(first_name, last_name)
        self.course = course

    def printNameCourse(self):
        print(f'{self.name}, {self.course}')