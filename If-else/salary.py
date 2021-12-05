ser=int(input("enter the period service"))
sal=int(input("enter the salary"))
if ser<10:
    bo=10/100*sal
if ser>=6 and ser>=10:
    bo =8/100*sal
if ser<6:
    bo=5/100*sal
    print("bonus is",bo)

