"""
Input : arr[]={1,2,3,4}
output : 10
"""

arr=[1,2,30,4,6]

print(sum(arr))

# To find Max. value in array
n  = len(arr)
max= arr[0]

for i in range (1,n):
    if arr[i]> max:
        max = arr[i]

print("Maximum value in given array is {}".format(max))

# To find Min. value in array
n  = len(arr)
min = arr[0]

for i in range (1,n):
    if arr[i]< min:
        min = arr[i]

print("Maximum value in given array is {}".format(min))