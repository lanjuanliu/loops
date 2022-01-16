# num=int(input("enter the number"))
# sum=0
# i=num
# while i>0:
#     degit=i%10
#     sum+=degit**num
#     i//=10
# if num==sum:
#     print(num,"armstrong number")
# else:
#    print(num,"not an armstrong number")


num=int(input("enter the number"))
user=len(str(num))
sum=0
temp=num
while temp>0:
    degit=temp%10
    sum=sum+degit**user
    temp=temp//10
if num==sum:
    print(num,"armstrong number")
else:
    print(num,"is not an armstrong number")
