"""this code prints the below pattern
if n = 4 the pattern is:-
* * * *
* * * *
* * * *
* * * *
"""
#the code is:-

n = int(input("Enter the number of rows you want: "))
for i in range(1,n+1):
    if i<=n:
        print("* "*n)
