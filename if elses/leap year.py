# year=int(input("enter the year"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")

# month=input("enter the month number")
# if month=="january":
#     print("31 days")
# elif month=="febuary":
#     print("28 or 29 days")
# if month=="march":
#     print("31 days")
# if month=="april":
#     print("30 days")
# if month=="may":
#     print("31 days")
# if month=="june":
#     print("30 days")
# if month=="july":
#     print("31 days")
# if month=="august":
#     print("31 days")
# if month=="september":
#     print("30 days")
# if month=="october":
#     print("31 days")
# if month=="november":
#     print("30 days")
# if month=="december":
#     print("31 days")
# else:
#     print("not included")



month_num=int(input("enter the month no"))
if month_num==2:
    print("this month have 28 or29 month")
elif month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
    print("this month have 31 days")
else:
    print("this month have 30 days")



                                                               