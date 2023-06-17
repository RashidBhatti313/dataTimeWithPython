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
min(2,26.5,3.5)
2
max(12,-4,6,-2)
12
2<3
True
3>2
True
5-1>2+1
True
3==3
True
3+5==4+4
True
3==5-3
False
3<=4
True
3>=4
False
3!=4
True
2<3 and 4>5
False
2<3 and True
True
3<4 or 4<3
True
3<2 or 2<1
False
not(3<4)
False
x=4
x
4
x=7
x
7
x==7
True
x==4
False
'hello,World'
'hello,World'
s= 'hello'
s
'hello'
k='Kashif'
k
'Kashif'
h='world'
h
'world'
s+h
'helloworld'
k+h
'Kashifworld'
s+' '+h
'hello world'
s=='hello'
True
h='world'
h
'world'
s!=h
True
s==t
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s==t
NameError: name 't' is not defined
s==h
False
s+k+h
'helloKashifworld'
3*'A'
'AAA'
'hello'*2
'hellohello'
30 * ' 30'
' 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30'
'kashif' * 45
'kashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashifkashif'
'h' in s
True
'll' in s
True
len(s)
5
len(k)
6



Practice
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Practice
NameError: name 'Practice' is not defined
2+4+6+8+10
30
15*8
120
1000*0
0
0.56*2
1.12
'sara'(23)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'sara'(23)
TypeError: 'str' object is not callable
sara_age = 23
mark_age = 19
fatima_age = 31
av = (sara_age + mark_age + fatima_age)/3
av
24.333333333333332
73*4
292
73*5
365
403/73
5.52054794520548
73*5.5205479
402.99999670000005
round(402.99)
403
2**10
1024
10**4
10000
15**5
759375
s+k
'helloKashif'
sara_age
23
sara_age+fatima_age
54
abs(54-57)
3
min($34.99,$29.95,$31.50)
SyntaxError: invalid syntax
34.99*270
9447.300000000001
2.95*270
796.5
31.50*270
8505.0
min(9447.30,796.5,8505.0)
796.5
2+2>4
False
5/2
2.5
5//2
2
1/3
0.3333333333333333
9/2
4.5
9//2
4
7//3
2
7//3=1+1
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
7//3==1+1
True
3**2
9
4**2
16
3**2==4**2
False
3**2+4**2==25
True
45**6+7**2-58
8303765616
2,4,6<12
(2, 4, True)
2+4+6<12
False
4+2+6>12
False
why
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    why
NameError: name 'why' is not defined
2+4+6>12
False
1387/19
73.0
31 is even
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    31 is even
NameError: name 'even' is not defined
31 is
SyntaxError: incomplete input
31
31
31/2
15.5
int
<class 'int'>
3
3
a
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'av'?
a=3

a
3
b=4
b
4
a*a+b*b
25
s1='ant'
s2='bat'
s3='cod'
s1+s2+s3
'antbatcod'
s1 + s2 + s3
'antbatcod'
s1+' '+s2+' '+s3
'ant bat cod'
s1 * '15'
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    s1 * '15'
TypeError: can't multiply sequence by non-int of type 'str'
s1* '15'
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    s1* '15'
TypeError: can't multiply sequence by non-int of type 'str'
'ant' * 15
'antantantantantantantantantantantantantantant'
15*' ant'
' ant ant ant ant ant ant ant ant ant ant ant ant ant ant ant'
'ant' +
SyntaxError: incomplete input
'ant+' '+bat'
'ant++bat'
s1+' '+s2
'ant bat'
s1+' '+s2*9
'ant batbatbatbatbatbatbatbatbat'
(s1+' '+s2+' '+s3) * 8
'ant bat codant bat codant bat codant bat codant bat codant bat codant bat codant bat cod'
>>> s1' 's2 * '2' 's3'
SyntaxError: invalid syntax
>>> s1+' '+s2* 2 's3'* 3
SyntaxError: invalid syntax
>>> 
>>> 'ant '85
SyntaxError: incomplete input
>>> (s1+' ')*5
'ant ant ant ant ant '
>>> s1+s2*2+s3*3
'antbatbatcodcodcod'
>>> s1+' '+s2*2+' 's3*3
SyntaxError: invalid syntax
>>> s1+' '+s2*2+' '+s3*3
'ant batbat codcodcod'
>>> s1+' '+s2 * 2+' '+s3 * 3
'ant batbat codcodcod'
>>> s1+' '+s2 '*'2
SyntaxError: invalid syntax
>>> s2 * '2'
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    s2 * '2'
TypeError: can't multiply sequence by non-int of type 'str'
>>> s2' *2
SyntaxError: incomplete input
>>> s2 '*2
SyntaxError: incomplete input
>>> s2 * '2'
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    s2 * '2'
TypeError: can't multiply sequence by non-int of type 'str'
>>> (s1+' ')+(s2+' ')*2+(s3+' ')*3
'ant bat bat cod cod cod '
>>> (s1+' ')+(s2+' ')*4
'ant bat bat bat bat '
