class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def display_info(self):
        print(f"\nName: {self.name}\nAge: {self.age}")

person1 = Person("Lina", 20)
person1.display_info()