
# # # def calculate_area(length,width):
# # #     return length*width

# # # area=calculate_area(10,5)
# # # print(area)


# # #default parameter

# # # def greet(name,language="Python"):
# # #     print(f"{name} is learning {language}")
    
    
# # # greet("Alex")
# # # greet("Ani","JavaScript")



# # def add_numbers(*numbers):
# #     total=0  
# #     for number in numbers:
# #         total+=number
        
# #     return total


# # print(add_numbers(1,2,3,4,5))



# # def show_info(**info):
# #     for key, value in info.items():
# #         print(key, value)
# # show_info(name="Alex", age=20, course="Python")



# def student_info(name,age=18):
#     return f"{name} is {age} years old."

# print(student_info("Alex", 20))
# print(student_info("Ani"))

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number       
#     return total

# print(multiply(2, 3))
# print(multiply(2, 3, 4))


def show_student(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_student(name="Alex", age=20, course="Python")
