"""this code prints the below pattern
if x = 5 the pattern is:-
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
#the code is:-


x = int(input("Enter: "))
for i in range(1,2*x):
    if i<=x:
        print("* "*i)
    if i>x:
        print("* "*((2*x)-i))
