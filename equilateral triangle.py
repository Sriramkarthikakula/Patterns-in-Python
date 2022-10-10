"""this code prints the below pattern
if n = 5 the pattern is:-
     * 
    * *
   * * *
  * * * *
 * * * * *
"""
#the code is:-

n = int(input("enter: "))
for i in range(1,n+1):
    if i<=n:
        print(" "*(n-i),end=" ")
        print("* "*i)
