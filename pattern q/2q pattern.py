# b)
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

n=5
i=n
while i>=0:
    j=0
    while j<i:
        print(n-j,end=" ")
        j+=1
    i-=1
    print()
