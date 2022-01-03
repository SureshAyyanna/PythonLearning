def reverse(string):
    reversed_string=""

    for i in string:
        reversed_string = i+ reversed_string
    print("Reveresed String is :", reversed_string)

string = input("Enter a string:")
print("Entered string is :",string)
reverse(string)
