from circle import Circle
from square import Square

def main():
   
    round1 = Circle("red",5.5)
    round2 = Circle("blue",10.5)
    playARound = Circle()  

    square1 = Square(5, "orange")
    square2 = Square(12, "purple")
    playASquare = Square()  

    round1.show()
    round2.show()
    playARound.show()

    square1.show()
    square2.show()
 
    playARound = round1 + round2  
    playASquare = square2 + square1 
    
    playARound.show()
    playASquare.show()

    playARound = round1 * round2  
    playASquare = square2 * square1 

    playARound.show()
    playASquare.show() 

    playARound = round1
    
    if playARound == round1:
        print("\nHurray !!")
    else:
        print("\nAwww !!")

if __name__ == "__main__":
    main()
