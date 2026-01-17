# main.py

from operations import add, subtract, multiply, divide, power, modulo

print("Simple Calculator")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Power:", power(a, b))
print("modulo division:", modulo(a, b))
