
class Circle :
    def __init__(self , r):
        self.r = r

    def area(self):
        print( 3.14 * self.r * self.r )

    def perimeter(self ):
        print(3.14 * self.r)

c = Circle(4)
c.area()
c.perimeter()
