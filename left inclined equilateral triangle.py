"""this code prints the below pattern
if n = 5 the pattern is:-
      *
     **
    ***
   ****
  *****
   ****
    ***
     **
      *
"""
#the code is:-


n = int(input("Enter: "))
for i in range(1,2*n+1):
    if i<=n:
        print(" "*(n-i),end=" ")
        print("*"*i)
    if i>n:
        print(" "*(n-((2*n)-i)),end=" ")
        print("*"*((2*n)-i))
    
