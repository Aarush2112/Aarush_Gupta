# Creating dictionary for all the courses
courses_db = {}
students_db = {}
def add_courses(courses_id, name, capacity, time, prerequisites=set()):
    courses_db[courses_id] = {
        'name' : name,
        'capacity' : capacity,
        'time' : time,
        'prerequisites' : set(prerequisites),
        'enrolled' : set(),
        'waitlist' : []
    }

def add_students(students_id, name, completed_course=set()):
    students_db[students_id] = {
        'name' : name,
        'completed_course' : set(completed_course),
        'current_schedule' : set(),
    }

