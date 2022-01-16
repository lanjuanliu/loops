# j)
#             1
#           2 1
#         3 2 1
#       4 3 2 1
#     5 4 3 2 1

i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end= " ")
        j+=1
    b=1
    while b<=j:
        print(j,end=" ")
        b+=1
    print()
    i+=1

