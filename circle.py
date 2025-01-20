from shape import Shape

class Circle(Shape):
    def __init__(self, colour='undefined', radius='0.0'):
        self.radius = radius
        super().__init__('circle', colour)

    def get_radius(self):
        return self.radius
    
    def set_radius(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def show(self):
        print("SHAPE INFORMATION")
        print("NAME \t \t    : ",self.name)
        print("COLOUR \t \t    : ",self.colour)
        print("RADIUS \t \t    : ",self.get_radius())
        print("circumfrence  : ",self.perimeter())
        print("AREA \t \t    : ",self.area())