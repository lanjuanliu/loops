num=int(input("enter the number"))
if num%10:
    last_degit=num%10
    print("last degit is;",last_degit)
    if last_degit%3:
        print("divisible")
    else:
        print("not divisible")