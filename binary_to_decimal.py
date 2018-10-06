n=str(input())
x=0
while x<len(n):
    if str(n[x])!="1" and str(n[x])!="0":
        print("error in input")
        x=-1
        break
    else:
        x+=1
if x>0:
    x=0
    y=int()
    i=len(n)-1
    while x<len(n):
        if str(n[x])=="1":
         y+=2**i
         i-=1
         x+=1
        elif str(n[x])=="0":
         i-=1
         x+=1
    print(y)
