import time

π = 3.14

# list for quadrilateral subset of 2d shapes
def betalist():
    betalistz = "1 - Square\n2 - Rectangle\n3 - Trapezium\n4 - Kite"
    print(betalistz)
# division list in trigonometry and 2d shapes

# lists for 2d shapes and commands
def olist():
    olistza = "\n2D SHAPES (perimeter):\n1 - Square\n2 - Triangle"
    print(olistza)
def alist():
    alistza = "\n2D SHAPES (area):\n360 - Circle functions/commands\n3 - Triangle\n4 - Quadrilaterals"
    print(alistza)
# lists for 3d shapes commands
def blist():
    blistza = "\n3D SHAPES (volume):\n1 - Sphere\n2 - Cylinder\n3 - Cube\n4 - Cone"
    print(blistza)
def clist():
    clistza = "\n3D SHAPES (surface area):\n1 - Sphere\n2 - Cube\n3 - Cylinder\n4 - Cone\n"
    print(clistza)

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
# defines the semicircle function
def semicircle():
    gfrh = int(float(input('Enter the radius: ')))
    gffh = (1/2*π*gfrh*gfrh)
    print(gffh)
# defines the kite function
def kite():
    sfdr = int(float(input('Enter diagonal A: ')))
    ghtz = int(float(input('Enter diagonal B: ')))
    fgfff = ((sfdr*ghtz)/2)
    print(fgfff)

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
# defines the cone function
def cone():
    ssd = int(float(input('Enter a number (radius): ')))
    ssed = int(float(input('Enter a number (height): ')))
    ghty = (π*ssd*ssd*(ssed*1/3))
    print(ghty)

# defines the function for a given sector of a circle
def circlesector():
    sds = int(float(input('Enter the angle (MAX - 360): ')))
    regz = int(float(input('Enter the radius: ')))
    gdjs = ((sds/360)*π*regz*regz)
    print(gdjs)

# 3d shapes surface area formula
# defines the sphere (surface area) function
def spheresurfacearea():
    op = int(float(input('Enter the radius: ')))
    ghdf = (4*π*op*op)
    print(ghdf)
# defines the cube (surface area) function
def cubesurfacearea():
    ghd = int(float(input('Enter the length: ')))
    ghii = (6*ghd*ghd)
    print(ghii)
# defines the cylinder (surface area) function
def cylindersurfacearea():
    ai = int(float(input('Enter the radius: ')))
    op = int(float(input('Enter the height: ')))
    ghyu = (π*ai*ai*op)
    print(ghyu)
# defines the cone (surface area) function
def conesurfacearea():
    airr = int(float(input('Enter the radius: ')))
    yopp = int(float(input('Enter the cone length: ')))
    ghyug = (π*airr*airr+π*airr*yopp)
    print(ghyug)

def squareperimeter():
    asds = int(float(input('Enter the length: ')))
    ghytt = (4*asds)
    print(ghytt)
def triangleperimeter():
    dau = int(float(input('Enter side A: ')))
    dsau = int(float(input('Enter side B: ')))
    ghtau = int(float(input('Enter side C: ')))
    ferve = (dau+dsau+ghtau)
    print(ferve)

while True:
    print("MENSURATION CALCULATOR V8.0")
    print("NOTE: While the answers are accurate, they may be off by less than one digit")
    time.sleep(4)
    alist()
    olist()
    blist()
    clist()
    # starting function for options of mensuration
    jz = int(float(input("Choose a number (20 - 2D, 30 - 3D): ")))
    # directs to 2d shapes
    if jz == 20:
        ytgs = int(input("Area(1) or Perimeter(2): "))
        if ytgs == 1:
            z = int(input("Enter the number of sides (for circles - degrees): "))
            # directs to circle function
            if z == 360:
                xsc = int(input("Regular(1), semi(2), or sector(3): "))
                if xsc == 1:
                    circle()
                elif xsc == 2:
                    semicircle()
                elif xsc == 3:
                    circlesector()            
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
                # directs to kite function
                elif zxv == 4:
                    kite()
        elif ytgs == 2:
            k = int(input("Enter the desired shape number: "))
            # directs to square (perimeter) function
            if k == 1:
                squareperimeter()
            # directs to triangle (perimeter) function
            elif k == 2:
                triangleperimeter()       
    # directs to 3d shapes
    elif jz == 30:
        tgh = int(input("Volume (1) or Surface Area (2): "))
        if tgh == 1:
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
            # directs to cone function
            elif xk == 4:
                cone()
        elif tgh == 2:
            fdg = int(input("Enter an option: "))
            # directs to sphere (surface area) function
            if fdg == 1:
                spheresurfacearea()
            # directs to cube (surface area) function
            elif fdg == 2:
                cubesurfacearea()
            # directs to cylinder (surface area) function
            elif fdg == 3:
                cylindersurfacearea()
            # directs to cone (surface area) function
            elif fdg == 4:
                conesurfacearea()
    else:
        error404 = '\nError 404 - restarting program\n'
        print(error404)
    time.sleep(5)

    '\n'
    pass
        
