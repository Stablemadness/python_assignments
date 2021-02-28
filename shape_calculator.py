#import math

class Rectangle:

    def __str__(self):
        return 'Rectangle(width=%s, height=%s)' % (self.width, self.height)

#     : Expected string representation of rectangle to be "Rectangle(width=3, height=6)"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        diag = self.width**2 + self.height**2
        return diag**.5

    def get_perimeter(self):
        return self.width*2 + self.height*2

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ""
        for i in range(self.height):
            picture += "*"*self.width + "\n"
        return picture.rstrip()

    def get_amount_inside(self, inside):
#        counter = 0
#        h = self.height / inside.height
#        w = self.width / inside.width
#        print(h, w)
#        return int(h * w)
        return int((self.height / inside.height) * (self.width / inside.width))



class Square(Rectangle):

    def __str__(self):
        return 'Square(side=%s)' % self.width

    def __init__(self, side):
#        self.name = ""
        self.width = side
        self.height = side

    def set_side(self, new_side):
        self.set_width(new_side)
        self.set_height(new_side)

r = Rectangle(10, 5)
print(r.get_perimeter())
print(r.get_picture())
print(r.get_area())
r.set_height(3)
print(r.get_perimeter())

rect = Rectangle(4,4)
sq = Square(4)
print(rect.get_diagonal())
print(sq.get_diagonal())
print(sq.get_picture())
r2 = Rectangle(1,1)
r2.set_width(8)
r2.set_height(16)
print(r2.get_amount_inside(sq))
print(sq)
print(r2)
print(r)
