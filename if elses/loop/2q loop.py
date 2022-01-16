i=1
while i<=100:
    if i%7==0:
        print(i)
    i+=1


i=1
while i<=100:
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    elif i%3==0 and i%7==0:
        print("nav gurukul")
    else:
        print(i)
    i+=1


