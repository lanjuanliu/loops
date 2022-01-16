# num=1
# while(num<=100):
#     count=0
#     i=2
#     while(i<=num//2):
#         if (num%i==0):
#             count=count+1
#             break
#         i+=1
#     if (count==0 and num!=1):
#         print('%d'%num)
#     num=num+1


num=int(input("enter the number"))
while num<=100:
    count=0
    i=2
    while i<=num//2:
        if num%i==0:
            count=count+1
            break
        i+=1
    if count==0 and num!=1:
        print(num,end=" ")
        if count==0 and num!=0:
            print("prim num ")
        else:
            print("is not an prim number")
    num=num+1
        
# i=0
# while i<3:
#     print(i)
#     i+=1
#     print(0)

# n=int(input("enter the number"))
# i=0
# while i<n:
#     j=1
#     count=0
#     while j<=n:
#         if i%j==0:
#             count=count+1
#             j=j+1
#             if count==2:
#                 print(i,"prime num")
#             i+=1


    