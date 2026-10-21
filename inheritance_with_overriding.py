class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.05


class Developer(Employee):
    def bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def bonus(self):
        return self.salary * 0.20


d = Developer("Ravi", 50000)
m = Manager("Priya", 60000)

print(d.name, d.bonus())
print(m.name, m.bonus())