class Complex :
    def __init__(self , real , img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i + " , self.img , "j")

    # def add(self , num2): -> Normal logic
    # we used dunder function here to add and operate something new function
    def __add__(self , num2):
        Real = self.real + num2.real
        Img = self.img + num2.img
        # print( "Sum of two given complex number is : " ,Real , "i + " , Img , "j")
        return Complex(Real , Img)

    def __sub__(self , num2 ):
        Real = self.real - num2.real
        Img = self.img - num2.img
        # print( "Sum of two given complex number is : " ,Real , "i + " , Img , "j")
        return Complex(Real, Img)
num1 = Complex( 1 , 4 )
num1.showNumber()

num2 = Complex(4 , 5)
num2.showNumber()

# this is called operator overloading
num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()