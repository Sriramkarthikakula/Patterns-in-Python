"""this code prints the below pattern
if x = 6 the pattern is:-
     * 

    * *

   * * *

  * * * *

 * * * * *

* * * * * *

 * * * * *

  * * * *

   * * *

    * *

     *
"""
#the code is:-

n = int(input("enter: "))
for i in range(1,(2*n)+1):
    if i<=n:
        print(" "*(n-i),end="")
        print("* "*i,end="")
    if i>n:
        print(" "*((n)-((2*n)-i)),end="")
        print("* "*((2*n)-i),end="")
    print("\n")
