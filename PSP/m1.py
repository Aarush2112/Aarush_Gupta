# Creating dictionary for all the courses
courses_db = {
    'MATH101' : {
        'name': 'Matrices',
        'capacity': 60,
        'class_time': [
            ('Monday', '09:00AM', '10:00AM'),
            ('Tuesday', '09:00AM', '10:00AM'),
            ('Wednesday', '09:00AM', '10:00AM'),
            ('Thursday', '09:00AM', '10:00AM'),
            ('Friday', '09:00AM', '10:00AM'),
        ],
        'prerequisites': set(),
        'enrollment': set(),
        'waitlist': []
    },
    'MATH102' : {
        'name': 'Statics',
        'capacity': 60,
        'class_time': [
            ('Monday', '10:00AM', '11:00AM'),
            ('Tuesday', '10:00AM', '11:00AM'),
            ('Wednesday', '10:00AM', '11:00AM'),
            ('Thursday', '10:00AM', '11:00AM'),
            ('Friday', '10:00AM', '11:00AM'),
        ],
        'prerequisites': set(),
        'enrollment': set(),
        'waitlist': []
    },
    'CS101' : {
        'name': 'Introduction to Python',
        'capacity': 60,
        'class_time': [
            ('Monday', '11:00AM', '12:00PM'),
            ('Tuesday', '11:00AM', '12:00PM'),
            ('Wednesday', '11:00AM', '12:00PM'),
            ('Thursday', '11:00AM', '12:00PM'),
            ('Friday', '11:00AM', '12:00PM'),
        ],
        'prerequisites': {'MATH101', 'MATH102'},
        'enrollment': set(),
        'waitlist': []
    },
    'CS102' : {
        'name': 'Algorithms',
        'capacity': 30,
        'class_time': [
            ('Monday', '12:00PM', '01:00PM'),
            ('Tuesday', '12:00PM', '01:00PM'),
            ('Wednesday', '12:00PM', '01:00PM'),
            ('Thursday', '12:00PM', '01:00PM'),
            ('Friday', '12:00PM', '01:00PM'),
        ],
        'prerequisites': {'CS101', 'MATH101', 'MATH102'},
        'enrollment': set(),
        'waitlist': [],
    },
    'CS103' : {
        'name': 'Data Structures',
        'capacity': 30,
        'class_time': [
            ('Monday', '12:00PM', '01:00PM'),
            ('Tuesday', '12:00PM', '01:00PM'),
            ('Wednesday', '12:00PM', '01:00PM'),
            ('Thursday', '12:00PM', '01:00PM'),
            ('Friday', '12:00PM', '01:00PM'),
        ],
        'prerequisites': {'CS101'},
        'enrollment': set(),
        'waitlist': [],
    },
    'DS101' : {
        'name': 'Data Science',
        'capacity': 30,
        'class_time': [
            ('Monday', '02:30PM', '04:00PM'),
            ('Tuesday', '02:30PM', '04:00PM'),
            ('Wednesday', '02:30PM', '04:00PM'),
            ('Thursday', '02:30PM', '04:00PM'),
            ('Friday', '02:30PM', '04:00PM'),
        ],
        'prerequisites': {'CS101', 'MATH102'},
        'enrollment': set(),
        'waitlist': [],
    }
}