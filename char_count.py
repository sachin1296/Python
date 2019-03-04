# count the char present in stirng 
#  example str="sachin"
# s=1
# a=1
# c=1
# h=1
# i=1
# n=1

name = input("enetr your name")
temp=""


for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}  is {name.count(name[i])} times")
        temp+=name[i]