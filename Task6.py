#Program to check a triangle is equilateral, isocelus or scalene
print("Input lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("Equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")
elif a!=b and b!=c and c!=a:
	print("Scalene triangle")
