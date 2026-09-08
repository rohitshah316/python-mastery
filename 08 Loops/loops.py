

# number=int(input("enter a number: "))

# for i in range(1,11):
#     print(f"{number} x {i} = {number*i}")
    
    
    
# while True:
#     number = int(input("Enter a number: "))

#     if number == 0:
#         print("Goodbye!")
#         break

#     print(f"You entered {number}")



for i in range(1,21):
    if i%2==0:
        continue
    
    if i>=15:
        break
    print(i)