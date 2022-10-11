"""this code prints the below pattern
if n = 5 the pattern is:-
* * * * * 
* * * *
* * *
* *
*
"""
#the code is:-


n = int(input("Enter: "))
for i in range(n):
    if i<=n:
        print("* "*(n-i))
    
