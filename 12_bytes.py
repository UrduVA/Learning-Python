'''
bytes Data Type: Represens a group of byte numbers [ 0 to 256 ] just like an array.

>>> x = [10,20,30,40]
>>> type(x)
<class 'list'>
>>> b = bytes(x)
>>> type(b)
<class 'bytes'>
>>> b[0]
10
>>> b[-4]
10
>>> b[:]
b'\n\x14\x1e('
>>> b[0:]
b'\n\x14\x1e('
>>> for j in b : print(b)

b'\n\x14\x1e('
b'\n\x14\x1e('
b'\n\x14\x1e('
b'\n\x14\x1e('
>>> for j in b : print(j)

10
20
30
40
------------------------------
x = [10,20,30,40, 300]
>>> b = bytes(x)
ValueError: bytes must be in range(0, 256)

The only allowed values for byte data type are 0 to 256. By mistake if we are trying to provide any other values then we will get value error.
-----------------------------
>>> b[0]
10
>>> b[0] = 100
TypeError: 'bytes' object does not support item assignment

Once we creates bytes data type value, we cannot change its values,otherwise we will get TypeError.
------------------------------------------------------------
bytearray Data type: Exactly same as bytes data type except that its elements can be modified.

>>> x = [10,20,30,40]
>>> b = bytearray(x)
>>> for j in b : print(b)

bytearray(b'\n\x14\x1e(')
bytearray(b'\n\x14\x1e(')
bytearray(b'\n\x14\x1e(')
bytearray(b'\n\x14\x1e(')
>>> for j in b : print(j)

10
20
30
40
>>> b[0] = 200
>>> for j in b : print(j)

200
20
30
40
'''