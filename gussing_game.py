import random
num=random.randint(1,100)
count=0
while True:
    num1=int(input("enetr number"))
    if num1>num:
        print("too high")
    if num1<num:
        print("too low")
    if num1==num:
        print("you win")
        count+=1
        break
    count+=1
