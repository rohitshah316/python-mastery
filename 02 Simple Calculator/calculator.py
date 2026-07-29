num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

print(f"First number:{num1}")
print(f"Second number:{num2}")

print(f"Addition:{num1+num2}")
print(f"Difference:{num1-num2}")
print(f"Multiplication:{num1*num2}")

div_res=num1/num2 if num2!=0 else "error"
print(f"Division:{div_res}")