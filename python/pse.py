...     i = 1
...     while i <= 10:
...         print(i)
...         i += 1
...         
>>> print_numbers()
1
2
3
4
5
6
7
8
9
10
>>> def print_numbers(n):
...     i = 1
...     while i <= n:
...         print(i)
...         i += 1
...         
>>> print_numbers(5)
1
2
3
4
5
>>> print_munbers(10)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    print_munbers(10)
    ^^^^^^^^^^^^^
NameError: name 'print_munbers' is not defined. Did you mean: 'print_numbers'?
>>> print_numbers(10)
1
2
3
4
5
6
7
8
9
10
>>> print_numbers(20)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> def sum_numbers(n):
...     i = 1
...     total = 0
...     while i <= n:
...         total = total + i
...         i += 1
...     return total
...     
>>> sum_numbers(5)
15
>>> sum_numbers(11)
66
>>> sum_numbers(23)
276
>>> sum_numbers(5683)
16151086
>>> sum_numbers(106839)
5707339380
>>> def sum_numbers(n):
...     total = 0
...     for i in range(1, n + 1):
...         total = total + i
...     return total
... def sum_numbers_to_10():
...     return sum_(10)
...     
>>> sum_numbers_to_10()
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    sum_numbers_to_10()
    ~~~~~~~~~~~~~~~~~^^
  File "<python-input-13>", line 7, in sum_numbers_to_10
    return sum_(10)
           ^^^^
NameError: name 'sum_' is not defined. Did you mean: 'sum'?
>>> def sum_numbers(n):
...     total = 0
...     for i in range(1, n + 1):
...         total = total + i
...     return total
... def sum_numbers_to_10():
...     return sum_numbers(10)
...     
>>> sum_numbers_to_10()
55
>>> 
>>> def add_two_numbers(x, y)
  File "<python-input-0>", line 1
    def add_two_numbers(x, y)
                             ^
SyntaxError: expected ':'
>>> def add_two_numbers(x, y)
  File "<python-input-1>", line 1
    def add_two_numbers(x, y)
                             ^
SyntaxError: expected ':'
>>> clear

>>> def add_two_numbers(x, y)
  File "<python-input-2>", line 1
    def add_two_numbers(x, y)
                             ^
SyntaxError: expected ':'
>>> def is_even(x):
...     return 0
...     
>>> is_even(5)
0
>>> def is_even(x):
...     return false
...     
>>> is_even(5)
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    is_even(5)
    ~~~~~~~^^^
  File "<python-input-5>", line 2, in is_even
    return false
           ^^^^^
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> def is_odd(x):
...     return False
...     
>>> is_odd(5)
False
>>> x = 5
>>> y = 2
>>> x % y
1
>>> i = 1 
>>> while i <= 10:
...     print(f"{i} % 2 = {i % 2}")
...     i += 1
...     
1 % 2 = 1
2 % 2 = 0
3 % 2 = 1
4 % 2 = 0
5 % 2 = 1
6 % 2 = 0
7 % 2 = 1
8 % 2 = 0
9 % 2 = 1
10 % 2 = 0
>>> def is_even(x):
...     return x % 2 == 0
...     
>>> def print_odd_even():
...     i = 1
...     while i <= 10:
...         if is_even(i):
...             print(f"{i} is even")
...         else:
...             print(f"{i} is odd")
...         i += 1
