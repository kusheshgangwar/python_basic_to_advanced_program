#  Write a Python Program to Check Prime Number.
#  Prime Numbers:
""" A prime number is a whole number that cannot be evenly divided by any other number
 except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
 cannot be divided by any other positive integer except for 1 and their own value."""

num = int(input("Enter a number: "))
 # define a flag variable
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
 # check for factors
 for i in range(2, num):
     if (num % i) == 0:
        flag = True     
        break
 # if factor is found, set flag to True
 # break out of loop
 # check if flag is True
if flag:
   print(f"{num}, is not a prime number")
else:
   print(f"{num}, is a prime number")