#object refference
class Student:
    college="LPU college"
    def __init__(self,name):self.name= name

s1, s2=Student("Alok"), Student("Gafoor")
print("\n",s1.name,"\n",s1.college,"\n\n",s2.name,"\n",s2.college,"\n\n",Student.college)

#object reffernce
class Student1:
    college="LPU college"
    def __init__(self,name):self.name= name

s3=Student("Aman")
s4=s3
print("\n\n",s3.name,"\n",s4.name)
s4.name= "Rahul"
print("\n\n",s3.name,"\n",s4.name)

s5=Student("Alok")
s6=s5
s7=Student("Alok")
print("\n\ns5 is s6:",s5 is s6,"\ns5 is s7:",s5 is s7)
print(id(s5))
print(id(s6))
print(id(s7))


class Student:
    def __init__(self,name,marks,result):
        self.name, self.marks, self.result = name, marks, result #instance variables

s1= Student("Ashmit",32,"Fail")
print("Name : ",s1.name,'\n',"Marks :  ",s1.marks,'\n',"Result :  ",s1.result)


class Calculator:
    def __init__(self,a,b): self.a, self.b = a, b #instance variables
    def add(self): return self.a + self.b
    def sub(self): return self.a - self.b
    def mul(self): return self.a * self.b
    def div(self): return self.a / self.b
    def pow(self): return self.a ** self.b
    def mod(self): return self.a % self.b
    def rem(self): return self.a // self.b

c1= Calculator(10,5)
print('\nAddition:\n',c1.add(),'\nSubtraction:\n',c1.sub(),'\nMultiplication:\n',c1.mul(),'\nDivision:\n',c1.div(),'\nPower:\n',c1.pow(),'\nModulus:\n',c1.mod())


#object destruction
class Student:
    def __init__(self,name): self.name = name #constructor
    def __del__(self):print("Object Destroyed Successfully")#destructor

s1=Student("Ashmit")
s2=s1
print("In s1:",s1.name)
del s1 #object deleted
print("It still Exists in s2:",s2.name)
del s2 #object reference deleted too


#static method
class Calculator:
    @staticmethod
    def add(a,b): return a + b
    def sub(a,b): return a - b
    def mul(a,b): return a * b
    def div(a,b): return a / b
    def pow(a,b): return a ** b
    def mod(a,b): return a % b
    def rem(a,b): return a // b

print(f'''\nAddition:\n{Calculator.add(10,5)}
\nSubtraction:\n{Calculator.sub(10,5)}
\nMultiplication:\n{Calculator.mul(10,5)}
\nDivision:\n{Calculator.div(10,5)}
\nPower:\n{Calculator.pow(10,5)}
\nModulus:\n{Calculator.mod(10,5)}''')


#class method
class Student:
    college = "ABC Univercity"
    @classmethod
    def cng_clg(cls,name) : cls.college = name
print(Student.college)
Student.cng_clg("LPU Univercity")
print(Student.college)


#All three methods
class Student:
    college = "ABC Univercity"
    def __init__(self,name,marks): self.name, self.marks  = name, marks 
    def display(self):print(self.name,self.marks)
    @classmethod
    def cng_clg(cls) : print(cls.college)
    @staticmethod
    def is_valid_marks(marks): return 0<=marks<=100

s1= Student("Aman",888)
s1.display()
Student.cng_clg()
print(Student.is_valid_marks(s1.marks))


class Student:
    def __init__(self): self.name = "Aman"
    pass
    
class Ashmit(Student):
    pass
s1=Student()
s2=s1
s3=Student()
print(type(s1))
print(id(s1))
print(id(s2))
print(id(s3))
print(isinstance(s1,Student))
print(isinstance(s1,int))
print(issubclass(Ashmit,Student))
print(issubclass(Student,Ashmit))
print(hasattr(s1,"name"))
print(hasattr(s1,"age"))
print(getattr(s1,"name"))
setattr(s1,"email","abc@outlook.com")
print("\n",s1.name,"\n",s1.email)


#HAS-A Relationship -- Car Has an Engine
class Engine:
    def start(self) : print("Engine Started")
    def stop(self) : print("Engine Stopped")
    def broke(self) : print("Something is wrong in your Engine")
    def accelerate(self) : print("Engine is accelerating")

class Car:
    def __init__(self) : self.engine = Engine()
    def start_car(self) : self.engine.start()
    def move_car(self) : self.engine.accelerate()
    def stop_car(self) : self.engine.stop()
    def not_starting(self) : self.engine.broke()

car1 = Car()
#if car1 == Car() : 
car1.start_car()
car1.move_car()
car1.stop_car()
car1.not_starting()
print(type(car1))
print(type(car1.engine))


class Student:
    def __init__(self, name, vid) : self.name, self.vid = name, vid
class Teacher:
    def __init__(self, t_name) : self.t_name = t_name
    def teach(self, student) : print(f"{self.t_name} is teaching {student.name} : {student.vid}")
    def mentor(self, student) : print(f"{self.t_name} is mentoring {student.name} : {student.vid}")

stu1=Student("Ashmit",12601011)
stu2=Student("Alok",12601019)
stu3=Student("Aman",12601016)
t1=Teacher("Pratik")
t1.teach(stu1)
t1.mentor(stu2)
t1.teach(stu3)


class Address:
    def __init__(self, city) : self.city = city
class Student:
    def __init__(self, name, address) : self.name, self.address = name, address

add1 = Address("Mumbai")
stu1 = Student("Ashmit",add1)
print(stu1.name,"\n",stu1.address.city)


