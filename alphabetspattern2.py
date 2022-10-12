"""this code prints the below pattern
if n = 5 the pattern is:-
A 

B C

D E F

G H I J

K L M N O
"""
#the code is:-


n = int(input("Enter: "))
sum = 64
for i in range(1,n+1):
    for j in range(i):
        sum = sum+1
        c = chr(sum)
        print(c,end=" ")
    print("\n")
