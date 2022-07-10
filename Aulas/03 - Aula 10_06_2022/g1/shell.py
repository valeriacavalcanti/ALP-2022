Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> media = 80
>>> freq = 80
>>> media >= 70
True
>>> media = 70
>>> media >= 70
True
>>> media = 60
>>> media >= 70
False
>>> media = 80
>>> (media >= 70) and (freq >= 75)
True
>>> if (media >= 70) and (freq >= 75)):
	
SyntaxError: unmatched ')'
>>> if (media >= 70) and (freq >= 75):
	print("eita")
	print("que bom")
	print("aprovado")
else:
	print("hummmm")
	print("que ruim")
	print("reprovado")

	
eita
que bom
aprovado
>>> 
======== RESTART: Z:/1744888/Documents/10_06_2022/exemplo01.py ========
Informe sua média: 100
Informe sua frequência: 100
Aprovado!
>>> 
>>> 
>>> 
>>> 
>>> a,b,c,d = input().split()
5 6 7 8
>>> a
'5'
>>> b
'6'
>>> c
'7'
>>> d
'8'
>>> a = int(a)
>>> b = int(b)
>>> c = int(c)
>>> d = int(d)
>>> a
5
>>> b
6
>>> c
7
>>> d
8
>>> 
=========== RESTART: Z:/1744888/Documents/10_06_2022/1035.py ==========
5 6 7 8
valores nao aceitos
>>> 
=========== RESTART: Z:/1744888/Documents/10_06_2022/1035.py ==========
2 3 2 6
valores aceitos
>>> 