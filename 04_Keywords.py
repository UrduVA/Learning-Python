"""
Reserved Words: 
some words are reserved to represent some meaning or functionality. Such type of words are called Reserved words.

Note:
1. All Reserved words in Python contain only alphabet symbols.
2. Except the following 3 reserved words, all contain only lower case alphabet symbols.
 True
 False
 None
Eg: a= true X
a=True √

"""
import keyword
print(keyword.kwlist)
''' ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] '''
print(len(keyword.kwlist))
#35