# n=int(input("enter the number"))
# temp=n
# sum=0
# i=1
# while temp%i==0:
#     sum=sum+n
#     if sum==temp:
#         print(sum,"is a perfect number")
#     else:
#         print(sum,"is not a perfect number")
#     i+=1

# n=int(input("enter the umber"))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum=sum+n
#         i+=1
#         if sum==n:
#             print(sum,"is a perfect number")
#         else:
#             print(sum,"is not an perfect number")


num=int(input("enter the number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
        if sum==num:
            print(num,"is a perfect number")
        else:
            print(num, "is not a perfect  number")
        i+=1