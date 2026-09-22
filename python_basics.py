print("hi")

print('''
      What's up bro!
      How are you''')

print("hello", end=" ")
print("hi")

print("Hi", end=" | ")
print("Hello")

print("How","Why","When", sep=" | ")

print("What's your age:",5)

print("comments")
#This will print comments

print("What \nHow") # \n is used for next line
print("Too \t Far") # \t is used for tab or 4 spaces

#Data_Types
age = 20
height = 5.8
name = "abcd"
i_man = True
complx = 2+3j
print(type(age))
print(type(height))
print(type(name))
print(type(i_man))
print(type(complx))

#Arthematic_operations
a=10
b=2
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)
print(a,"%",b,"=",a%b)
print(a,"**",b,"=",a**b)
print(a,"//",b,"=",a//b)

y=10
print(y)
y+=5
print(y)
y-=2
print(y)
y*=3
print(y)
y/=2
print(y)

a=20
b=15
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

marks=80
attendance=85
print(marks > 40 and attendance > 75)
print(marks > 90 or attendance > 75)
print(not(marks > 40))

fruit=["mango","apple","cherry"]
print("mango" in fruit)
print("banana" in fruit)
print("tomato" not in fruit)

a = [10,20]
b = a
c = [10,20]
print(a is b)
print(a is c)
print(a == b)

name = input("Enter Name: ")
print("Hello!",name)

age = float(input("Enter Age: "))
print(age)

#basic_Calculator
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=input("enter operation : ")
if c=="+" : print(a,"+",b,"=",a+b)
elif c=="-" : print(a,"-",b,"=",a-b)
elif c=="*" : print(a,"*",b,"=",a*b)
elif c=="/" : print(a,"/",b,"=",a/b)
elif c=="%" : print(a,"%",b,"=",a%b)
elif c=="**" : print(a,"**",b,"=",a**b)
elif c=="//" : print(a,"//",b,"=",a//b)

num=int(input("enter a number: "))
if num > 0 : print("The number ",num," is Positive.")
if num < 0 : print("The number ",num," is Negative.")

num=int(input("enter a number: "))
if num % 2 == 0 : print("The number ",num," is Even.")
else : print("The number ",num," is Odd.")

day=int(input("enter day number(1-7): "))
if day == 1: print("Monday")
elif day == 2: print("Tuesday")
elif day == 3: print("Wednesday")
elif day == 4: print("Thursday")
elif day == 5: print("Friday")
elif day == 6: print("Saturday")
elif day == 7: print("Sunday")
else:print("Invalid day")

choice =int(input("enter a number(1-3): "))
match choice:
    case 1: print("you selected pizza.")
    case 2: print("you selected burger.")
    case 3: print("you selected sandwitch.")
    case _: print("Invalid choice.")
    
num=int(input("enter first number : "))
num1=int(input("enter second number: "))
num2=int(input("enter third number: "))
if num>num1 and  num>num2:print(num," is larger than",num1," and ",num2)
elif num1>num and  num1>num2:print(num1," is larger than",num," and ",num2)
elif num2>num and  num2>num1:print(num2," is larger than",num," and ",num1)
else:print("Either same or invalid.")

#built in functions
numbers=[10,20,30,40,50]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(type(numbers))

#user-defined functions
def welcome():
    print("Hello, welcome to LPU uni")
welcome()

def intro(name="Guest"):#func with one paremeter and default value as Guest
    print("Hi",name,"\nHow are you!")
intro()
intro("Pratik")

def addition(a,b):#func with two paremeter
    print(a,"+",b,"=",a+b)
addition(654,76)

def greet(name,age):#func with positional argument
    print("Hi",name,"!")
    print("You are",age, "years old")
greet("Pratik",21)

def greet(name,age):#func with keyword argument
    print("Hi",name,"!")
    print("You are",age, "years old")
greet(age=26,name="Ujjwal")

#variable length
def add(*args): # *args are tuple
    print(args)
    print(type(args))
    print(sum(args))

add(10,243,6,676,786,434.90)
add(423)
# add("abc","def") TypeError: unsupported operand type(s) for +: 'int' and 'str'

#diff b/w print and return
def double(x):
    print(x*2)
result = double(5)
print(result)#'print' Prints twice one with value and another without 

def double(x):
    return(x*2)
result = double(5)
print(result)#return is used where you define it t a variable and then print it once

#local variable
def show():
    x=10 #inside the function
    print(x)
show()
#print(x) NameError: name 'x' is not defined 

#global variable
y=25 #outside the function
def show():
    print(y)
show()
print(y)

def show():
    global z #use global keyword inside a function
    z=50
    print(z)
show()
print(z)

#calc pass or fail
    
def result(marks):
    if marks>89 and marks<101 : print("Pass, Grade O")
    elif marks>79 and marks<90 : print("Pass, Grade A")
    elif marks>69 and marks<80 : print("Pass, Grade B")
    elif marks>59 and marks<70 : print("Pass, Grade C")
    elif marks>49 and marks<60 : print("Pass, Grade D")
    elif marks>39 and marks<50 : print("Reappear, Grade E")
    elif marks<40 and marks>-1 : print("Fail, Grade F")
    else : print("Invalid entry")
        
num = int(input("Enter your marks: "))
result(num)

#check even odd
def result(num):
    if num/2==0 : print(num ,"is an Even number")
    elif num/2!=0 : print(num,"is an Odd number")
    else : print("Invalid entry")

num1 = int(input("Enter a number: "))
result(num1)

#recursive function
def factorial_recursive(n):
    if n<0:print("not defined for negative number")
    if n<=1:return 1
    return n * factorial_recursive(n-1)

num1 = int(input("Enter a number: "))
print(factorial_recursive(num1),"is the factorial of",num1)
    
#class
class  Student :
    pass
#object
s1=Student()
s2=Student()
s3=Student()
print(type(s1))
#<class '__main__.Student'> here __main__ acts as a constructor here

#adding data to objects
s1.name,s1.age,s1.marks = "Aman",19,85
s2.email,s2.course,s2.program = "Alok@gmail.com","Python","MCA"
print(s1.name,'\n',s1.age,'\n',s1.marks)
print(s2.email,'\n',s2.course,'\n',s2.program)

#constructor
'''
__init__
__main__
'''

class Student:
    def __init__(self):
        print("student object created")

s1= Student()
#find out can we write anything in place of '__init__' constructor and 'self' keyword

class Student:
    def __init__(self,name,age):
        self.name, self.age = name, age #instance variables

s1= Student("Ashmit",32)
print("Name : ",s1.name,'\n',"Age :  ",s1.age)

class Student:
    def __init__(self,name,age):
        self.name, self.age = name, age
    def display(self): #instance method (functions which are used to call the self or instance)
        print("Name : ",self.name)
        print("Age : ",self.age)

s1= Student("Ashmit",32)
s1.display()

class Rectangle:
    def __init__(self,length,breadth):
        self.length, self.breadth = length, breadth
    def area(self):
        area =  self.length*self.breadth
        #return self.length*self.breadth
        print("Area : ",area)
    def perimeter(self):
        perimeter = 2*(self.length+self.breadth)
        #return 2*(self.length+self.breadth)
        print("Perimeter : ",perimeter)

rec=Rectangle(4,6)
rec.area()
rec.perimeter()

class BankAccount:
    def __init__(self,name,balance):
        self.name, self.balance= name, balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def display_balance(self):
        print("Name : ",self.name,"\n","Balance : ",self.balance)

account=BankAccount("Aman",5000)
account.display_balance()
account.deposit(2000)
account.display_balance()
account.withdraw(1000)
account.display_balance()

#object refference
class Student:
    college="abc college"
    def __init__(self,name):
        self.name= name

s1=Student("Aman")
s2=Student("Riya")
print(s1.name)
print(s1.college)
print()
print(s2.name)
print(s2.college)
print()
print(Student.college)