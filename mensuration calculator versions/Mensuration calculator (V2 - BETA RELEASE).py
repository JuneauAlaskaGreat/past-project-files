import math
import time

π = 3.14
Circle = 1

# list for quadrilateral subset of 2d shapes
def betalist():
    betalistz = "1 - Square\n2 - Rectangle\n3 - Trapezium"
    print(betalistz)
# division list in trigonometry and 2d shapes

# list for 2d shapes and commands
def alist():
    alistza = "\n2D SHAPES:\n360 - Circle\n3 - Triangle\n4 - Quadrilaterals\n6 - Hexagon (CURRENTLY GIVES INCORRECT ANSWER)"
    print(alistza)
# list for 3d shapes and commands
def blist():
    blistza = "\n3D SHAPES:\n1 - Sphere\n2 - cylinder\n3 - cube\n"
    print(blistza)

# 2d shapes area formulas
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
# defines the hexagon function
def hexagon():
    fgy = int(float(input('Enter the side A: ')))
    ghyz = ((3*math.sqrt(3)/3)*(fgy*fgy))
    print(ghyz)
    
# 3d shapes volume formulas
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
# defines the cube function
def cube():
    sd = int(input('Enter a number (length): '))
    fz = (sd*sd*sd)
    print(fz)
    # defines the pyramid 4 line function
def foursidepyramid():
    print("")

# 3d shapes surface area formulas
# defines the sphere (surface area) function
def spheresurfacearea():
    f = int(input('Enter a number (radius): '))
    h = (4*π*f*f)
    print(h)


while True:
    print("MENSURATION CALCULATOR V2.0 - BETA RELEASE")
    print("Volume and area functions are available, surface area and perimeter functions are not available")
    time.sleep(2)
    alist()
    blist()
    # starting function for options of mensuration
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
            # directs to square function
            if zxv == 1:
                square()
            # directs to rectangle function
            elif zxv == 2:
                rectangle()
            # directs to trapezium function
            elif zxv == 3:
                trapezium()
        elif z == 6:
            hexagon()
    # directs to 3d shapes
    elif jz == 30:
        # option for volume or surface area
        rt = int(input("Volume or surface area: "))
        # option for volume
        if rt == '1':
            xk = int(input("Enter an option: "))
            # directs to sphere function
            if xk == 1:
                sphere()
            # directs to cylinder function
            elif xk == 2:
                cylinder()
            # directs to cube function
            elif xk == 3:
                cube()
        # option for surface area
        elif rt == '2':
            ghim = int(input("Enter an option: "))
            # directs to the option for the surface area of a sphere
            if ghim == '1':
                spheresurfacearea()
    else:
        error404 = '\nError 404 - restarting program\n'
        print(error404)
    time.sleep(5)

    pass
        
