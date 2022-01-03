# Program to find Factorial of a number

num = int(input("Enter a number:"))
fact = 1

if num<0 :
    print("Factorial number doesn't exist for negative numbers")
elif num==0 :
    print("Factorial of 0 is 1")
else :
    for i in range (1,num+1):
      fact = fact * i
    print("Factorial of {} is : {}".format(num, fact))
"""
#Using Ternary approach
num =5

return 1 if (n==0 or n==1) else n*fact(n-1)
"""
""""
def factorial(n)
    if (num == 0 or num ==1) :
        return 1
    else:
        return n * fact(n-1)
"""

