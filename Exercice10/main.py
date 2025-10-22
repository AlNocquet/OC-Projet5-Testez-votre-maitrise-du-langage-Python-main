
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Nom: {self.name}")
        print(f"Âge: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


# --- Tests ---
if __name__ == "__main__":
    p = Person("Alice", 30)
    e = Employee("Olivier", 40, 3500)

    print("Détails Person :")
    p.display_details()

    print("\nDétails Employee :")
    e.display_details()