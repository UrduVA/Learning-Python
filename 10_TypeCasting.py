'''
Type Casting:
Convert one type value to another type, called as Typecasting or
Type coversion.

1. int()
2. float()
3. complex()
4. bool()
5. str()

1.int(): Convert values from other types to int.
1. We can convert from any type to int except complex type.
2. If we want to convert string type to int type, compulsary string should contain only integral value and should be specified in base-10

>>> int(123.654)
123
>>> int(True)
1
>>> int(False)
0
>>> int("20")
20
>>> int("20.50")
ValueError: invalid literal for int() with base 10: '20.50'

>>> int("two")
ValueError: invalid literal for int() with base 10: 'two'

>>> int("0B111")
ValueError: invalid literal for int() with base 10: '0B111'

>>> int("0X16")
ValueError: invalid literal for int() with base 10: '0X16'

>>> int("3+5j")
ValueError: invalid literal for int() with base 10: '3+5j'
_____________________________________________________________________
2. float(): Convert other type values to float type.

1. Van Convert any type value to float type except complex type.
2. Whenever we are trying to convert string type to float type compulsary string should be either integral or floating point literal and should be specified only in base-10.

>>> float(10)
10.0
>>> float(10.10)
10.1
>>> float(True)
1.0
>>> float(False)
0.0
>>> float("10.20")
10.2
>>> float("Ten") : ValueError: could not convert string to float: 'Ten'
>>> float("0B11") : ValueError: could not convert string to float: '0B11'
____________________________________________________________________
3.complex(): Convert other types to complex type.

Form-1: complex(x)
Convert x into complex number with real part x and imaginary part 0.

>>> complex(20)
(20+0j)
>>> complex(20.0)
(20+0j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex("15")
(15+0j)
>>> complex("20.50")
(20.5+0j)
>>> complex("ten")
ValueError: complex() arg is a malformed string

Form-2: complex(x,y)
Convert x and y into complex number such that x will be real part and y will be imaginary part.

>>> complex(10,20)
(10+20j)
>>> complex(10.50,20.50)
(10.5+20.5j)
>>> complex(False,20.50)
20.5j
>>> complex(True,20.50)
(1+20.5j)
>>> complex('10',20.50)
TypeError: complex() can't take second arg if first is a string
>>> complex('10','20.50')
TypeError: complex() can't take second arg if first is a string
____________________________________________________________________
4. bool(): Convert other type values to bool type.

    False -> 0, 0.0, 0+0j "[emptyString]" otherwise True

>>> bool("0")
True
>>> bool(0)
False
>>> bool("")
False
>>> bool(10)
True
>>> bool(0.122)
True
>>> bool(0.0)
False
>>> bool(0+0j)
False
____________________________________________________________________
5. str(): Convert other type values to str type

>>> str(10)
'10'
>>> str(Hello)
NameError: name 'Hello' is not defined
>>> str('Hello')
'Hello'
>>> str(50.20)
'50.2'
>>> str(True)
'True'

'''