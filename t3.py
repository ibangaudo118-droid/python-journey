username = input("Enter username: ")
password = input("Enter password: ")
is_admin = input("Are you an admin? yes/no: ")

if username == "" or password == "":
    print("Username and password required")
elif len(password) < 6:
    print("Password too short")
elif username == "admin" and password == "secret123":
    if is_admin == "yes":
        print("Welcome, administrator")
    else:
        print("Welcome, admin")
else:
    print("Invalid credentials")