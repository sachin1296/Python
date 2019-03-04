# pelindrom using for loop
num=input("enter number")
l=len(num)
total=0
num1=int(num)
num2=num1

for i in range(l):
    total=total*10+num1%10
    num1=num1//10;              # // for integer division and / is for float division 

if num2==total:
    print("pelindrom")