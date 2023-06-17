Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(-4)
4
abs(4)
4
abs(-3.2)
3.2
min(6,-2)
-2
max(6,-2)
6
min(2,-4,6,-2)
-4
max(12,26.5,3.5)
26.5
2<3
True
3<2
False
5-1>2+1
True
3==3
True
3+5==4+4
True
3==5-3
False
3=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
3<=4
True
3>=4
False
3!=4
True
2<3and4>5
SyntaxError: invalid decimal literal
2<3 and 4>5
False
2<3 and true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    2<3 and true
NameError: name 'true' is not defined. Did you mean: 'True'?
2<3 and True
True
3<2 or 2<1
False
3<4 or 4<3
True
not (3<4)
False
x=4
x
4
x=Rashid Bhatti
SyntaxError: incomplete input
x=Rashid
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x=Rashid
NameError: name 'Rashid' is not defined
x=1234
x
1234
x=7
x
7
x==7
True
x==5
False
'Hello World!'
'Hello World!'
s='hello'
s
'hello'
s=='hello'
True
s=='World'
False
h='World'
>>> h
'World'
>>> s+h
'helloWorld'
>>> s + h
'helloWorld'
>>> s' + 'h
SyntaxError: invalid syntax
>>> s+' '+h
'hello World'
>>> s!=h
True
>>> s==h
False
>>> 'hello' * 'world'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    'hello' * 'world'
TypeError: can't multiply sequence by non-int of type 'str'
>>> 3*'A'
'AAA'
>>> 'hello'* 2
'hellohello'
>>> "hello" * 3
'hellohellohello'
>>> 'hello ' * 4
'hello hello hello hello '
>>> 30*'-'
'------------------------------'
>>> 30*' 30 '
' 30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30  30 '
>>> s='hello"
SyntaxError: incomplete input
>>> s='hello'
>>> 'h' in s
True
>>> 'g' in s
False
abs(-4)
4
