expression = input("Enter an expression: ")

#Take numbers from input, turn into floats and store into variables as constituents
x, y, z = expression.split()
a = float(x)
b = float(z)

#I tried error handling, but does not work the way I intended. I looked up try/except statement, but did not implement it; we haven't covered that yet, and don't want to jump ahead.
if "/" in expression and b == 0:
    print("Cant divide by zero.")

#Take operators from input and use accordingly to take a result
if "+" in expression:
    result = a + b
elif "-" in expression:
    result = a - b
elif "*" in expression:
    result = a * b
elif "/" in expression:
    result = a / b
else:
    print("Invalid input.")

print(result)
