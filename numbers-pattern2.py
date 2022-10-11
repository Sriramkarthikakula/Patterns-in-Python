"""this code prints the below pattern
if x = 5 the pattern is:-
1 

2 3

4 5 6

7 8 9 10

11 12 13 14 15   
"""
#the code is:-


x = int(input("Enter the number: "))
sum = 0
for i in range(1,x+1):
  for j in range(i):
    sum = sum+1
    print(sum,end=" ")
  print("\n")
