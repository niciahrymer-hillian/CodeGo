>>> age = 25
>>> age 
25
>>> score = 100
>>> score
100
>>> negative = -10
>>> negative
-10
>>> sum_total = age + score
>>> sum_total
125
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'age', 'negative', 'score', 'sum_total']
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, 'age': 25, 'score': 100, 'negative': -10, 'sum_total': 125}
>>> 

>>> is_student = True
>>> is_student
True
>>> has_passed_exam = False
>>> has_passesd_exam
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    has_passesd_exam
NameError: name 'has_passesd_exam' is not defined. Did you mean: 'has_passed_exam'?
>>> has_passed_exam = False
>>> has_passed_exam
False
>>> result = 10 > 5
>>> result
True
>>> is_equal = (15 == 15)
>>> is_equal
True
>>> price = 19.99
>>> price
19.99
>>> temperature = -2.5
>>> temperature
-2.5
>>> result = 10.5 + 3.7
>>> result
14.2
>>> division = 10.0 / 3.0
>>> division
3.3333333333333335
>>> name = "John"
>>> name
'John'
>>> greeting = "Hello, World!"
>>> greeting
'Hello, World!'
>>> combined = name + " says " + greeting
>>> combined
'John says Hello, World!'
>>> empty = ""
>>> empty
''
>>> formatted = f"{name} says {greeting}"
>>> formatted
'John says Hello, World!'
>>> x = 5
>>> type(x)
<class 'int'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> x = 3.14
>>> type(x)
<class 'float'>
>>> 

