client_name = input("Enter the client name: ")
phone_number = input("Enter the phone number: ")
email = input("Enter the email address: ")

#security checks for the Client field
if any(char.isdigit() for char in client_name):
    print("Error: Client name should not contain numbers.")
else:
    print("Client name is valid.")
    
# security checks for the Phone Number field
if phone_number.isdigit() and len(phone_number) == 10:
    print("Phone number is accepted:",phone_number)
else:
    print("Error: Phone number must be 10 digits long and contain only numbers.")     
    
# security checks for the Email field
if '@gmail.com' in email or '@yahoo.com' in email:
    print("Email is accepted:", email)
else:
    print("Error: Email must be a Gmail or Yahoo address.")


    