


# # file=open("notes.txt","w")

# # file.write("Python")
# # file.close()


# #better approach: with
# with open("notes.txt","w") as file:
#     file.write("I am learning Python.\nPython is awesome!")
    
# # "w" → write (creates/overwrites)
# # "a" → append
# # "r" → read

# with open("notes.txt", "a") as file:
#     file.write("\nI am getting better at Python.")


# with open("notes.txt","r") as file:
#     content=file.readlines()
    
# print(content)

note=input("Enter a note: ")

with open("notes.txt","a") as file:
    file.write(f"\n{note}")
    
    
with open("notes.txt","r") as file:
    content=file.read()
    
print(content)