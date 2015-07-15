from sys import argv
from PIL import Image
from math import floor
from math import sqrt

_EUCLIDIAN = "euclidian"
_MANHATTAN = "manhattan"
_CHEBYSHEV = "chebyshev"

DEFAULT_DISTANCE = _EUCLIDIAN

def euclidianDistance(sx, sy, x, y):
    return sqrt((sx - x)**2 + (sy - y)**2)    

def manhattanDistance(sx, sy, x, y):
    return abs(sx - x) + abs(sy - y)

def chebyshevDistance(sx, sy, x, y):
    return max(abs(sx - x), abs(sy - y))

ALLOWED_DISTANCES = {_EUCLIDIAN: euclidianDistance, _MANHATTAN: manhattanDistance, 
                     _CHEBYSHEV: chebyshevDistance}

def parseFile(fileName):
    f = file(fileName, "r")
    dimensions = False
    stars = set()
    for line in f.readlines():
        if not dimensions:
            dimensions = True
            arr = line.replace("\n", "").split(" ")
            if len(arr) != 2:
                raise Exception("width height expected")

            width, height = map(int, arr)

            if width < 1:
                raise Exception("width must be greater than 0")
            if height < 1:
                raise Exception("height must be greater than 0")
        else:
            arr = line.replace("\n", "").split(" ")
            if len(arr) != 6:
                raise Exception("x y intensity red green blue expected")
            x, y, intensity, red, green, blue = map(int, arr)
            if intensity < 1:
                raise Exception("intensity must be greater than 0")
            if 255 > red < 0:
                raise Exception("red must be in range [0, 255]")
            if 255 > green < 0:
                raise Exception("green must be in range [0, 255]")
            if 255 > blue < 0:
                raise Exception("blue must be in range [0, 255]")

            stars.add((x, y, intensity, red, green, blue))

    return width, height, stars

def parseArg(argv):
    if len(argv) == 1:
        raise Exception("Missing arguments")
    elif len(argv) == 2:
        return argv[1], DEFAULT_DISTANCE
    elif len(argv) == 3:
        if argv[2] in ALLOWED_DISTANCES:
            return argv[1], argv[2]
        return argv[1], DEFAULT_DISTANCE
    else:
        raise Exception("Too many arguments")

def computeValues(x, y, stars, distance):
    comulativeRed = 0
    comulativeGreen = 0
    comulativeBlue = 0
    for star in stars:
        sx, sy, intensity, red, green, blue = star
        dist =  ALLOWED_DISTANCES[distance](sx, sy, x, y) 
        comulativeRed += intensity * red / (dist + 1)
        comulativeGreen += intensity * green / (dist + 1)
        comulativeBlue += intensity * blue / (dist + 1)

    comulativeRed = int(floor(comulativeRed))
    comulativeGreen = int(floor(comulativeGreen))
    comulativeBlue = int(floor(comulativeBlue))
    
    return comulativeRed, comulativeGreen, comulativeBlue

def createImage(width, height, stars, distance):
    print "creating image with size {width}, {height}".format(width=width,
                                                              height=height)
    print "using {distance} distance".format(distance=distance)

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for i in xrange(width):
        for j in xrange(height):
            red, green, blue = computeValues(i, j, stars, distance)
            pixels[i,j] = (red, green, blue)

    return image

def main(argv):
    fileName, distance = parseArg(argv)
    width, height, stars = parseFile(fileName)
    
    image = createImage(width, height, stars, distance)

    image.show()

    decision = raw_input("Do you want to save the image to {0}.jpg?(y)".format(fileName))
    if decision == "y":
        image.save("{0}.jpg".format(fileName))

if __name__ == "__main__":
    main(argv)
