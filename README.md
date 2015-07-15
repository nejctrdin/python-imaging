# python-imaging

This is an implementation of The Colors in Our Stars. The problem is specified on [Code Golf Stack Exchange](http://codegolf.stackexchange.com/questions/53124/the-colors-in-our-stars).

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

The configuration file needs at least one line giving a space separated `width` and `height`. Each subsequent line is of the form `x y intensity red green blue`, which gives the position of the star on a plane by `x` and `y`. Additionally it gives a non-zero star `intensity` and the colours in RGB space by `red`, `green` and `blue`. The colours must be in range `[0, 255]`. For examples, see configuration files in repository.

## Examples
