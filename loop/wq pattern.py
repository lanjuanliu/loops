# w)
# A
# A B
# A B C
# A B C D
# A B C D E 
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(64+j),end=" ")
        j+=1
    i+=1
    print()