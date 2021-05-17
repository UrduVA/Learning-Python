'''str type: To Represents String data type.
A String is a sequence of characters enclosed within single quotes or double quotes.
>>> s = "Python"
>>> s2 = 'Python'
>>> s
'Python'
>>> s2
'Python'
__________
By using single quotes or double quotes we cannot represent multi line string literals.

s2 = 'Python
SyntaxError: EOL while scanning string literal

For this requirement we should go for triple single quotes(''') or triple double quotes(""")
>>> s3 = '''Python
is
Easy '''
>>> s3
'Python\nis\nEasy '
>>> print(s3)
Python
is
Easy 
______________________
We can also use triple quotes to use single quote or double quote in our String.
>>> ''' This is " character'''
' This is " character'

>>> ' This i " Character '
' This i " Character '

We can embed one string in another string

>>> '''This "Python class very helpful" me! '''
'This "Python class very helpful" me! '
'''