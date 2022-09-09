# defining a function
def greet():
    """Display a greeting"""
    print("Hello")


greet()
print()

# parameterised function


def greet_user(name):
    """Display a customised grreting to the user"""
    print(f"Hello, {name}")


greet_user("Akash")
print()


def get_fullname(first_name, last_name):
    return f"{first_name} {last_name}"


name = get_fullname("Akash", "Das")
print(name)
print()

greet_user(get_fullname("Akash", "Das"))
