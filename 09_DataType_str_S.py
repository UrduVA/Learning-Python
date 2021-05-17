'''
Slicing of Strings:
* slice means a piece
* [ ] operator is called slice operator,which can be used to retrieve parts of String.
* In Python Strings follows zero based index.
* The index can be either +ve or -ve.
* +ve index means forward direction from Left to Right
* -ve index means backward direction from Right to Left
_______________________________________________________

>>> s = 'Python'
>>> s
'Python'
>>> s[0]
'P'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[6] #IndexError: string index out of range
>>> s[0:]
'Python'
>>> s[:0]
''
>>> s[:]
'Python'
>>> s[0:30]
'Python'
>>> s[:30]
'Python'
>>> s * 5
'PythonPythonPythonPythonPython'
>>> len(s)
6
_______________________________________________________

Note:
1. In Python the following data types are considered as Fundamental Data types
 int
 float
 complex
 bool
 str
2. In Python,we can represent char values also by using str type and explicitly char type is not available.
Eg:
1) >>> c='a'
2) >>> type(c)
3) <class 'str'>
3. long Data Type is available in Python2 but not in Python3. In Python3 long values also we can represent by using int type only.
'''