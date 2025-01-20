from shape import Shape


class Square(Shape):
    def __init__(self, SIDE_L=0.0,colour='undefined'):
        self.SIDE_L = SIDE_L
        super().__init__('square', colour)

    def get_SIDE_L(self):
        return self.SIDE_L
    
    def set_SIDE_L(self,SIDE_L):
        self.SIDE_L = SIDE_L

    def perimeter(self):
        return 4*self.SIDE_L
    
    def area(self):
        return self.SIDE_L*self.SIDE_L
    
    def show(self):
        print("SHAPE INFORMATION")
        print("NAME \t \t    : ",self.name)
        print("COLOUR \t \t    : ",self.colour)
        print("Side-Length \t \t    : ",self.get_SIDE_L())
        print("circumfrence  : ",self.perimeter())
        print("AREA \t \t    : ",self.area())

    def __add__(self,square2):
        colour =self.colour 
        s3_Length= self.get_SIDE_L() + square2.get_SIDE_L()
        return Square(s3_Length,colour)
    
    def __mul__(self,square2):
        colour =self.colour 
        s3_Length = self.get_SIDE_L()* square2.get_SIDE_L()
        return Square(s3_Length,colour)
    
    def __eq__(self,square2):
        colour =self.colour 
        if(self.colour == colour and self.get_SIDE_L() == square2.get_SIDE_L()):
            print("2 sauare are same")
        else:
            False