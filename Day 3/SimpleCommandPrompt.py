# Simple command promp using python while loop

command = ''
while command.lower() != 'exit':  # will stop as soon as user type exit in lowercase
    command = input('>')
    print(f"Echo: {command}")
