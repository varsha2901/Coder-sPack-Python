#To find the median of three values
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b or a > c:
    if a < c or a > c:
        median = a
    elif b > c or b < c:
        median = b
    else:
        median = c

print("The median is", median)
