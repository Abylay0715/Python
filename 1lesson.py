class Vector:
    min = 0
    max = 100
    @classmethod
    def validate(cls, arg):
        return cls.min <= arg <= cls.max
    def __init__(self, x , y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
    def get_coord(self):
        return self.x , self.y
    @staticmethod
    def norm(x , y):
        return x**x + y**y
# v = Vector(1, 200)
# res = Vector.get_coord(v)
# print(res)
# print(Vector.validate(50))
print(Vector.norm(2 , 2))
