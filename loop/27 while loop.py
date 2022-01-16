num=int(input("enter the number"))
sum=0
i=1
temp=num
while i<=temp:
        if temp%i==0:
           sum=sum+i
           i+=1
           if num==sum:
                  print("prim number")
           else:
                print("not prim number")
                