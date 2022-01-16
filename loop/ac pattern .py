# ac)
# A 
#  
# B  C

# D  E   F

# G  H   I   J

i=1
k=1
while i<=4:
    j=1
    while j<=i:
        print(chr(64+k),end="  ")
        j+=1
        k+=1
    print()
    i+=1