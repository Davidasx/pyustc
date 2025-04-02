from pyustc import EduSystem

es = EduSystem(...) # See examples/edu_system.py for how to create a EduSystem instance

# Get current teaching week
week = es.get_current_teach_week()

# Get the course table
table = es.get_course_table(
    week=week,
    semester="now"
)
print(
    table.std_name,
    table.std_id,
    table.grade,
    table.major,
    table.admin_class,
    table.credits,
    table.week
)

# Get all courses
courses = table.courses
filtered_courses = table.get_courses(
    weekday=1,
    unit=3,
    place="5201"
)

# Print course information
course = courses[0]
print(
    course.code,
    course.name,
    course.place, # Place object, use `include` method to check if it contains a string
    course.weekday,
    course.teachers, # List of Teacher objects
    course.student_count,
    course.start_time,
    course.end_time,
    course.unit
)
time = course.time(format=True), # a string if `format` is True, otherwise a tuple of time objects
