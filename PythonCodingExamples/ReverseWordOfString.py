str= "Welcome to python programming"

words=str.split(" ")

print(words)
print(words[::-1])

res = ' '.join(words[::-1])

print(res)