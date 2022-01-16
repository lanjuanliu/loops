language=input("enter the language")
if language=="english":
    print("welcome to statebank of india swape your code")
    balance=5000
    print("choose your transaction balance equitry with draw deposit transfer 5 exit")
transaction=int(input("enter the transaction"))
if transaction==1 or transaction==2 or transaction==3 or transaction==4:
     ATM_PIN = int(input("enter the pin"))
if ATM_PIN == 1234:
       if transaction==1:
           print("collect your card/thank you for using me")
           print("balance is",balance)
elif transaction==2:
    amount=int(input("enter the amount"))
    total=balance-amount
    if amount<=balance:
        print(total)
        print("collect your cash/thankyou for chosing me")
    else:
        print("you have no balance")
elif transaction==3:
    deposite=int(input("enter the deposite amount"))
    total=balance+deposite
    if deposite==0:
        print(total)
        print("your deposite is succesful/thankyou for using me")
    else:
        print("no deposite")
 
    

