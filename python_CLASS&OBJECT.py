# Q3. Triangle
class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        print(f"The area of triangle is {(self.base * self.height) / 2}")

    def perimeter(self):
        print(f"The perimeter of triangle is {self.side1 + self.side2 + self.side3}")


t1 = Triangle(5, 8, 19, 22, 17)
t1.area()
t1.perimeter()


# Q4. Student
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}\nRoll number: {self.roll_no}\nMarks: {self.marks}")

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


students_list = [
    Student("Pratik", 1, 78),
    Student("Alok", 2, 38),
    Student("Amrit", 3, 57),
    Student("Kartik", 4, 89),
]
for student in students_list:
    student.display()
    student.result()


# Q5. Employee Salary
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}\nEmployee ID: {self.emp_id}\nSalary: {self.salary}")

    def annual(self):
        print(f"Annual Salary: {self.salary * 12}")

    def bonus(self):
        print(f"Bonus: {self.salary * 0.1}")


employees_list = [
    Employee("Pratik", 1, 78000),
    Employee("Alok", 2, 38000),
    Employee("Amrit", 3, 57000),
    Employee("Kartik", 4, 89000),
]
for employee in employees_list:
    employee.display()
    employee.annual()
    employee.bonus()


# Q6. Cars
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}/-")

    def discount(self):
        print(f"10% Discount: {self.price * 0.1}/-")

    def final_price(self):
        self.price = self.price - (self.price * 0.1)
        print(f"Final Discounted Price: {self.price}/-\n")


cars_list = [
    Car("BMW", "S3", 8000000),
    Car("Audi", "A5", 9500000),
    Car("Porche", "911", 12600000),
    Car("Audi", "Q3", 7300000),
]
for car in cars_list:
    car.display()
    car.discount()
    car.final_price()


# Q8. Bank Account
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.acc_no}\nName: {self.name}\nBalance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}\nBalance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}\nBalance: {self.balance}")
        else:
            print(f"Invalid Amount\nRemaining Balance: {self.balance}")


account = BankAccount(1213345331, "Pratik", 10000)
account.display()
account.deposit(1234)
account.withdraw(7890)
account.withdraw(4000)


# Q9. Mobile
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")

    def costly(self, mobile_list):
        expensive = max(mobile_list, key=lambda mobile: mobile.price)
        print(
            f"The most expensive Mobile: \n"
            f"Brand: {expensive.brand}\n"
            f"Model: {expensive.model}\n"
            f"Price: {expensive.price}"
        )


mobiles = [
    Mobile("Samsung", "A30", 40000),
    Mobile("Oneplus", "Nord", 35000),
    Mobile("Apple", "14", 80000),
]
for mobile in mobiles:
    mobile.display()
mobiles[0].costly(mobiles)
