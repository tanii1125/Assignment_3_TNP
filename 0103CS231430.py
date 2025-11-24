import json, random, datetime, os

STUDENT_FILE = "students.json"
SCORE_FILE = "scores.json"

# ------------------ Helper Functions ------------------
def load_data(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Student Registration ------------------
def register():
    students = load_data(STUDENT_FILE)
    username = input("Enter username: ")
    for s in students:
        if s["username"] == username:
            print("Username already exists!")
            return
    student = {
        "username": username,
        "password": input("Enter password: "),
        "name": input("Enter name: "),
        "email": input("Enter email: "),
        "branch": input("Enter branch: "),
        "year": input("Enter year: "),
        "contact": input("Enter contact number: "),
        "enrollment": input("Enter enrollment number: "),
        "dob": input("Enter date of birth: "),
        "address": input("Enter address: "),
        "gender": input("Enter gender: ")
    }
    students.append(student)
    save_data(STUDENT_FILE, students)
    print("Registration successful!\n")

# ------------------ Login ------------------
def login():
    students = load_data(STUDENT_FILE)
    username = input("Enter username: ")
    password = input("Enter password: ")
    for s in students:
        if s["username"] == username and s["password"] == password:
            print(f"Welcome, {s['name']}!\n")
            student_menu(s)
            return
    print("Invalid credentials!\n")

# ------------------ Update Profile ------------------
def update_profile(student):
    print("\nUpdate Profile:")
    for key in ["name", "email", "branch", "year", "contact", "address"]:
        val = input(f"Enter new {key} (leave blank to keep same): ")
        if val:
            student[key] = val
    students = load_data(STUDENT_FILE)
    for i, s in enumerate(students):
        if s["username"] == student["username"]:
            students[i] = student
            break
    save_data(STUDENT_FILE, students)
    print("Profile updated!\n")

# ------------------ Show Profile ------------------
def show_profile(student):
    print("\n--- Profile ---")
    for k, v in student.items():
        if k != "password":
            print(f"{k.capitalize()}: {v}")
    print()

# ------------------ Quiz Section ------------------
QUIZZES = {
    "DSA": [
        ("Which data structure uses LIFO?", ["Queue", "Stack", "Array", "Tree"], "Stack"),
        ("Which of these is not linear?", ["Array", "List", "Tree", "Stack"], "Tree"),
        ("What is complexity of binary search?", ["O(n)", "O(n^2)", "O(log n)", "O(1)"], "O(log n)"),
        ("Queue works on?", ["FIFO", "LIFO", "LILO", "None"], "FIFO"),
        ("Which DS is used in recursion?", ["Queue", "Stack", "Tree", "Graph"], "Stack")
    ],
    "DBMS": [
        ("Which is not a DBMS?", ["MySQL", "Oracle", "Python", "PostgreSQL"], "Python"),
        ("SQL stands for?", ["Structured Query Language", "Simple Query Language", "None", "Sequential Query Logic"], "Structured Query Language"),
        ("Which key uniquely identifies a record?", ["Foreign key", "Primary key", "Candidate key", "Super key"], "Primary key"),
        ("Normalization removes?", ["Redundancy", "Dependency", "Integrity", "Security"], "Redundancy"),
        ("Which command is used to remove a table?", ["DELETE", "REMOVE", "DROP", "CLEAR"], "DROP")
    ],
    "PYTHON": [
        ("Which is immutable?", ["List", "Dict", "Set", "Tuple"], "Tuple"),
        ("PEP stands for?", ["Python Enhancement Proposal", "Program Enhancement Process", "None", "Performance Execution Plan"], "Python Enhancement Proposal"),
        ("Which creates a generator?", ["[]", "()", "{}", "None"], "()"),
        ("What is used to define function?", ["fun", "define", "def", "func"], "def"),
        ("Which library is used for data?", ["pandas", "math", "sys", "os"], "pandas")
    ]
}

def attempt_quiz(student):
    category = input("Enter category (DSA/DBMS/PYTHON): ").upper()
    if category not in QUIZZES:
        print("Invalid category!\n")
        return
    questions = random.sample(QUIZZES[category], len(QUIZZES[category]))
    score = 0
    for q, opts, ans in questions:
        print("\nQ:", q)
        for i, o in enumerate(opts, 1):
            print(f"{i}. {o}")
        try:
            choice = int(input("Enter choice (1-4): "))
            if opts[choice - 1] == ans:
                score += 1
        except:
            print("Invalid input! Skipped.")
    total = len(questions)
    print(f"\nYou scored {score}/{total}\n")

    scores = load_data(SCORE_FILE)
    scores.append({
        "enrollment": student["enrollment"],
        "category": category,
        "marks": f"{score}/{total}",
        "datetime": str(datetime.datetime.now())
    })
    save_data(SCORE_FILE, scores)

# ------------------ View Scores ------------------
def view_scores(student):
    scores = load_data(SCORE_FILE)
    print("\n--- Your Quiz History ---")
    for s in scores:
        if s["enrollment"] == student["enrollment"]:
            print(f"{s['category']} | {s['marks']} | {s['datetime']}")
    print()

# ------------------ Student Menu ------------------
def student_menu(student):
    while True:
        print("1. Show Profile\n2. Update Profile\n3. Attempt Quiz\n4. View Scores\n5. Logout")
        ch = input("Enter choice: ")
        if ch == "1":
            show_profile(student)
        elif ch == "2":
            update_profile(student)
        elif ch == "3":
            attempt_quiz(student)
        elif ch == "4":
            view_scores(student)
        elif ch == "5":
            print("Logged out!\n")
            break
        else:
            print("Invalid choice!\n")

# ------------------ Main Menu ------------------
def main():
    while True:
        print("1. Register\n2. Login\n3. Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            register()
        elif ch == "2":
            login()
        elif ch == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
