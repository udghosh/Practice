print("Input lengths of the triangle sides: ")
x = int(input("Enter side x: "))
y = int(input("Enter side y: "))
z = int(input("Enter side z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
