caps=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

small=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

sym=["@", "#", "_", "&", "-", "!", "?", "-", "(", ")", "+", "*", ":", ";", "/"]

n=str(input())
score=0
s1=0
s2=0
s3=0
s4=0

for i in n:
    for c in caps:
        if str(i)==str(c):
            s1=1

for i in n:
    for s in small:
        if str(i)==str(s):
            s2=1

for i in n:
    for k in num:
        if str(i)==str(k):
            s3=1

for i in n:
    for r in sym:
        if str(i)==str(r):
            s4=1

if s1==1 and s2==1:
    score+=2
elif s1!=1 and s2!=1:
    score-=2

if s3==1:
    score+=2

if s4==1:
    score+=2

if len(n)>=12:
    score+=3
elif len(n)>=8:
    score+=1
elif len(n)<8:
    score-=1

if score>=8:
    print("Password Strength: Very Strong")
elif score>=6:
    print("Password Strength: Strong")
elif score>=4:
    print("Password Strength: Fair")
elif score>0:
    print("Password Strength: Weak")
elif score<=0:
    print("Password Strengh: Poor")
