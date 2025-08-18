client_name = input('Enter Your name:')

if any(char.isdigit() for char in client_name):
    print('Name should not contain numbers.')
else:
    print(client_name)