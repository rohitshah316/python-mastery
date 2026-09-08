# # name="Alex"
# # print(name.upper())
# # print(name.lower())
# # print(name.strip())


# # text="This is simple text"
# # print(text.upper())
# # print(text.lower())
# # print(text.strip())   #remove unnecessary spaces
# # print(text.replace("simple","hard"))

# # print(text.split())

# text="Python Java C++ JavaScript"

# words=text.split()
# print(words)
# print(words[0])

# print(", ".join(words))

# message=["I","Love","Python"]

# joined=" ".join(message)

# print(joined.lower())


# name="Alex"
# age=20
# level=3
# language="Python"

# # print("My name is", name, "and I am",age,"years old.")
# #f-string way - it helps insert variable into string
# print(f"My name is {name} and I am {age} years old.")

# print(f"{name} is learning {language} at level {level}.")

# print(name[-4])

# text="Python"
# # print(text[0])
# # print(text[2])
# # print(text[-1])
# # print(text[-2])


# print(text[:3])
# print(text[2:])
# print(text[1:4])
# print(text[4:])


text=input("Enter some text: ")

print(text)
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print(text[0])
print(text[-1])
print(text[:3])

splitted=text.split()
print("-".join(splitted))
print(f"Alex said {text}")