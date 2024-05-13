"""2)შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ
 გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა 
 შემთხვევაში იმუშაოს"""


num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
num4 = int(input("enter a number: "))
num5 = int(input("enter a number: "))

list = []
list.append (num1)
list.append (num2)
list.append (num3)
list.append (num4)
list.append (num5)

for i in list:
    if i %2 ==0:
        print(i)
