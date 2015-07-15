# python-imaging

This is an implementation of The Colors in Our Stars. The problem is specified on [Code Golf Stack Exchange](http://codegolf.stackexchange.com/questions/53124/the-colors-in-our-stars).

The program creates an image of the specified size and computes the RGB values of each point in space, based on the influences of specified stars. Each star has a position in plane, intensity and the colours of radiation. The influences on each pixel are also based on the distance used in the running of the program. The nearer some point is to the star, the more influenced is by the particular star.

## Dependencies

The program uses [PIL](http://www.pythonware.com/products/pil/), python imaging library for processing images.

## Running the program

The program is run as follows:

```bash
python imaging.py X distance
```

It expects two arguments on the input:

1. The configuration file `X`, and
2. the distance type.

The configuration file needs at least one line giving a space separated `width` and `height`. Each subsequent line is of the form `x y intensity red green blue`, which gives the position of the star on a plane by `x` and `y`. Additionally it gives a non-zero star `intensity` and the colours in RGB space by `red`, `green` and `blue`. The colours must be in range `[0, 255]`. If the program cannot parse the inputs or they are out of range, an `Exception` is raised. For examples, see configuration files in repository.

The currently supported distances are `euclidian`, `manhattan` and `chebyshev`. If the distance is not specified or not recognized, the default `euclidian` distance is used.

## Computing the pixel values

For some pixel `(x, y)` and given `stars`, the value for some colour `c` is computed as follows. For each star the `distance` (`dist(sx, sy, x, y)`) is computed with the chosen metric, and the product of the star `intensity` and `colour` value is divided by the `distance + 1`. This value contributes to the end value of the particular colour in pixel `(x, y)`.

### Distance types

Three distances can be used in the program:

1. Euclidian distance: `dist(sx, sy, x, y) = sqrt((sx-x)**2, (sy - y)**2)`
2. Manhattan distance: `dist(sx, sy, x, y) = abs(sx-x) + abs(sy - y)`
3. Chebyshev distance: `dist(sx, sy, x, y) = max(abs(sx-x), abs(sy - y))`

## Examples
