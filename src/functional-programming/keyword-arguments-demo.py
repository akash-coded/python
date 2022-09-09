def get_net_price(price, discount):
    return price * (1 - discount)

net_price = get_net_price(100, 0.1)
print(net_price, end="\n\n")

net_price = get_net_price(0.1, 100)
print(net_price, end="\n\n")

net_price = get_net_price(discount=0.1, price=100)
print(net_price, end="\n\n")
