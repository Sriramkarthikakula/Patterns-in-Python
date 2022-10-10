"""this code prints the below pattern
if x = 5 the pattern is:-
 * * * * * 
  * * * *
   * * *
    * *
     *
     *
    * *
   * * *
  * * * *
 * * * * *
"""
#the code is:-

x = int(input("Enter: "))
for i in range(x):
    print(" "*i,end=" ")
    print("* "*(x-i))
for i in range(1,x+1):
    if i<=x:
        print(" "*(x-i),end=" ")
        print("* "*i)
