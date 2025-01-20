from shape import Shape


class Square(Shape):
    def __init__(self, SIDE_L='0.0',colour='undefined'):
        self.SIDE_L = SIDE_L
        super().__init__('square', colour)

    def get_SIDEL_L(self):
        return self.SIDE_L
    
    def set_SIDE_L(self,SIDE_L):
        self.SIDE_L = SIDE_L

    def perimeter(self):
        return 4*self.SIDE_L
    
    def area(self):
        return self.SIDE_L**2
    
    def show(self):
        print("SHAPE INFORMATION")
        print("NAME \t \t    : ",self.name)
        print("COLOUR \t \t    : ",self.colour)
        print("Side-Length \t \t    : ",self.set_SIDE_L())
        print("circumfrence  : ",self.perimeter())
        print("AREA \t \t    : ",self.area())