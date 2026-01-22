class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"My name is {self.name} and I am studying {self.course}."


if __name__ == "__main__":
    student = Student("Haibo", "CSCN8010")
    print(student.introduce())
