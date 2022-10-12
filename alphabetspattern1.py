"""this code prints the below pattern
if n = 5 the pattern is:-
A 

A B 

A B C 

A B C D

A B C D E
"""
#the code is:-


n = int(input("Enter: "))
for i in range(1,n+1):
    for j in range(i):
        sum = 65+j
        c = chr(sum)
        print(c,end=" ")
    print("\n")
