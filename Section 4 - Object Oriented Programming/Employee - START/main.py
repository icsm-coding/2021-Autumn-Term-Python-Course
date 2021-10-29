class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def greeting(self):
        print(f'Hello my name is {self.name}. I am {self.age} years old. My role is {self.role}')

    def increment_age(self):
        self.age += 1

    def change_role(self, new_role):
        self.role = new_role

charlie = Employee(name='Charlie', age=21, role='Shelf stocker')

# charlie.age = 22
# print(charlie.age)

# charlie.increment_age()
# print(charlie.age)k


charlie.change_role(new_role='Manager')
print(charlie.role)