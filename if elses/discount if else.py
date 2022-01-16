# age=int(input("enter the age"))
# sex=input("enter male/female")
# if sex=="female":
#     print("work in urban place")
# elif age>=20 and age<=40:
#     if sex=="male":
#         print("can work anywhere")
# elif age>=40 and age<=60:
#     if sex=="male":
#         print("he will work in urban area")
# else:
#     print("error")


a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
if a>b and b>c or c>b and b>a:
    print(b,"is the middle number")
elif a>c and c>b or b>c and c>a:
    print(c,"is the middle number")
elif c>a and a>b or b>a and a>c:
    print(a,"is the middle number")
elif a<b and b<c or c<b and b<a:
    print(b,"is the middle number")
elif a<c and c<b or b<c and c<a:
    print(c,"is the middle number")
elif c<a and a<b or b<a and a<c:
    print(a,"is the middle number")