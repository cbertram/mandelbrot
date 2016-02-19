# mandelbrot
Program written in python, approximating the mandelbrot set, and saving it to a .png file. 

## How to use
The program requires the [PyPNG](https://github.com/drj11/pypng) module. ([python2-pypng](https://aur.archlinux.org/packages/python2-pypng/) AUR package if running Arch Linux)

To start the program, run `python2 mandelbrot.py`. The number of processed lines is writen every time the program is done processing a horisontal 1px line.

When the program is done, it will genrate a .png file in the same directory as the program (will overrite file with the same name). By default the image will be grayscale.

The variables in the top of the program are used to custimize the output.
 * `NAME` specifies the name of the output file.
 * `HEIGHT` and `WIDTH` specify the dimensions of the output file in pixels.
 * `X` and `Y` specify the coordiantes of where on the complex plane to approximate the set. By default this is the center of the image, but if `X -= XL/2` and `Y += YL/2` are commented out, it will be the top left corner of the image.
 * `XL` and `YL` specify the length on the complex plane, to approximate in the x and y direction. Remember to end whole numbers with .0!
 * `MAXIT` specifies how many iterations the recursive mandelbrot function should run. The precision of the approximation will be increased when this gets bigger, which is needed when zooming in, or genrating high definition images. If this gets higher than 1000, then the recursion limit must be increased (Watch out for stack overflow, if this is increased too much).
 
## Further customization
There are a few other things that can be changed to customize the output:
 * Colorcycle can be changed by editing `m = m` to something like `m = 2*m` to change how fast the colors cycle. This sometimes needs to be asjusted when `MAXIT` is changed.
 * Color can be changed from grayscale to rgb by commenting the the line setting the grayscale color, and uncommenting the line setting RGB color. You can change how the RGB color is calculated to get a colorcycle that you like. The line `w = png.Writer(WIDTH, HEIGHT, greyscale=True)` also needs to be changed to `w = png.Writer(WIDTH, HEIGHT, greyscale=False)`.
