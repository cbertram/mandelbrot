import png
import math, cmath
import sys

NAME = "mandelbrot.png"
WIDTH, HEIGHT = 1000, 1000
X, XL =  -.7, 3.0
Y, YL = 0,  3.0
MAXIT = 500 # Needs to be increased when zooming in, to get detail
sys.setrecursionlimit(1000) # the recursion limit needs to be increased if you make MAXIT higher

#Coordinates as center (normally they are top-left corner)
X -= XL/2
Y += YL/2

def mandelbrot(z, c, it):
    if math.sqrt(z.real**2 + z.imag**2) > 2:
        return it
    elif it < MAXIT:
        return mandelbrot(z**2+c, c, it+1)
    else:
        return None

def main():
    image = []
    for h in xrange(HEIGHT):
        print h
        row = ()
        for w in xrange(WIDTH):
            x = X + w * XL/WIDTH
            y = Y - h * YL/HEIGHT
            m = mandelbrot(0, complex(x, y), 0)

            if m == None:
                row += (0,)
            else:
                m = m # could be changed to m = 2*m or something like that, when zoomin in, to get more detail 
                #Greyscale
                row += (int((255.0/MAXIT*m)%255),)
                #Color
                #row = row + (math.floor(255/MAXIT*m), math.floor(255/MAXIT*m/5), 0,) #Change the equation to make fancy colors
        image.append(row)

    f = open(NAME, "wb")
    w = png.Writer(WIDTH, HEIGHT, greyscale=True)
    w.write(f, image)
    f.close()

if __name__ == "__main__":
    main()
