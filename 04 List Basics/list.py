# #list 
# #a collection of values

# # fruits=["apple","banana","mango"]

# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])

# # fruits.append("orange")
# # print(fruits)

# # # fruits.remove("banana")
# # fruits.pop(0)
# # print(fruits)


# foods=["rice","egg","burger","pizza","milk"]

# foods[1]="chicken"
# foods[2]="momo"

# # print(foods)
# # print(foods[0])
# # foods.append("fruits")
# # foods.pop(2)
# # print(foods)
# # print(len(foods))

# # for food in foods:
# #     print(f"I like {food}")


# #without enumerate()
# # for i in range(len(foods)):
# #     print(i,foods[i])             

# # with enumerate
# for i,food in enumerate(foods):
#     print(f"{i+1}. I like {food}")


shopping_list=["rice","milk","eggs"]

print("Shopping List:")
for i,item in enumerate(shopping_list):
    print(f"{i+1}. {item}")
    

shopping_list.append("bread")
shopping_list.remove("milk")

print("After changes:")
for i,item in enumerate(shopping_list):
    print(f"{i+1}. {item}")
    
    
print(f"Total items: {len(shopping_list)}")