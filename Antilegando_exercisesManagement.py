class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"\nName: {self.name}\nAge: {self.__age}  #It's better because the process is clean and avoids errors.")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

person1 = Student("Lina", 20)
person1.display_info()
person1.study()

person2 = Teacher("Mona", 30)
person2.display_info()
person2.teach()