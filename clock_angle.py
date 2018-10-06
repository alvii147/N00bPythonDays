h=int(input()) #input hours
m=int(input()) #input minutes
if h>24 or m>60 or h<0 or m<0:
    print("error in input")
if len(str(m))==1:
    u=str("0"+str(m))
else:
    u=str(m)
if len(str(h))==1:
    v=str("0"+str(h))
else:
    v=str(h)
print("At "+v+":"+u)
if h>=12 and h<=24:
    h-=12
if h*5>=m:
    a=(h-(m/5))*30
    b=(m/60)*30
    c=a+b
    if c>180:
        c-=180
    print("angle is "+str(c))
if h*5<m:
    d=((m/5)-h)*30
    e=(m/60)*30
    f=d-e
    if f>180:
        f-=180
    print("angle is "+str(f))
