expec_date=int(input("enter expec_date"))
expec_month=int(input("enter expec_month"))
expec_year=int(input("enter expec_year"))
return_date=int(input("enter return_date"))
return_month=int(input("eneter return_month"))
return_year=int(input("enter the return_year"))
if return_date==expec_date:
    if return_month==expec_month:
        if return_year==expec_year:
            print("no fine")
        else:
            print("fine is",(return_year-expec_year)*1000)
    else:
        print("fine is",(return_month-expec_month)*500)
else:
    print("fine is",(return_date-expec_date)*15)