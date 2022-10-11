"""this code prints the below pattern
if x = 5 the pattern is:-
1 

1 2

1 2 3

1 2 3 4

1 2 3 4 5
"""
#the code is:-

x = int(input("enter: "))
for i in range(1,x+1):
    for j in range(i):
        sum = j+1
        print(sum,end=" ")
    print("\n")
