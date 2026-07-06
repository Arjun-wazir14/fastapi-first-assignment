from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{
        "message" : "Welcome to my first FastAPI assignment"
    }

@app.get("/about")
def about():
    return{
        "student_name": "Your Name",
        "course": "FastAPI",
        "topic": "First API Assignment",
        "status": "Learning"
    }    


@app.get("/trainer")
def trainer():
    return{
       "name": "Hemanth",
       "role": "Trainer",
       "subject": "FastAPI"
    }
 

@app.get("/courses")
def courses():
    return[
 {
 "id": 1,
 "name": "Python Basics",
 "duration": "1 week"
 },
 {
 "id": 2,
 "name": "FastAPI",
 "duration": "2 weeks"
 },
 {
 "id": 3,
 "name": "SQL Basics",
 "duration": "1 week"
 }
    ]

@app.get("/students")
def students():
    return[
 {
 "id": 1,
 "name": "Arjun",
 "course": "Python",
 "city": "Jammu"
 },
 {
 "id": 2,
 "name": "Ajanya",
 "course": "FastAPI",
 "city": "Jammu"
 }
]
@app.get("/college")
def college():
    return{
        "MIET JAMMU"
        "location": "Jammu",
        "department": "Computer Science",
        "current_module": "FastAPI Basics"

    }

@app.get("/technologies")
def technologies():
    return[
 "Python",
 "FastAPI",
 "JSON",
 "HTTP",
 "REST API"
    ]


@app.get('/students/{student_id}')
def get_student_by_id(student_id : int):
    return{
        "student_id" : student_id,
        "message"   :  "learning Dynamic URL's"
    }

@app.get('/students/{course_id}')
def get_course_by_id(course_id : str):
    return{
        "course_id" : course_id,
        "message"   :  "learning Dynamic URL's"
    }    

@app.get('/books/{book_id}/author/{author_id}')
def get_book_by_id(book_id : str,author_id :str):
    return{
        "book_id" : book_id,
        "name" : "how to get fit in 100 days",
        "author_id" : author_id,
        "author" : "Ajanya "

    }    

@app.get('/students/{student_id}/courses/{course_name}')
def get_student_by_id(student_id : int,course_id :str):
    return{
        "student_id" : student_id,
        "name" : "Arjun",
        "course_id" : course_id,
        "course" : "web Dev"

    }
        