i=int(input("enter the number"))
rev=0
while i>0:
    degit=i%10
    rev=rev*10+degit
    i=i//10
    print(rev)