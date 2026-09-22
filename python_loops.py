#LOOPS
#For loop
for i in range(3):
    for i in range(50):
        print("_",end="-")
    print("\n")
    
for i in range(5):print(i)

for i in range(5,11):print(i)

for i in range(2,21,2):print(i)

for i in range(20,0,-2):print(i)

list1=[2,3,4,6,8,7,8]
for i in list1:
    print(i)
    
t1=(2,3,4,6,8,7,8)
for i in t1:
    print(i)
    
list1=[2,3,4,6,8,7,8]
total=0
for i in list1:
    total=total+i
print(total)

list1=[20,30,40,60,80,70,80]
for i in list1:
    if i>50:
        print(f"The numbers greater than 50 in {(list1)} is {i}")
        
for i in range(1,30,2):
    if i==17:break
    print(i)
    
for i in range(1,10):
    if i==6 or i==3 or i==9:
        continue
    print(i)

#While loop
i=1
while i<=5:
    print(i)
    i+=1
    
i=10
while i>=1:
    print(i)
    i-=1
    
for i in range(1):
    for j in range(1):
        for k in range(5):
            print(i,j,k)
            