# Name: Aarush Gupta
# Enrollment Number: 2502140001
# Smart Course Registration System (Password Encrypted)

USERNAME = 'admin'
PASSWORD = 'admin123'

# -----------------------------
# Login System
# -----------------------------
def login():
    print('==== CAMPUS COURSE REGISTRATION SYSTEM ====')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == USERNAME and password == PASSWORD:
        print('\nLogin Successful! Welcome, Admin 🙂')
        main_menu()
    else:
        print('Invalid username or password.')

# -----------------------------
# Main Menu
# -----------------------------
courses = {}
students = {}
student_ids = set()
course_codes = set()

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Course Management")
        print("2. Student Management")
        print("3. Registration Management")
        print("4. Reports")
        print("5. Exit")
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            course_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            registration_menu()
        elif choice == '4':
            report_menu()
        elif choice == '5':
            print('Goodbye! 👋')
            break
        else:
            print('Invalid choice!')


# -----------------------------
# Course Management
# -----------------------------
def course_menu():
    while True:
        print("\n==== Course Management ====")
        print("1. Add Course")
        print("2. Modify Course")
        print("3. Delete Course")
        print("4. Back to Main Menu")
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            add_course()
        elif choice == '2':
            modify_course()
        elif choice == '3':
            delete_course()
        elif choice == '4':
            break
        else:
            print('Invalid choice!')

def add_course():
    cid = input('Enter course code: ')  #(cid refers to course id)
    if cid in course_codes:
        print('Course code already exists!')
        return
    name = input('Enter Course Name: ')
    cap = int(input('Enter Course Capacity: ')) #(cap refers to the capacity of students in course)
    prereq = input('Enter Course Prerequisites: ')
    courses[cid] = {'name': name, 'cap': cap, 'prereq': prereq, 'registered': [], 'waitlist': []}
    course_codes.add(cid)
    print(f"Course '{name}' added!")

def modify_course():
    cid = input('Enter course code: ')
    if cid in courses:
        new_cap = int(input('Enter new Capacity: '))
        courses[cid]['capacity'] = new_cap
        print('Course updated!')
    else:
        print('Course not found!')

def delete_course():
    cid = input('Enter course code: ')
    if cid in courses:
        del courses[cid]
        course_codes.remove(cid)
        print('Course DELETED!')
    else:
        print('Course not found!')


# -----------------------------
# Student Management
# -----------------------------
def student_menu():
    while True:
        print("\n==== Student Management ====")
        print("1. Add Student")
        print("2. Modify Student")
        print("3. Delete Student")
        print("4. Back to Main Menu")
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            add_student()
        elif choice == '2':
            modify_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            break
        else:
            print('Invalid choice!')

def add_student():
    sid = input('Enter Student ID: ')  #(sid refers to student id)
    if sid in students:
        print('Student ID already exists!')
        return
    name = input('Enter Student Name: ')
    students[sid] = {'name': name, 'courses': set(), 'completed': set()}
    student_ids.add(sid)
    print(f"Student added!")

def modify_student():
    sid = input('Enter Student ID: ')
    if sid in students:
        new_name = input('Enter new Name: ')
        students[sid]['name'] = new_name
        print('Student Details updated!')
    else:
        print('Student not found!')

def delete_student():
    sid = input('Enter Student ID: ')
    if sid in students:
        del students[sid]
        student_ids.remove(sid)
        print('Student Details DELETED!')
    else:
        print('Student not found!')


# -----------------------------
# Registration Management
# -----------------------------
def registration_menu():
    while True:
        print("\n==== Registration Management ====")
        print("1. Register Student for Course")
        print("2. Drop Course")
        print("3. Back to Main Menu")
        choice = input('Enter your choice (1-3): ')
        if choice == '1':
            register_student()
        elif choice == '2':
            drop_course()
        elif choice == '3':
            break
        else:
            print('Invalid choice!')

def register_student():
    sid = input('Enter Student ID: ')
    cid = input('Enter Course code: ')
    if sid not in students or cid not in courses:
        print('Invalid Student ID or Course Code!')
        return

    course = courses[cid]
    prereq_ok = all(p in students[sid]['completed'] for p in course['prereq'])
    if not prereq_ok:
        print('Student does not meet Prerequisites!')
        return

    if len(course['registered']) < course['capacity']:
        course['registered'].append(sid)
        students[sid]['courses'].add(cid)
        print(f"Student {sid} Registered in {cid}.")
    else:
        course['waitlist'].append(sid)
        print(f"Course full. Student {sid} added to waitlist.")

def drop_course():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course code: ")

    if cid in courses and sid in courses[cid]['registered']:
        courses[cid]['registered'].remove(sid)
        students[sid]['courses'].discard(cid)

        if courses[cid]['waitlist']: # Promote from waitlist if available
            next_sid = courses[cid]['waitlist'].pop(0)
            courses[cid]['registered'].append(next_sid)
            students[next_sid]['courses'].add(cid)
            print(f"{next_sid} moved from waitlist to registered.")
        print("Course dropped successfully.")
    else:
        print("Student not registered in this course.")


if __name__ == "__main__":
    login()