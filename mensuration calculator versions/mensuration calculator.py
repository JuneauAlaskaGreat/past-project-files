import math

π = 3.14
Circle = 1

# list for quadrilateral subset of 2d shapes
def betalist():
    betalistz = "1 - Square\n2 - Rectangle\n3 - Trapezium"
    print(betalistz)
# division list in trigonometry and 2d shapes
def trigonometryor2dlist():
    eylist = "1 - 2D shapes\n2 - Trigonometry"
    print(eylist)

# list for 2d shapes and commands
def alist():
    alistza = "\n2D SHAPES:\n\n360 - Circle\n3 - Triangle\n4 - Quadrilaterals"
    print(alistza)
# list for 3d shapes and commands
def blist():
    blistza = "\n3D SHAPES:\n\n1 - Sphere\n2 - cylinder"
    print(blistza)

# 2d shapes
# defines the circle function
def circle():
    x = int(input('Enter a number (radius): '))
    i = (π*(x*x))
    print(i)
# defines the square function
def square():
    m = int(input('Enter a number (length): '))
    jl = (m*m)
    print(jl)
# defines the rectangle function
def rectangle():
    mx = int(input('Enter a number (length): '))
    rz = int(input('Enter a number (width): '))
    xcz = (mx*rz)
    print(xcz)
# defines the triangle function
def triangle():
    xkc = int(float(input('Enter a number (base): ')))
    xkz = int(float(input('Enter a number (height): ')))
    jz = (1/2*xkc*xkz)
    print(jz)
# defines the trapezium function
def trapezium():
    fgn = int(float(input('Enter the side A (base): ')))
    ght = int(float(input('Enter the side B (top): ')))
    ghyt = int(float(input('Enter the height H: ')))
    ghyb = (fgn+ght*ghyt/2)
    print(ghyb)

# 3d shapes
# defines the sphere function
def sphere():
    x = int(input('Enter a number (radius): '))
    i = (π*(x*x*x))
    print(i)
# defines the cylinder function
def cylinder():
    b = int(input('Enter a number (radius): '))
    h = int(input('Enter a number (height): '))
    x0 = (π*(b*b)*h)
    print(x0)

print("MENSURATION CALCULATOR")
# starting function for options of mensuration
while True:
    fZ = input("Do you want to start? ")
    if fZ == 'yes':
        ghzc = int(float(input("1 for commands: ")))
    if ghzc == 1:
        alist()
        blist()
    jz = int(float(input("Choose a number (20 - 2D, 30 - 3D): ")))
    # directs to 2d shapes
    if jz == 20:
        z = int(input("Enter the number of sides (for circles - degrees): "))
        # directs to circle function
        if z == 360:
            circle()
        # directs to triangle function
        elif z == 3:
            triangle()
        # directs to quadrilateral function
        elif z == 4:
            print(betalist())
            zxv = int(input("Select the option: "))
            if zxv == 1:
                square()
            elif zxv == 2:
                rectangle()
            elif zxv == 3:
                trapezium()

    # directs to 3d shapes
    elif jz == 30:
        xk = int(input("Enter an option: "))
        # directs to sphere function
        if xk == 1:
            sphere()
        # directs to cylinder function
        elif xk == 2:
            cylinder()
    else:
        print("Error 404 - restarting program")
        
    pass
    
