class Shape:
    def __init__(self,name='Unknow', colour='undefined'):
        self.name = name
        self.colour = colour
    
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
 
    def get_colour(self):
        return self.colour
    
    def set_colour(self, colour):
        self.colour = colour

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

C = Circle('red',3.56)
print(C.show())


