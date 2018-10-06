#you must enter 3 inputs everytime you run this program: dealer's total, your total, your action

d=int(input())
#first input: enter dealer's total
#when you run this code for the first time, enter "0" as input

i=int(input())
#second input: enter your total
#when you run this code for the first time, enter "0" as input

n=str(input())
#third input: enter your action
#there are 3 possible actions: "deal", "hit", "stand"
#enter "deal" to start a new game
#from the second time onwards you may "hit" if you want another card, or "stand" if you don't want any more cards

cards=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
import random

if n=="deal":
 D=random.choice(cards)
 if str(D)==str("A"):
  d=11
 elif str(D)==str("J"):
  d=10
 elif str(D)==str("Q"):
  d=10
 elif str(D)==str("K"):
  d=10
 else:
  d=int(D)
 print("Dealer gets a/an "+str(D))
 print("Dealer has a total of "+str(d))
 P=random.choice(cards)
 if str(P)==str("A"):
  p=11
 elif str(P)==str("J"):
  p=10
 elif str(P)==str("Q"):
  p=10
 elif str(P)==str("K"):
  p=10
 else:
  p=int(P)
 U=random.choice(cards)
 if str(U)==str("A"):
  u=11
 elif str(U)==str("J"):
  u=10
 elif str(U)==str("Q"):
  u=10
 elif str(U)==str("K"):
  u=10
 else:
  u=int(U)
 t=i+p+u
 print("You recieved a/an "+str(P)+" and a/an "+str(U))
 if t==21:
  print("You have a total of "+str(i+p+u))
  print("You win!")
 if t>21:
  if p==11 and u==11:
   p=1
   print("You have a total of "+str(i+p+u))
   if i+p==21:
    print("You win!")
   else:
    print("Hit or Stand?")
   t=i+p+u
 elif t<21:
  print("You have a total of "+str(t))
  print("Hit or Stand?")
   
if n=="hit":
 print("Dealer has a total of "+str(d))
 P=random.choice(cards)
 if str(P)==str("A"):
  p=11
 elif str(P)==str("J"):
  p=10
 elif str(P)==str("Q"):
  p=10
 elif str(P)==str("K"):
  p=10
 else:
  p=int(P)
 t=i+p
 print("You recieved a/an "+str(P))
 if t>21:
  if p==11:
   p=1
   print("You have a total of "+str(i+p))
   if i+p==21:
    print("You win!")
   else:
    print("Hit or Stand?")
  else:
   print("You have a total of "+str(t))
   print("You are bust")
   print("You lose!")
 elif t<21:
  print("You have a total of "+str(t))
  print("Hit or Stand?")
 elif t==21:
  print("You have a total of "+str(t))
  print("You win!")

if n=="stand":
 print("You have a total of "+str(i))
 print("Dealer has "+str(d))
 if d>i:
  print("You lose!")
 elif d<=i:
  while d<=i:
   S=random.choice(cards)
   if str(S)==str("A"):
    s=11
   elif str(S)==str("J"):
    s=10
   elif str(S)==str("Q"):
    s=10
   elif str(S)==str("K"):
    s=10
   else:
    s=int(S)
   print("Dealer gets a/an "+str(S))
   if d+s==21:
    print("Dealer has "+str(d+s))
    print("You lose!")
    break
   elif d+s>i and d+s<21:
    print("Dealer has "+str(d+s))
    print("You lose!")
    break
   elif d+s>21 and s==11:
    s=1
    print("Dealer has "+str(d+s))
    if d+s==21 or d+s>i:
     print("You lose!")
     break
    elif d+s<i:
     d=d+s
     continue
   elif d+s>21 and s!=11:
    print("Dealer has "+str(d+s))
    print("Dealer is bust")
    print("You win!")
    break
   elif d+s<i or d+s==i:
    print("Dealer has "+str(d+s))
    d=d+s
    continue
