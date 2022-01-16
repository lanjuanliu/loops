# i=1
# k=1
# while i<=4:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         k+=1
#         j+=1
#     print()
#     i+=1

i=1
k=0
while i<=3:
    j=1
    while j<=i:
        while j<=i+i:
            print(k,end=" ")
            j+=1
            k+=1
    print()
    i+=1