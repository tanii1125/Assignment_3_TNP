students = {}
current_user = None

def register():
    print("\n--- Student Registration ---")
    username = input("Enter username: ")
    if username in students:
        print("Username already exists")
        return
    password = input("Enter password: ")
    name = input("Full Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    course = input("Course: ")
    year = input("Year: ")
    roll_no = input("Roll Number: ")
    students[username] = {
        "username": username,
        "password": password,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year,
        "roll_no": roll_no
    }
    print("Registration successful")

def login():
    global current_user
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in students and students[username]["password"] == password:
        current_user = username
        print("Login successful")
    else:
        print("Invalid username or password")

def show_profile():
    if not current_user:
        print("Login required")
        return
    print("\n--- Profile ---")
    for key, value in students[current_user].items():
        if key != "password":
            print(f"{key}: {value}")

def update_profile():
    if not current_user:
        print("Login required")
        return
    print("\n--- Update Profile ---")
    profile = students[current_user]
    for key in profile:
        if key != "username" and key != "password":
            new_value = input(f"Enter new {key} (leave blank to keep same): ")
            if new_value != "":
                profile[key] = new_value
    print("Profile updated")

def logout():
    global current_user
    current_user = None
    print("Logged out")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            logout()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
