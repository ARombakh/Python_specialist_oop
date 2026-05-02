from math import sqrt, cos, sin, radians

CARTESIAN = 'cartesian'
POLAR = 'polar'

class Point:
    """ x, y, dist, __str__, __init__, move """

    def __init__(self, coord1: float, coord2: float, *args,
                 name: str = CARTESIAN):
        if name == CARTESIAN:
            self.x: float = coord1
            self.y: float = coord2
            self.dist_val: float = sqrt(coord1 * coord1 +
                                               coord2 * coord2)
        else:
            self.x: float = coord1 * cos(radians(coord2))
            self.y: float = coord1 * sin(radians(coord2))
            self.dist_val: float = coord1
    
    # def dist(self) -> int:
    #     if self.dist_val == None:
    #         self.dist_val = math.sqrt(self.x * 2 + self.y * 2)
    #     return self.dist_val
    
    def __str__(self):
        return ("x = " + str(self.x) + "\n" +
                "y = " + str(self.y) + "\n" +
                "dist = " + str(self.dist_val))

    def move(self, dx, dy) -> "Point":
        x = self.x
        y = self.y
        return Point(x + dx, y + dy)

point = Point(2, 3)

print(point)

point2 = point.move(1 , 1)

print(point2)