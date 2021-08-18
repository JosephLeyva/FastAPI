from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#Creating an instance of FastAPI object
app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

#create an endpoint
# an endpoint is an end of a communication channel
# most common endpoints are: GET POST PUT DELETE
# GET: Get (or return) an information
# POST: Create something new (object)
# PUT: Update a data or something
# DELETE: Delete or erase something

          #endpoint
@app.get("/")

def index():
    return {"name": "First Data"}

# cmd: uvicorn myapi:app --reload

# endpoint parameters are used to return a data related to an input of the endpoint
@app.get("/get-student/{student_id}")
#Path Parameters
def get_student(student_id: int = Path(None,description= "The ID of the student you want to view", gt=0,lt=3)):
    return students[student_id]

#Query Parameter
@app.get("/get-by-name/{student_id}") # Combining path and query parameters
def get_student(*,student_id:int,name: Optional[str] = None, test: int): #str = None makes not required
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not Found"}


# Request Body and The Post Method
#information r data pass when creating a new object using the
#POST method
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student
    return students[student_id]

# Put Method
# Put method is used to update something that already exists

@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

#Delete Method

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    del students[student_id]

    return {"Message":"Student deleted succesfully"}