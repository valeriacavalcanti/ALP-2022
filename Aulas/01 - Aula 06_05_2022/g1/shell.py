Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10+10
20
>>> 14%4
2
>>> 10%2
0
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>> sys.float_info.max
1.7976931348623157e+308
>>> true
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> 'valeria'
'valeria'
>>> "valeria"
'valeria'
>>> 'ifpb' + 4
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    'ifpb' + 4
TypeError: can only concatenate str (not "int") to str
>>> nome = 'Valéria Maria'
>>> nome
'Valéria Maria'
>>> idade
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    idade
NameError: name 'idade' is not defined
>>> idade = 15
>>> idade
15
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'idade', 'nome', 'sys']
>>> idade = 100
>>> idade
100
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> nome = input('Digite seu nome: ')
Digite seu nome: Valéria Maria
>>> nome
'Valéria Maria'
>>> idade = input('Digite sua idade: ')
Digite sua idade: 15
>>> nome
'Valéria Maria'
>>> idade
'15'
>>> idade*2
'1515'
>>> type(idade)
<class 'str'>
>>> 
= RESTART: Z:/1744888/Documents/primeiro.py
Digite seu nome: Valéria Maria Bezerra
Digite sua idade: 15
Valéria Maria Bezerra 15
>>> 
= RESTART: Z:/1744888/Documents/primeiro.py
Digite seu nome: Valéria Maria
Digite sua idade: 15
<class 'str'> Valéria Maria
<class 'int'> 15
>>> 