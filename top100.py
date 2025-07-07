# 1. abs() - Returns the absolute value of a number
print(abs(-5))  # 5

# 2. all() - Returns True if all elements of the iterable are true
print(all([True, True, False]))  # False

# 3. any() - Returns True if any element of the iterable is true
print(any([False, False, True]))  # True

# 4. ascii() - Returns a string with non-ASCII characters escaped
print(ascii('café'))  # 'caf\xe9'

# 5. bin() - Converts an integer to a binary string
print(bin(10))  # '0b1010'

# 6. bool() - Converts a value to a Boolean
print(bool(0))  # False

# 7. bytearray() - Returns a mutable array of bytes
print(bytearray('abc', 'utf-8'))  # bytearray(b'abc')

# 8. bytes() - Returns an immutable bytes object
print(bytes('abc', 'utf-8'))  # b'abc'

# 9. callable() - Checks if the object appears callable
def foo(): pass
print(callable(foo))  # True

# 10. chr() - Returns the string representing a character whose Unicode code point is the integer
print(chr(97))  # 'a'

# 11. classmethod() - Converts a method to a class method
class MyClass:
    @classmethod
    def hello(cls):
        return 'hello'
print(MyClass.hello())  # 'hello'

# 12. compile() - Compiles source into a code or AST object
code = compile('print(123)', '', 'exec')
exec(code)  # 123

# 13. complex() - Creates a complex number
print(complex(2, 3))  # (2+3j)

# 14. delattr() - Deletes an attribute from an object
class A: x = 1
delattr(A, 'x')
print(hasattr(A, 'x'))  # False

# 15. dict() - Creates a new dictionary
d = dict(a=1, b=2)
print(d)  # {'a': 1, 'b': 2}

# 16. dir() - Returns a list of valid attributes for an object
print(dir([]))  # List of list methods

# 17. divmod() - Returns the quotient and remainder of dividing two numbers
print(divmod(9, 2))  # (4, 1)

# 18. enumerate() - Returns an enumerate object with index and value pairs
for i, v in enumerate(['a', 'b']):
    print(i, v)  # 0 a \n 1 b

# 19. eval() - Evaluates a Python expression from a string
print(eval('2 + 2'))  # 4

# 20. exec() - Executes Python code dynamically
exec("x = 5")
print(x)  # 5

# 21. filter() - Filters elements of an iterable using a function
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # [1, 2]

# 22. float() - Converts a value to a floating point number
print(float('3.14'))  # 3.14

# 23. format() - Formats a value using a format string
print(format(3.14159, '.2f'))  # '3.14'

# 24. frozenset() - Returns an immutable frozenset object
print(frozenset([1, 2, 3]))  # frozenset({1, 2, 3})

# 25. getattr() - Returns the value of a named attribute of an object
class B: y = 10
print(getattr(B, 'y'))  # 10

# 26. globals() - Returns a dictionary of the current global symbol table
print('globals' in globals())  # True

# 27. hasattr() - Checks if an object has a given attribute
print(hasattr(B, 'y'))  # True

# 28. hash() - Returns the hash value of an object
print(hash('abc'))  # Hash value

# 29. help() - Invokes the built-in help system
# help(str)  # Uncomment to see help

# 30. hex() - Converts an integer to a hexadecimal string
print(hex(255))  # '0xff'

# 31. id() - Returns the identity of an object
a = []
print(id(a))  # Memory address

# 32. input() - Reads a line from input
# name = input("Enter name: ")  # User input

# 33. int() - Converts a value to an integer
print(int('42'))  # 42

# 34. isinstance() - Checks if an object is an instance of a class or tuple of classes
print(isinstance(5, int))  # True

# 35. issubclass() - Checks if a class is a subclass of another class
class C: pass
print(issubclass(C, object))  # True

# 36. iter() - Returns an iterator object
it = iter([1, 2, 3])
print(next(it))  # 1

# 37. len() - Returns the length of an object
print(len([1, 2, 3]))  # 3

# 38. list() - Creates a new list
print(list('abc'))  # ['a', 'b', 'c']

# 39. locals() - Returns a dictionary of the current local symbol table
def f(): print('x' in locals())
f()  # False

# 40. map() - Applies a function to every item of an iterable
print(list(map(str.upper, ['a', 'b'])))  # ['A', 'B']

# 41. max() - Returns the largest item in an iterable
print(max([1, 2, 3]))  # 3

# 42. memoryview() - Returns a memory view object of the given argument
print(memoryview(b'abc')[0])  # 97

# 43. min() - Returns the smallest item in an iterable
print(min([1, 2, 3]))  # 1

# 44. next() - Retrieves the next item from an iterator
it = iter([10, 20])
print(next(it))  # 10

# 45. object() - Returns a new featureless object
o = object()
print(type(o))  # <class 'object'>

# 46. oct() - Converts an integer to an octal string
print(oct(8))  # '0o10'

# 47. open() - Opens a file and returns a file object
# f = open('test.txt', 'w'); f.write('hi'); f.close()

# 48. ord() - Returns the Unicode code point for a single character
print(ord('a'))  # 97

# 49. pow() - Returns base to the power of exp
print(pow(2, 3))  # 8

# 50. print() - Prints objects to the text stream
print('Hello, world!')  # Hello, world!

# 51. property() - Returns a property attribute
class D:
    def __init__(self): self._x = 0
    def getx(self): return self._x
    def setx(self, value): self._x = value
    x = property(getx, setx)
d = D(); d.x = 5; print(d.x)  # 5

