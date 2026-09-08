# LIST   → ordered, changeable, duplicates allowed

# TUPLE  → ordered, NOT changeable, duplicates allowed

# SET    → unique values, changeable, no duplicate values


# numbers=(10,20,30)
# print(numbers)
# print(numbers[0])
# numbers[0]=10 throws error cause tuples are immutable


#set
# numbers={10,20,20,30,30,30}
# print(numbers)

# numbers.add(40)
# numbers.add(30)
# numbers.discard(20)
# print(numbers)



languages={"Python","Java","Python","C++","Java"}

print(languages)
languages.add("JavaScript")
languages.discard("Java")
print(languages)