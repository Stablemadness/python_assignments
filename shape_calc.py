class Rectangle:

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
        picture = ""
        for i in range(self.height):
            picture += "*"*self.width + "\n"
        return picture.rstrip()

    def get_amount_inside(self, inside):
        return int((self.height / inside.height) * (self.width / inside.width))


class Square(Rectangle):
    def __str__(self):
        return 'Square(side=%s)' % self.width

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, new_side):
        self.set_width(new_side)
        self.set_height(new_side)
