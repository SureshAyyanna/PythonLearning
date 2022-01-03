mylist= [1, 3, 4, 2, 1, 4, 1, 4, 2, 3, 5, 4, 1, 2, 4, 2, 3, 4, 5, 2]

count =0
x= 2

for ele in mylist:
    if (ele == x):
        count = count + 1

print("The given number occured {} times".format(count))