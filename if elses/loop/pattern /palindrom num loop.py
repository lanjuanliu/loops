n=int(input("enter the number"))
temp=n
rev=0
while temp>0:
    degit=temp%10
    rev=rev*10+degit
    temp=temp//10
if n==rev:
    print(n,"is a palindrom number")
else:
    print(n,"is not an palindrom")


# num=int(input("enter the number"))
# sum=0
# temp=num
# while temp>0:
#     rem=temp%10
#     sum=sum+rem
#     temp=temp//10
# if temp%sum==0:
#     print(num,"is a harshad number")
# else:
#     print(num,"is not a harshad mumber")
