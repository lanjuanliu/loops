user=int(input("enter the number"))
if user==5:
    print( 2/user)
elif user>=6 and user<=10:
    print(3/user)
elif user>=10 and user<=15:
    print(4/user)
elif user>15:
    print(5/user)
else:
    print("no charge")