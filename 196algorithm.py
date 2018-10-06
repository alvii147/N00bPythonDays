def flip(n):
    n=str(n)
    i=len(n)-1
    result=""
    while i>=0:
        result=result+n[i]
        i-=1
    return result

def palindrome(m):
    m=str(m)
    if len(m)%2==0:
        a=(len(m)/2)-1
        first_bit=""
        b=0
        while b<=a:
            first_bit=first_bit+m[b]
            b+=1
        c=len(m)-1
        second_bit=""
        d=len(m)/2
        while c>=d:
            second_bit=second_bit+m[c]
            c-=1
        if first_bit==second_bit:
            return 1
        else:
            return 0
    elif (len(m)+1)%2==0:
        a=((len(m)-1)/2)-1
        first_bit=""
        b=0
        while b<=a:
            first_bit=first_bit+m[b]
            b+=1
        c=len(m)-1
        second_bit=""
        d=(len(m)+1)/2
        while c>=d:
            second_bit=second_bit+m[c]
            c-=1
        if first_bit==second_bit:
            return 1
        else:
            return 0

num=int(input())
initial=num
count=0
x=palindrome(num)
if x==1:
    print(str(num)+" is already a palindrome number")
else:
    x=0
    while count<=1000 and x!=1:
        temp=int(flip(num))
        num=num+temp
        x=palindrome(num)
        count+=1
    if x==1:
        print("The number "+str(initial)+" ends up as the palindrome number "+str(num)+" under the 196-algorithm")
        print("The algorithm was applied "+str(count)+" times")
    elif x==0:
        print("The number of times the 196-algorithm was applied exceeded 1000")
