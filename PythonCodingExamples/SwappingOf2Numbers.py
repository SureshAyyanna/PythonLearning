# Using Temp variable
num1 = input("Enter the num1:")
num2 = input("Enter the num2:")

print("Before Swapping: Value of num1 ={} , Value of num2 = {}". format(num1, num2))

# Using Temp variable
temp = num1
num1 = num2
num2 = temp

"""
# Without using temp variable
num1, num2 = num2, num1
"""

""""
# Method 03
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
"""

""""
# Method 04
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2
"""

print("After Swapping: Value of num1 ={} , Value of num2 = {}". format(num1, num2))
