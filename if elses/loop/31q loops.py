# Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
n=int(input("enter the number"))
i=1
sum=1
while i<=n:
    sum=sum*i
    print(sum,"+",end=" ")
    i+=1
