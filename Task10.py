#Area of rectangle using class named rectangle 
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

a=int(input("Enter length of rectangle: "))
b=int(input("Enter width of rectangle: "))
obj=Rectangle(a,b)
print("Area of rectangle:",obj.rectangle_area())
 
