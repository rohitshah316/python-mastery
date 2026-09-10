import json

# student = {
#     "name": "Alex",
#     "age": 20,
#     "course": "Python"
# }

# data=json.dumps(student)
# print(data)


data = '{"name": "Alex", "age": 20}'

student=json.loads(data)

print(student)
print(student["name"])