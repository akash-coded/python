def count_down(start):
    print(start)


for index in range(3, -1, -1):
    print(index)

print()


def tail_recursive_count_down(start):
    print(start)
    next_val = start - 1
    if next_val > -1:
        tail_recursive_count_down(next_val)


tail_recursive_count_down(3)
print()


def head_recursive_count_down(start):
    next_val = start - 1
    if next_val > -1:
        head_recursive_count_down(next_val)
    print(start)


head_recursive_count_down(3)
