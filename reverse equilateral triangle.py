"""this code prints the below pattern
if x = 5 the pattern is:-
 * * * * * 
  * * * *
   * * *
    * *
     *
"""
#the code is:-

x = int(input("Enter: "))
for i in range(x):
    print(" "*i,end=" ")
    print("* "*(x-i))
