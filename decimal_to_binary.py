n=int(input())
i=0
if n>0:
    while n>=(2**i):
        i+=1
    i-=1
if n<0:
    print("error: number is negative")
else:
    y=""
    while i!=-1:
        if n-(2**i)>=0:
            n-=(2**i)
            y+="1"
        elif n-(2**i)<0:
            y+="0"
        i-=1
    print(y)
