people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 22},
    {'name': 'Peter', 'age': 30},
    {'name': 'Jenifer', 'age': 28}
]

name = input('Enter a name:: ')

found = False
for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break

if not found:
    print(f'{name} is not found!')

name = input('Enter a name:: ')

for person in people:
    if person['name'] == name:
        print(person)
        break
else:
    print(f'{name} is not found!')
