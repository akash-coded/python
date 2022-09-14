basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit = input('Enter a fruit:: ')

index = 0

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item['fruit'] == fruit:
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        break
    index += 1
else:
    qty = int(input(f'Enter the qty for {fruit}: '))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)
