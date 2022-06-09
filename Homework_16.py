class Triangle:

    def __init__(self, a, b, c):
        self.side_1 = a
        self.side_2 = b
        self.side_3 = c


class TTriangle(Triangle):

    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    @staticmethod
    def triangle_area(self, a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def triangle_perimeter(self, a, b, c):
        return a + b + c
    @staticmethod
    def validation(self, a, b, c):
        v_validation = (a + b <= c) or (a + c <= b) or (b + c <= a):

        if self.v_validation:
            return True
        else:
            return False


new_triangle = TTriangle(3, 4, 5)
print("area : {}".format(new_triangle.triangle_area(0, 3, 4, 5)))
print("area : {}".format(new_triangle.triangle_perimeter(0, 3, 4, 5)))
print("area : {}".format(new_triangle.validation(0, 3, 4, 5)))