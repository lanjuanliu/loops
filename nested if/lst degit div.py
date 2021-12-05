num=int(input("enter the number"))
if num%10:
    last_digit=num%10
    print( "lastdigit is:",last_digit)
    if last_digit%3==0:
        print("divisible")
    else:
        print("not divisible")