# 52. range() - Returns an immutable sequence of numbers
print(list(range(3)))  # [0, 1, 2]

# 53. repr() - Returns a string containing a printable representation of an object
print(repr('abc'))  # "'abc'"

# 54. reversed() - Returns a reversed iterator
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# 55. round() - Rounds a number to a given precision
print(round(3.14159, 2))  # 3.14

# 56. set() - Returns a new set object
print(set([1, 2, 2, 3]))  # {1, 2, 3}

# 57. setattr() - Sets an attribute of an object
class E: pass
setattr(E, 'z', 99)
print(E.z)  # 99

# 58. slice() - Returns a slice object
s = slice(1, 3)
print([0, 1, 2, 3][s])  # [1, 2]

# 59. sorted() - Returns a sorted list from the items in an iterable
print(sorted([3, 1, 2]))  # [1, 2, 3]

# 60. staticmethod() - Converts a method to a static method
class F:
    @staticmethod
    def foo(): return 'bar'
print(F.foo())  # 'bar'

# 61. str() - Converts an object to a string
print(str(123))  # '123'

# 62. sum() - Sums items of an iterable
print(sum([1, 2, 3]))  # 6

# 63. super() - Returns a proxy object that delegates method calls to a parent or sibling class
class G:
    def hello(self): return 'hello'
class H(G):
    def hello(self): return super().hello() + ' world'
print(H().hello())  # 'hello world'

# 64. tuple() - Creates a tuple
print(tuple([1, 2, 3]))  # (1, 2, 3)

# 65. type() - Returns the type of an object
print(type(123))  # <class 'int'>

# 66. vars() - Returns the __dict__ attribute for a module, class, instance, or the current locals
class I: a = 1
print(vars(I))  # dict of attributes

# 67. zip() - Aggregates elements from two or more iterables
print(list(zip([1, 2], ['a', 'b'])))  # [(1, 'a'), (2, 'b')]

# 68. __import__() - Imports a module
math = __import__('math')
print(math.sqrt(16))  # 4.0

# 69. breakpoint() - Drops into the debugger at the call site
# breakpoint()  # Debugger

# 70. hasattr() - Checks if an object has a given attribute
print(hasattr(I, 'a'))  # True

# 71. setattr() - Sets an attribute of an object
setattr(I, 'b', 2)
print(I.b)  # 2

# 72. delattr() - Deletes an attribute from an object
delattr(I, 'b')
print(hasattr(I, 'b'))  # False

# 73. compile() - Compiles source into a code or AST object
code = compile('a=1+2', '', 'exec')
exec(code)
print(a)  # 3

# 74. complex() - Creates a complex number from a string or numbers
print(complex('1+2j'))  # (1+2j)

# 75. id() - Returns the identity of an object
print(id(123))  # Memory address

# 76. iter() - Returns an iterator object
it = iter('abc')
print(next(it))  # 'a'

# 77. next() - Retrieves the next item from an iterator
print(next(it))  # 'b'

# 78. repr() - Returns a string containing a printable representation of an object
print(repr(123))  # '123'

# 79. reversed() - Returns a reversed iterator
print(list(reversed('abc')))  # ['c', 'b', 'a']

# 80. round() - Rounds a number to a given precision
print(round(2.718, 1))  # 2.7

# 81. sorted() - Returns a sorted list from the items in an iterable
print(sorted('cab'))  # ['a', 'b', 'c']

# 82. sum() - Sums items of an iterable
print(sum((4, 5, 6)))  # 15

# 83. vars() - Returns the __dict__ attribute for a module, class, instance, or the current locals
print(vars())  # Current local symbol table

# 84. zip() - Aggregates elements from two or more iterables
print(list(zip('ab', [1, 2])))  # [('a', 1), ('b', 2)]

# 85. format() - Formats a value using a format string
print(format(255, 'x'))  # 'ff'

# 86. memoryview() - Returns a memory view object of the given argument
mv = memoryview(b'hello')
print(mv[1])  # 101

# 87. property() - Returns a property attribute
class J:
    def __init__(self): self._y = 0
    @property
    def y(self): return self._y
    @y.setter
    def y(self, value): self._y = value
j = J(); j.y = 7; print(j.y)  # 7

# 88. staticmethod() - Converts a method to a static method
class K:
    @staticmethod
    def hi(): return 'hi'
print(K.hi())  # 'hi'

# 89. classmethod() - Converts a method to a class method
class L:
    @classmethod
    def bye(cls): return 'bye'
print(L.bye())  # 'bye'

# 90. frozenset() - Returns an immutable frozenset object
print(frozenset('abc'))  # frozenset({'a', 'b', 'c'})

# 91. bytes() - Returns an immutable bytes object
print(bytes([65, 66, 67]))  # b'ABC'

# 92. bytearray() - Returns a mutable array of bytes
print(bytearray([65, 66, 67]))  # bytearray(b'ABC')

# 93. callable() - Checks if the object appears callable
print(callable(len))  # True

# 94. chr() - Returns the string representing a character whose Unicode code point is the integer
print(chr(8364))  # '€'

# 95. ord() - Returns the Unicode code point for a single character
print(ord('€'))  # 8364

# 96. bin() - Converts an integer to a binary string
print(bin(7))  # '0b111'

# 97. oct() - Converts an integer to an octal string
print(oct(9))  # '0o11'

# 98. hex() - Converts an integer to a hexadecimal string
print(hex(10))  # '0xa'

# 99. bool() - Converts a value to a Boolean
print(bool(''))  # False

# 100. float() - Converts a value to a floating point number
print(float(5))  # 5.0