class Student:
    def __init__(self,name,rollno,marks):self.name, self.rollno, self.marks = name, rollno, marks
    def display(self):print("Name:",self.name,"\nRoll no:",self.rollno,"\nMarks:",self.marks,"\nPercentage:",self.percentage,"%")
    def allmarks(self, physics,chemistry,maths): 
        if 0<=physics<=100 and 0<=chemistry<=100 and 0<=maths<=100:
            self.marks=physics+chemistry+maths
            self.percentage=round(self.marks/3,3)
        else:
            print("Invalid Marks")
            pass
s1 = [Student("Ashmit",20,0), Student("Alok",21,0), Student("Ashu",22,0), Student("Amit",23,0)]
s1[0].allmarks(78,88,45)
s1[1].allmarks(68,98,66)
s1[2].allmarks(42,83,40)
s1[3].allmarks(38,81,70)
s1[0].display()
s1[1].display()
s1[2].display()
s1[3].display()
# import pandas as pd
# data = pd.DataFrame([s1[0].display()],[s1[1].display()],[s1[2].display()],[s1[3].display()])
# print(data)


class Employee:
    def __init__(self,name,age,salary):self.name, self.age, self.salary = name, age, salary
    def display(self):print("Name:",self.name,"\nAge:",self.age,"\nSalary:",self.salary,"\nAnnual salary:",self.salary*12)
s1 = [Employee("Ashmit",36,78000),Employee("Amit",31,56000),Employee("Alok",40,90000),Employee("Mita",28,23000)]
s1[0].display()
s1[1].display()
s1[2].display()
s1[3].display()


class Employee:
    def __init__(self,name,age,salary):self.name, self.age, self.salary = name, age, salary
    def display(self):print("\nName:",self.name,"\nAge:",self.age,"\nSalary:",self.salary)
    def calc_annual_salary(self):print("Annual salary:",self.salary*12)
s1 = [Employee("Ashmit",36,78000),Employee("Amit",31,56000),Employee("Alok",40,90000),Employee("Mita",28,23000)]
s1[0].display()
s1[0].calc_annual_salary()
s1[1].display()
s1[1].calc_annual_salary()
s1[2].display()
s1[2].calc_annual_salary()
s1[3].display()
s1[3].calc_annual_salary()


class Rectangle:
    def __init__(self,length,breadth):self.length, self.breadth = length, breadth
    def display_area(self):print(f"\nLength:{self.length}, Breadth:{self.breadth}\nArea of Rectangle:{self.length*self.breadth}")
    def display_perimeter(self):print(f"\nLength:{self.length}, Breadth:{self.breadth}\nPerimeter of Rectangle:{2*(self.length+self.breadth)}")

s1 = [Rectangle(12,8),Rectangle(4,3),Rectangle(10,2)]
s1[0].display_area()
s1[0].display_perimeter()
s1[1].display_area()
s1[1].display_perimeter()
s1[2].display_area()
s1[2].display_perimeter()


class rectangle:
    def __init__(self,length,breadth):
        self.length, self.breadth = length, breadth
    def display(self,option):
        # self.Area, self.Perimeter = Area, Perimeter
        if option=="Area":
            Area = self.length*self.breadth
            print(f"\nLength: {self.length} Breadth: {self.breadth}\nArea of Rectangle:{Area}")
        if option=="Perimeter":
            Perimeter = 2*(self.length+self.breadth)
            print(f"\nLength: {self.length} Breadth: {self.breadth}\nPerimeter of Rectangle:{Perimeter}")
s1 = [rectangle(12,8),rectangle(4,3),rectangle(10,2)]
s1[0].display("Perimeter")
s1[0].display("Area")


class BankAccount:
    def __init__(self,account_holder,balance):self.account_holder, self.balance = account_holder, balance
    def deposit(self,deposit):
        self.deposit = deposit
        self.balance = self.balance+self.deposit
        print(f"\nDeposited Ammount:{self.deposit}\nTotal Balance:{self.balance}")
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        self.balance = self.balance-self.withdraw
        print(f"\nWithdrawn Ammount:{self.withdraw}\nTotal Balance:{self.balance}")
    def display(self):print(f"\nAccount Holder Name:{self.account_holder}, Balance:{self.balance}")

s1 = BankAccount("Pratik",999999)
s1.display()
s1.deposit(500)
s1.withdraw(80000)
s1.display()


class Car:
    def __init__(self,brand,model,price):
        self.brand, self.model, self.price = brand, model, price
    def display(self):
        print(f"\nBrand Name:{self.brand}, Model:{self.model}, Price:{self.price}")

allcars=[Car("BMW","S3",8000000),Car("Audi","A5",9500000),Car("Porche","911",12600000),Car("Audi","Q3",7300000)]
for i in allcars:
    i.display()

costly_car = max(allcars, key=lambda allcars : allcars.price)

print(f"The most expensive car is {costly_car.brand} {costly_car.model}")


class Car:
    def __init__(self,brand,model,price):self.brand, self.model, self.price = brand, model, price
    def display(self):print(f"\nBrand Name:{self.brand}, Model:{self.model}, Price:{self.price}")
    def costly_car(self, cars):
        costly = max(cars, key=lambda car: car.price)
        print(f"The most expensive car is {costly.brand} {costly.model}")
s1=[Car("BMW","S3",8000000),Car("Audi","A5",9500000),Car("Porche","911",12600000),Car("Audi","Q3",7300000)]
for cars in s1:
    cars.display()
s1[2].costly_car(s1)