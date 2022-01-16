expec_date=int(input("enter the expec_date"))
expec_month=int(input("enter the expec_month"))
expec_year=int(input("enter the expec_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if return_date==expec_date:
    if return_month==expec_month:
        if return_year==expec_year:
            print("no fine")
        else:
            print("fine is",(return_year-expec_year)*15)
    else:
        print("fine is",(return_month-expec_month)*500)
else:
    print("fine is",(return_date-expec_date)*10000)
    