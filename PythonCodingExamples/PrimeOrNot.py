# Verify the given number is Prime or not
"""
1) It should be a whole number greater than 1.
2) it should have only two factors i.e one and the number itself.
"""
num = int(input("Enter a number: "))
count = 0

if num > 1:
    for i in range(1, num+1):
        if(num % i) == 0 :
            count = count + 1
    if count == 2:
        print("The given number is prime number")
    else:
        print("The given number is not a prime number")