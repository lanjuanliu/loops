# t)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n=5
i=0
while i<n:
    space=n-i-1
    while space>0:
        print(end=" ")
        space=space-1
    star=i+1
    while star>0:
        print("*",end=" ")
        star=star-1
    i+=1
    print()

