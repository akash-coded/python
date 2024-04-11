fruits = ["apple", "banana", "orange", "mango", "watermelon"]
newlist = []

for x in fruits:
    if "o" in x:
        newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "o" in x]
print(newlist)
