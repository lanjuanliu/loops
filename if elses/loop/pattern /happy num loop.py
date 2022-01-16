n=int(input("enter the number"))
temp=n
sum=0
while sum!=0 and sum!=4:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem*rem
        temp=temp//10
        sum=temp
    if sum==1:
        print(sum,"is a happy number")
    else:
        print(sum,"is not a happy number")
