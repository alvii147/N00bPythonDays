i=int(input())
x=0
print(i)

while i!=1:
    if i%2==0:
        i=int(i/2)
    else:
        i=int((i*3)+1)
    print(i)
    x+=1

print("\nnumber of times the operation was performed: "+str(x))
