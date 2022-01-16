# q)
# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=2
#     i+=2
#     print()


num=int(input("enter the number"))
temp=num
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem*rem
        temp=temp//10
    temp=sum
if sum==1:
    print("happy number")
else:
    print("not happy number")

