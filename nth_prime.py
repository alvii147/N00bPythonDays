import math

def f(x):
    if x==1:
        return False
    if x==2:
        return True
    if x==3:
        return True
    else:
        y=1
        t=int(math.ceil(x**0.5)+1)
        for i in range(2,t):
            if x%i==0:
                y=0
        if y==1:
            return True
        elif y==0:
            return False

a=0
b=1
n=int(input())
while a<n:
    b+=1
    if f(b) is True:
        a+=1
print(b)
