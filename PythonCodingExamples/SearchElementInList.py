mylist =[1,2,3,4,5]
len =len(mylist)
flag =0
ele = input("Enter the element to be search:")

for i in mylist:
    if (i == ele):
        print("Element found")
        flag=1
        break

if(flag==0):
        print("Element not found")