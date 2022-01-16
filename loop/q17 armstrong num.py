num=int(input("enter the number"))
user=len(str(num))
sum=0
temp=num
while temp>0:
    degit=temp%10
    sum=sum+degit**user 
    temp=temp//10
    if num==sum:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")


