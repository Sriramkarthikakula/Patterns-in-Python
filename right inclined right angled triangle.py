"""this code prints the below pattern
if n = 5 the pattern is:-
      *
     **
    ***
   ****
  *****
"""
#the code is:-

x = int(input("enter: "))
for i in range(1,x+1):
    print(" "*(x-i),end=" ")
    print("*"*i)
