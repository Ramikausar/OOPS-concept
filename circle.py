from shape import Shape

class Circle(Shape):
    def __init__(self, colour='undefined', radius=0.0):
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
        print("circumfrence \t    : ",self.perimeter())
        print("AREA \t \t    : ",self.area())

    def __add__(self,circle2):
        colour =self.colour 
        c3_radius = self.get_radius() + circle2.get_radius()

        return Circle(colour,c3_radius)
    
    def __mul__(self,circle2):
        colour =self.colour 
        c3_radius = self.get_radius() * circle2.get_radius()
        return Circle(colour,c3_radius)
    
    def __eq__(self,circle2):
        colour =self.colour 
        if(self.colour == colour and self.get_radius() == circle2.get_radius()):
            print("2 circle are same")
        else:
            False
    
 