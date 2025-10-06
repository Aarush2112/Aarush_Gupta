courses_db = {}
students_db = {}
def add_course(course_id, name, capacity, schedule_time, prerequisites=set()):
    """Add a new course to the course database."""
    courses_db[course_id] = {
        'name': name,
        'capacity': capacity,
        'schedule_time': schedule_time,
        'prerequisites': set(prerequisites),
        'enrolled_students': set(),
        'waitlist': []
    }

def add_student(student_id, name, completed_courses=set()):
    """Add a new student to the student database."""
    students_db[student_id] = {
        'name': name,
        'completed_courses': set(completed_courses),
        'current_schedule': set()
    }

def has_prerequisites(student_id, course_id):
    """Check if a student meets the course prerequisites."""
    student = students_db[student_id]
    course = courses_db[course_id]
    return course['prerequisites'].issubset(student['completed_courses'])
