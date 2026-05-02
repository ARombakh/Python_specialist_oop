import math

class Point:
    """ x, y, dist, __str__, __init__, move """

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.dist_val: int | None = None
    
    def dist(self) -> int:
        if self.dist_val == None:
            self.dist_val = math.sqrt(self.x * 2 + self.y * 2)
        return self.dist_val
    
    def __str__(self):
        return ("x = " + str(self.x) + "\n" +
                "y = " + str(self.y) + "\n" +
                "dist = " + str(self.dist()))

    def move(self, dx, dy) -> "Point":
        x = self.x
        y = self.y
        return Point(x + dx, y + dy)

point = Point(2, 3)

print(point)

point2 = point.move(1 , 1)

print(point2)