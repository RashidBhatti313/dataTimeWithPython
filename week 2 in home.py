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
3<=3
True
3>=4
False
3!=4
True
2<3 and 4>5
False
2<3 and true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
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
x=7
x==
SyntaxError: incomplete input
x==7
True
x==4
False
'Heloo world'
'Heloo world'
'Hello world'
'Hello world'
s='hello'
s
'hello'
s=='hello'
True
s=='world'
False
h='World'
h
'World'
s+h
'helloWorld'
s+' '+h
'hello World'
s!=h
True
s==h
False
3*'A'
'AAA'
'hello'*2
'hellohello'
'hello '*4
'hello hello hello hello '
30*'-'
'------------------------------'
30*' 30'
' 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30'
'h' in s
True
'g' in s
False
len(s)
5
a=3
b=4
c=4
d=5
av = (a+b+c+d)/4
av
4.0
sara_age = 23
mark_age = 19
fatima_age = 31
av = (sara_age + mark_age + fatima_age)/3
av
24.333333333333332
73*4
292
403/73
5.52054794520548
73*5.52054794520548
403.0
2**10
1024
abs(54-57)
3
min(8922.45,7637.25,8032.5)
7637.25
max(8922.45,7637.25,8032.5)
8922.45
2+2>4
False
5/2
2.5
5//2
2
9/2
4.5
9//2
4
1/3
0.3333333333333333
1//3
0
7//3==1+1
True
3**2
9
4**2
16

3**2+4**2==25
True
45**6+7**2-58
8303765616
2+4+6<12
False
1387/19
73.0
31/2
15.5
int
<class 'int'>
3
3
a=3
a
3
b=4
a*a+b*b
25
s1='ant'
s2='bat'
s3='cod'
s1+' '+s2+' '+s3
'ant bat cod'
(s1+' ')* 8
'ant ant ant ant ant ant ant ant '
(s1+ ' ')+(s2+' ')*2+(s3+' ')*3
'ant bat bat cod cod cod '
(s1+' ') + (s2+' ')*5
'ant bat bat bat bat bat '
((s1+' ') + (s2+' '))*5
'ant bat ant bat ant bat ant bat ant bat '
(((s2+'')*2) + (s3+' '))*4
'batbatcod batbatcod batbatcod batbatcod '
s='hello'
s[0]
'h'
s[]1
SyntaxError: invalid syntax
s[1]
'e'
s[-2]
'l'
pets=['goldfish','cat','dog']
pets
['goldfish', 'cat', 'dog']
pets[0]
'goldfish'
pets[2]
'dog'
len(pets)
3
pets + pets
['goldfish', 'cat', 'dog', 'goldfish', 'cat', 'dog']
>>> pets*2
['goldfish', 'cat', 'dog', 'goldfish', 'cat', 'dog']
>>> rabbit in pets
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    rabbit in pets
NameError: name 'rabbit' is not defined
>>> 'rabbit' in pets
False
>>> 'dog' in pets
True
>>> lst=[23.99,19.99,34.50,120.99]
>>> min(lst)
19.99
>>> max(lst)
120.99
>>> sum(lst)
199.46999999999997
>>> s='01345689'
>>> s[5]
'6'
>>> s[]2
SyntaxError: invalid syntax
>>> s[-4]
'5'
>>> words=['bat','ball','barn','barn','basket','football]
...        
SyntaxError: incomplete input
>>> words=['bat','ball','barn','barn','basket','football']
...        
>>> words
...        
['bat', 'ball', 'barn', 'barn', 'basket', 'football']
>>> 4
...        
4
>>> len(words)
...        
6
