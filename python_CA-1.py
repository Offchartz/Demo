#QUESTION-1
class Book:
    def __init__(self,title,author,price,quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def display(self): #To Display the details of the book.
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\nQuantity: {self.quantity}")

    def total_value(self):
        self.price=self.price*self.quantity  #To calculate the total price we need (price * quantity)
        print(f"Total value of Product: {self.price}")

b1= [Book("Night's Watch","GOT",500,2),Book("Diary of Anne","Anne",1500,2),Book("Cruize","Amber.H",680,2)] #list of books
for book in b1: #To print all details of books
    book.display()
    book.total_value()
    
#QUESTION-2
class Employee:
    def __init__(self,name,department,salary,performance_score):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = performance_score

    def display(self): #To display the Employee details
        print(f"\nName: {self.name}\nDepartment: {self.department}\nSalary: {self.salary}\nPerformance Score: {self.performance_score}")

    def bonus(self):
        if self.performance_score>=80: #It will only run (add bonus) if the performance score is greater than or equal to 80
            print(f"{self.name} is eligible for bonus of {self.salary*0.1}")
            self.salary = self.salary+(self.salary*0.1) #Bonus is added to the salary
            print(f"Total Salary: {self.salary}")
        else:
            print("Not eligible for bonus.")
e1 = [Employee("Karan","IT",50000,81),Employee("Kiran","HR",90000,76),Employee("Kunal","IT",35000,88)]
for emp in e1:
    emp.display()
    emp.bonus()
i=0
for emp in e1: #This loop finds all the employees and 'if' condition is used to count the eligible  employees
    if emp.performance_score>80:
        i = i+1
print("Number of employees eligible for bonus : ",i)

#QUESTION-3
class ElectricityBill:
    def __init__(self,customer_name,units,rate_per_unit):
        self.customer_name = customer_name
        self.units = units
        self.rate_per_unit = rate_per_unit

    def display(self): #To display the Electricity Bill Details
        print(f"\nName: {self.customer_name}\nUnits: {self.units}\nrate per unit: {self.rate_per_unit}")

    def bill(self):
        bill = self.rate_per_unit*self.units #To calculate the bill
        if bill>=2000: #If bill is more than 2000 then it'll add a supercharge of 5%
            bill = bill+(bill*0.05)
            print("5% Super Charge Applicable.")
            print(f"Final Bill : {bill}")
        else:
            print(f"Final Bill : {bill}")

bill1=[ElectricityBill("Pratik",100,18),ElectricityBill("Ritik",450,27),ElectricityBill("Kartik",500,22)]
for bill in bill1:
    bill.display()
    bill.bill()
