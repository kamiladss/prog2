import math
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def show(self):
        print(self.x, self.y)
        print(f"coordinates: {self.x}, {self.y}")
        
    def move(self, nx, ny):
        self.x=nx
        self.y=ny
        print(f"new coordinates: {nx}, {ny}")
        
    def dist(self, secondPoint):
        distanceX = secondPoint.x - self.x
        distanceY = secondPoint.y - self.y
        distance = round(math.sqrt(distanceX**2 + distanceY**2))
        print(f"distance: {distance}")
        
point1 = Point(2, 6)
point2 = Point(4, 7)

point1.show()
point1.move(3, 5)
point1.dist(point2)
