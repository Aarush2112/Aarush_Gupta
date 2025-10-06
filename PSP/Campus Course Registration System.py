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
        # main_menu()
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




'''
def add_course(course_id, name, capacity, schedule_time, prerequisites=set()):
    """Add a new course to the course database."""
    courses[course_id] = {
        'name': name,
        'capacity': capacity,
        'schedule_time': schedule_time,
        'prerequisites': set(prerequisites),
        'enrolled_students': set(),
        'waitlist': []
    }

def add_student(student_id, name, completed_courses=set()):
    """Add a new student to the student database."""
    students[student_id] = {
        'name': name,
        'completed_courses': set(completed_courses),
        'current_schedule': set()
    }

def has_prerequisites(student_id, course_id):
    """Check if a student meets the course prerequisites."""
    student = students[student_id]
    course = courses[course_id]
    return course['prerequisites'].issubset(student['completed_courses'])

def time_conflict(student_id, course_id):
    """Check for time conflict between existing and new course."""
    new_time = courses[course_id]['schedule_time']
    for c_id in students[student_id]['current_schedule']:
        if courses[c_id]['schedule_time'] == new_time:
            return True
    return False
'''

if __name__ == "__main__":
    login()