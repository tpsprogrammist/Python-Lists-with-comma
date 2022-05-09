Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

================== RESTART: /Users/pate/Documents/commalist.py =================
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 11, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 7, in foo
    for i in length:
TypeError: 'int' object is not iterable

================== RESTART: /Users/pate/Documents/commalist.py =================
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 11, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 8, in foo
    commalist += list[i] + ', '
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 11, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 8, in foo
    commalist += list[i]
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 11, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 8, in foo
    commalist = commalist + list[i]
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 12, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 9, in foo
    commalist = commalist + list[i]
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 12, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 9, in foo
    commalist = commalist + str(list[i])
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
<class 'int'>
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 13, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 10, in foo
    commalist = commalist + str(list[i])
TypeError: list indices must be integers or slices, not str

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
<class 'int'>
applesbananastofucats

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
apples,bananas,tofu,cats,

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
0
1
2
3
apples,bananas,tofu,cats,

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
0
1
2
3
apples,bananas,tofu,cats,

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
4
0
1
2
3
apples,bananas,tofu,cats,

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 17, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 7, in foo
    print(length +  ' length')
TypeError: unsupported operand type(s) for +: 'int' and 'str'

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
Traceback (most recent call last):
  File "/Users/pate/Documents/commalist.py", line 17, in <module>
    expose = foo(spam)
  File "/Users/pate/Documents/commalist.py", line 7, in foo
    print('length' + length)
TypeError: can only concatenate str (not "int") to str

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
length4
0
1
2
3
apples,bananas,tofu, and cats

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
length4
0
1
2
3
apples, bananas, tofu,  and cats

================== RESTART: /Users/pate/Documents/commalist.py =================
<class 'str'>
length4
0
1
2
3
apples, bananas, tofu, and cats
