def get_fullname(first_name, last_name):
    return f"{first_name} {last_name}"


def get_fullname_lambda():
    return lambda first_name, last_name: f"{first_name} {last_name}"


get_name = get_fullname_lambda()
name = get_name("Akash", "Das")
print(name, end="\n\n")


def times(n):
    return lambda x: x * n


double = times(2)
print(double)
print(double(7))
print()

triple = times(3)
print(triple(3))
print(triple(7))
