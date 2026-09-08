# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# squares=[number*number for number in numbers if number%2==0]

# print(squares)

numbers = [1, 2, 3, 4, 5, 6]

result={number: "even" if number%2==0 else "odd" for number in numbers}
print(result)