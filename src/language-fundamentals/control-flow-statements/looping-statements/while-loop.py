max = 5
counter = 0
while counter < max:
    print(counter)
    counter += 1


command = ""
while command.lower().strip() != "quit":
    command = input("> ")
    print(f"Echo: {command}")
