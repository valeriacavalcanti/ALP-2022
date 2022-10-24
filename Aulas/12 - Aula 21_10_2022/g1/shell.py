Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> letra = 'A'
>>> type(letra)
<class 'str'>
>>> letra
'A'
>>> ord(letra)
65
>>> ord('A')
65
>>> codigo = ord(letra)
>>> letra
'A'
>>> codigo
65
>>> bin(codigo)
'0b1000001'
>>> bits = '01000001'
>>> bits
'01000001'
>>> int(bits, 2)
65
>>> int(bits, 16)
16777217
>>> codigo = 48
>>> ord('A')
65
>>> chr(65)
'A'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 'TESTE' < 'CASA'
False
>>> '22' < '22'
False
>>> '22' == '22'
True
>>> '210' < '23'
True
>>> '230' < '23'
False
>>> '230' == '23'
False
>>> '230' > '23'
True
>>> 'TESTE' < '123'
False
>>> 'TESTE' < 'teste'
True
>>> ord('T')
84
>>> ord('t')
116
>>> 
>>> 
>>> 
>>> frase = input('Frase: ')
Frase: Eu adoro estudar Python! Em 2022 !!
>>> frase
'Eu adoro estudar Python! Em 2022 !!'
>>> 
>>> nome = 'Valéria'
>>> nome[0]
'V'
>>> nome[1]
'a'
>>> nome[2]
'l'
>>> nome[3]
'é'
>>> nom[4]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    nom[4]
NameError: name 'nom' is not defined
>>> nome[4]
'r'
>>> nome[6]
'a'
>>> len(nome)
7
>>> len(frase)
35
>>> frase
'Eu adoro estudar Python! Em 2022 !!'
>>> for i in range(len(frase)):
	print(i, frase[i], ord(frase[i]))

	
0 E 69
1 u 117
2   32
3 a 97
4 d 100
5 o 111
6 r 114
7 o 111
8   32
9 e 101
10 s 115
11 t 116
12 u 117
13 d 100
14 a 97
15 r 114
16   32
17 P 80
18 y 121
19 t 116
20 h 104
21 o 111
22 n 110
23 ! 33
24   32
25 E 69
26 m 109
27   32
28 2 50
29 0 48
30 2 50
31 2 50
32   32
33 ! 33
34 ! 33
>>> 