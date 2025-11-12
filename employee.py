class employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    def increase_salary(self):
        self.salary = self.salary+0.2*self.salary

    def print_salary(self):
        print("Salary:", self.salary)

    def set_salary(self, new_salary):
        self.salary = new_salary


emp1 = employee("Jester", 45, 80000)
emp2 = employee("Jadu", 15, 50000)
emp1.increase_salary()
emp1.print_salary()
emp2.increase_salary()
emp2.print_salary()

