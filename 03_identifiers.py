"""
Identifiers:
A name in Python program is called identifier.
It can be class name or function name or module name or variable name.
a = 10

Rules to define identifiers in Python:
1. The only allowed characters in Python are
 alphabet symbols(either lower case or upper case)
 digits(0 to 9)
 underscore symbol(_) : 2. If Identifier is start with Underscore (_) then it indicates it is private
By mistake if we are using any other symbol like $ then we will get syntax error.
 cash = 10 √
 ca$h =20 X
2. Identifier should not starts with digit
 123total X
 total123 √
3. Identifiers are case sensitive, Python language is case sensitive language.
 total=10
 TOTAL=999
 print(total) #10
 print(TOTAL) #999

5. We cannot use reserved words as identifiers
Eg: def=10 
6. There is no length limit for Python identifiers. But not recommended to use too lengthy
identifiers.
7. Dollor ($) Symbol is not allowed in Python.
________________________________________________
Q. Which of the following are valid Python identifiers?
1) 123total X
2) total123 √
3) java2share √
4) ca$h X
5) _abc_abc_ √
6) def X
7) if X

Note:
1. If identifier starts with _ symbol then it indicates that it is private
2. If identifier starts with __(two under score symbols) indicating that strongly private
identifier.
3.If the identifier starts and ends with two underscore symbols then the identifier is
language defined special name,which is also known as magic methods.
Eg: __add__
"""