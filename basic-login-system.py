
users = {
    "parrot": "pa25",
    "nazeer": "9010",
    "nagahayes": "13456",
    "vijay": "kittaya",
    "munna": "98480",
    "nagaraju": "08489",
    "sameer": "nagaveni",
    "shaik": "hayes",
    "rabbit": "naz45"
}

print("=== Basic Login System ===")
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("\nLogin Successful! Welcome,", username)
else:
    print("\nLogin Failed! Invalid username or password.")
