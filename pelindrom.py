# pelindrom number in pyhton

num = int(input("enter number"))
num1=num
print(num1)
total=0
while num1>0:
    total=total * 10+ num1%10
    print(total)
    num1=num1//10
    print(total)
print(total)
if num==total:
    print( 'is pelindrom')
