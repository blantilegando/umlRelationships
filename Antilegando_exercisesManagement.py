#heliumAntilegando_theAbstractScientist.py
#Name: Betelgeuse L. Antilegando
#Section: Helium


from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age


    def get_name(self):
        return self.name


    def get_age(self):
        return self.__age

    @abstractmethod
    def role(self):
        print(f"{self.__name} is a person")


    def display_info(self):
        print(f"\nName: {self.name}\nAge: {self.__age}  #It's better because the process is clean and avoids errors.")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

    def role(self):
        print(f"{self.name} is a student")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

    def role(self):
        print(f"{self.name} is a teacher")

class Principal(Person):
    def  manage_school(self):
        print(f"{self.name} is managing the school")

    def role(self):
        print(f"{self.name} is the principal")

class GuidanceCounselor(Person):
    def  assist_students(self):
        print(f"{self.name} is assisting the students")

    def role(self):
        print(f"{self.name} is the guidance counselor")

person1 = Student("Lina", 20)
person1.display_info()
person1.study()
person1.role()

print("")

person2 = Teacher("Mona", 30)
person2.display_info()
person2.teach()
person2.role()

print("")

person3 = Principal("Mr. X", 55)
person3.display_info()
person3.manage_school()
person3.role()

print("")

person4 = GuidanceCounselor("Maan", 2528)
person4.display_info()
person4.assist_students()
person4.role()

print("")

people = [person1, person2, person3, person4]

for classs in people:
    classs.role()

print("\n\n Reflection Answers: \n")
print("1. Encapsulation protects information such that it ensures that the information is only accessible through that class.")
print("2. Student inherits features from Person by making Person a parent class which in this case putting Person in the parenthesis when defining the classes.")
print("3. Role can produce different results for different objects because it was redefined seperately throughout the different classes.")
print("4. Person is made an abstract class so that we can abstract the method role().")
print("5. The four pillars ensure that this system is complete and free of errors. It makes this system more clear and easier for the users to interpret.")