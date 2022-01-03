"""
Input:[1,2,3]
output:[3,2,1]
"""

mylist = [1, 3, 5, 7, 9, 13]
len= len(mylist)

print("Before swapping:", mylist)
temp = mylist[0]

mylist[0] = mylist[len-1]
mylist[len-1] = temp

print("After swapping:", mylist)