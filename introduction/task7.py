class BoundingRectangle:
    def __init__(self):
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
    def add_point(self, x, y):
        if self.min_x is None:
            self.min_x = self.max_x = x
            self.min_y = self.max_y = y
        else:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)
    def width(self):
        return self.max_x - self.min_x
    def height(self):
        return self.max_y - self.min_y
    def bottom_y(self):
        return self.min_y
    def top_y(self):
        return self.max_y
    def left_x(self):
        return self.min_x
    def right_x(self):
        return self.max_x
rect1 = BoundingRectangle()
rect1.add_point(-1, -2)
rect1.add_point(3, 4)
print(rect1.left_x(), rect1.right_x())
print(rect1.bottom_y(), rect1.top_y())
print(rect1.width(), rect1.height())
print()
rect2 = BoundingRectangle()
rect2.add_point(10, 20)
rect2.add_point(5, 7)
rect2.add_point(6, 3)
print(rect2.left_x(), rect2.right_x())
print(rect2.bottom_y(), rect2.top_y())
print(rect2.width(), rect2.height())
print()
rect3 = BoundingRectangle()
rect3.add_point(-11, -12)
rect3.add_point(13, -14)
rect3.add_point(-15, 10)
print(rect3.left_x(), rect3.right_x())
print(rect3.bottom_y(), rect3.top_y())
print(rect3.width(), rect3.height())
print()
rect3.add_point(-21, -12)
rect3.add_point(13, -14)
rect3.add_point(-15, 36)
print(rect3.width(), rect3.height())
print(rect3.left_x(), rect3.right_x())
print(rect3.bottom_y(), rect3.top_y())
print()
rect3.add_point(-21, 78)
rect3.add_point(13, -14)
rect3.add_point(-55, 36)
print(rect3.bottom_y(), rect.top_y())
print(rect3.width(), rect.height())
print(rect3.left_x(), rect.right_x())