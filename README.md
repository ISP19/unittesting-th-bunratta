## Unit Testing Assignment

by T. Bunratta.

[![Build Status](https://travis-ci.com/th-bunratta/unittesting-th-bunratta.svg?branch=master)](https://travis-ci.com/th-bunratta)

## Test Cases for ```unique```

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| 1 list with 1 item               |  list with 1 item   |
| 1 list with repetitive items   |  list with 1 item   |
| 1 list with repetitive items in various orders | 2-item list, items in same order  |
| 1 list with the huge (arbitrary) number of repetitive items | 1 list with 1 item |
| nested lists with all repetitive items | 1 top-level lists with no nested list element conflict |
| non-lists  | InvalidTypeException raised |


## Test Cases for ```Fraction``` class

### Equality operator (```==```)
| Test case              |  Expected Result    |
|------------------------|---------------------|
|Fraction instance of a whole number and an integer of the same value|Equal|
|Pairs of fractions of positive numerator and denominator and their respective reduced form |Equal|
|Pairs of fractions of negative numerator and denominator and their respective reduced form |Equal|
|Pairs of fractions of numerator and denominator and their negative reduced form |Equal|
|Pairs of fractions and their reduced form of approximate value |Not equal|
### Plus operator (```+```) and subtraction operator (```-```)
| Test case              |  Expected Result    |
|------------------------|--------------------|
|Fraction plus zero| The same fraction|
|Positive fractions plus positive ones|Added positive fraction|
|Positive fractions plus greater negative ones (also subtracts)|Subtracted negative fraction|
|Positive fractions plus lesser negative ones (also subtracts)|Subtracted positive fraction|
|Negative fractions plus negative ones|Added negative fraction|

### Multiplication operator (```*```)
| Test case              |  Expected Result    |
|------------------------|---------------------|
|Fraction multiplied by zero|Zero|
|Positive fraction multiplied by positive fraction|Multiplied positive fraction|
|Negative fraction multiplied by positive fraction|Multiplied negative fraction|
|Negative fraction multiplied by negative fraction|Multiplied positive fraction|
### String representation and the constructor of the object (```__str__``` and ```__init__```)
| Test case              |  Expected Result    |
|------------------------|---------------------|
|Fraction without denominator of 1 or 0|Fraction representation in "numerator/denominator" form, e.g. 1/2, 1/3, -6/7|
|Fraction with denominator of 1|Whole number with value equal to that of the numerator|
|Fraction with denominator of 0|ZeroDivisionError raised|
|Indeterminate form of 1/0 as a representation of positive infinity|math.inf|
|Indeterminate form of -1/0 as a representation of negative infinity|-math.inf|
|Indeterminate form of 0/0|math.NaN|