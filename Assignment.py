class Shape:
    def what_am_i(self):
        print(f"I am a shape.")

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.length*2 + self.width*2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    
    def calculate_perimeter(self):
        return self.s1*4

rect1 = Rectangle(5,8)
r_perimeter = rect1.calculate_perimeter()
print(rect1.width)
print(rect1.length)
print(r_perimeter)
rect1.what_am_i()

square1 = Square(5)
s_perimeter = square1.calculate_perimeter()
print(square1.s1)
print(s_perimeter)
square1.what_am_i()