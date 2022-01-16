i = 2
num=int(input("enter a number"))
while (i):    
    if (num%i == 0):
        print(num, 'is not a prime number')
        i = i + 1
        break
    else:
         print(num, 'is a prime number')
         i+=1
         break
