# row=5
# print("right triangle pattern of number")
# for i in range(1,row + 1):
#     for j in range (1,i + 1):
#         print('%d'%i, end=' ')
#     print()


# row=5
# print('inverted triangle ')
# for i in range(1,row + 1):
#     for j in range(1,row + 1):
#         if(j<i):
#             print('',end='')
#         else:
#             print('%d'%i,end=' ')
#     print()


# row=5
# print("triangle")
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         if(j<i):
#             print('',end=' ')
#         else:
#             print('%d'%i,end=' ')
#     print()

# i=1
# sum=0
# while i<=140:
#     if i%3==0:
#         sum=sum+i
#         print(sum)
#     i=i+1


# i=0
# while i<10:
#     j=0
#     while j<=5:
#     #     print(j)
#         # j=j+1
#         print(j)
#         j=j+1
#         i=i+1
# print(i)
# i=i+1

# i=0
# num=int(input("enter the number"))
# while i<=num:
#     if i>0:
#         print("positive")
#     if i<0:
#         print("negetive") 
#     else:
#         print("zero") 
#         i+=1


n=5
i=n
while i>=1:
    j=0
    while j<i:
        print(n-j,end=" ")
        j+=1
    i-=1
    print()




