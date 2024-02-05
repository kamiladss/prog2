class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
        
    def area(self):
        return self.length * self.length
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
shape= Shape()
print(shape.area()) 
square= Square(2)
print(square.area())
rect= Rectangle(2,3)
print(rect.area())
        
        