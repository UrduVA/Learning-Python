#float data type, Complex Data Type, bool data type

# float data type : To represent floating point values (decimal values)
f=1.234
print(type(f)) #<class 'float'>

''' We can also represent floating point values by using exponential form (scientific notation) 
Instead of 'e' we can use 'E'.
The main advantage of exponential form is we can represent big values in less memory.
'''

f=1.2e3
print(f) #1200.0

'''
Note: We can represent int values in decimal, binary, octal and hexa decimal forms. 
But we can represent float values only by using decimal form.
>>> f=0o123.456 : SyntaxError: invalid syntax
>>> f=0X123.456 : SyntaxError: invalid syntax
'''
#f=0B11.01 #Error

'''
Complex Data Type:
A complex number is of the form : a + bj
a and b contain intergers or floating point values

3+5j
10+5.5j
0.5+0.1j

In the real part if we use int value then we can specify that either by decimal,octal,binary or hexa decimal form.
But imaginary part should be specified only by using decimal form.

>>> a=0B11+5j #(3+5j)

>>> a=3+0B11j # SyntaxError: invalid syntax

Even we can perform operations on complex type values.
>>> a=10+1.5j
>>> b=20+2.5j
>>> c=a+b
>>> c
(30+4j)
>>> type(c)
<class 'complex'>

Note: Complex data type has some inbuilt attributes to retrieve the real part and imaginary part.
We can use complex type generally in scientific Applications and electrical engineering Applications.
'''
c=10.5+3.6j
print(c.real)  #10.5
print(c.imag)  #3.6

'''
bool data type:
To represent boolean values.
The only allowed values for this data type are: True and False
Internally Python represents True as 1 and False as 0

>>> a=10
>>> b=20
>>> a > b
False
>>> a < b
True

>>> True+True
2
>>> True-False
1
'''
b=True
print(type(b)) #<class 'bool'>


