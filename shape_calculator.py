class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return (self.area)

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return (self.perimeter)

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return (self.diagonal)

    def get_picture(self):
        self.picture = ("*" * self.width + "\n") * self.height
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return self.picture

    def get_amount_inside(self, x):
        self.amount = (self.width * self.height) / (x.width * x.height)
        self.amount = int(self.amount)
        return self.amount

class Square(Rectangle):

    def __init__(self, sidelength):
        self.width = sidelength
        self.height = sidelength

    def __str__(self):
        return f"Square(width={self.width}, height={self.height})"

    def set_side(self, newside):
        self.width = newside
        self.height = newside

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height
