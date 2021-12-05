age=int(input("enter the age"))                                                                                                                 
if age>=18:
    print("can take vaccine")
    vaccination=input("enter yes or no")
    if vaccination=="yes":
         print("can go for 2nd dose")
    else:
         print("go for 1st dose")
else:
    print("can't take vaccine")
