

students = {
    "student1": {
        "name": "Alex",
        "age": 20,
        "course": "Python"
    },
    "student2": {
        "name": "Ani",
        "age": 19,
        "course": "JavaScript"
    }
}

print(students.get("student1").get("name"))
print(students.get("student2").get("course"))

students["student1"]["level"]=3

for key,value in students.get("student1").items():
    print(key,value)
    


print(students.get("student3","Student not found"))

# print(student["student2"]["course"])
# for key,value in student.items():
#     print(key,value)