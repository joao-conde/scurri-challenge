# Scurri Coding Challenge

Scurri coding challenges solutions.

## Challenge 1

> *"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”".*

[Folder 1](1/) contains the solution for the first challenge.
There are shorter ways to write a FizzBuzz but I prefer readable code.

## Challenge 2

> *"Write a library that supports validating and formatting postcodes for the UK. The details of which postcodes are valid and which are the parts they consist of can be [found here.](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting)."*

[Folder 2](2/) contains the solution for the second challenge.
Generalized the package to support more postal codes, but implemented only the UK validator and formatter.

### Installing

```
python setup.py install
```

### Running Tests


```
python setup.py test
```

### Running Examples

```
PYTHONPATH=src python examples/build.py
```
