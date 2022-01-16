language=input("enter the language")
if language=="english":
    print("welcome to the state bank of india")
    balance=50000
    print("enter ur transactn:\n1balnc entry\n2witdrw\n3dposit\n4trnsfer\n5exit")
    transactn=int(input("enter the transaction:"))
    if transactn==1 or transactn==2 or transactn==3 or transactn==4:
        atmpin=int(input("enter the pin:"))
        if atmpin==1234:
            if transactn==1:
                print("collect ur card/thank you")
                print("balance is",balance)
            elif transactn==2:
                witdrw=int(input("enter the witdrw amout:"))
                if witdrw<=balance:
                    total=balance-witdrw
                    print(total)
                    print("collect ur money/thankyou")
                else:
                    print("you have no balance")
            elif transactn==3:
                dpsit=int(input("enter the dpsit amount:"))
                if dpsit>=0:
                    total=balance+dpsit
                    print(total)
                    print("tour ur dpsit is succesful\.thank you")
                else:
                    print("no dpsit")
            elif transactn==4:
                trnsfer=int(input("enter the trnsfer:"))
                if trnsfer>0:
                    total=balance-trnsfer
                    print(total)
                    print("your money has been trnsfer/.thankyou ")
                else:
                    print("trnsfer fail")
            else:
                print("wrong pin")
        elif transactn==0:
            exit=input("do you wnt to exit:")
            if exit=="yes":
                print("thank you for visiting")
            else:
                print("choose ur trnsactn")
else:
    print("language does not found")
    

    
            






