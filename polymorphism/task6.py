class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h
    def intersection(self, other):
        left = max(self.x, other.x)
        right = min(self.x + self.w, other.x + other.w)
        bottom = max(self.y, other.y)
        top = min(self.y + self.h, other.y + other.h)
        if left < right and bottom < top:
            return Rectangle(left, bottom, right - left, top - bottom)
        else:
            return None
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)
if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
rect4 = Rectangle(0, 0, 10, 10)
rect5 = Rectangle(10, 0, 10, 10)
rect6 = rect4.intersection(rect5)
if rect6 is None:
    print('No intersection')
else:
    print(rect6.get_x(), rect6.get_y(), rect6.get_w(), rect6.get_h())
rect7 = Rectangle(3, 5, 2, 1)
rect8 = Rectangle(1, 2, 10, 10)
rect9 = rect7.intersection(rect8)
if rect9 is None:
    print('No intersection')
else:
    print(rect9.get_x(), rect9.get_y(), rect9.get_w(), rect9.get_h())