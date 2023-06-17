Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+2+3+4+5
15
(23+19+31)/3
24.333333333333332
403//73
5
403%73
38
2**10
1024
abs(54-57)
3
min(34.99,29.95,31.50)
29.95
2+2<4
False
7//3==1+1
True
3**2+4**2==25
True
2+4+6>12
False
1387%19==0
True
31%2==0
False
min(34.99,29.95,31.50,30.00)
29.95
min(34.99,29.95,31.50)<30.00
True
a=3
b=4
c=a*a+b*b
c
25
a+b+c
32
s1='ant'
s2='bat'
s3='cod'
s1+ ''+s2+ ''+s3
'antbatcod'
10 * (s1 + '')
'antantantantantantantantantant'
s1 + '' + 2 * (s2 + '') + 2 * (s3 + '') + s3
'antbatbatcodcodcod'
7*(s1+' '+s2+' ')
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
3*(2 * s2+s3+' ')
'batbatcod batbatcod batbatcod '
s[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[0]
NameError: name 's' is not defined. Did you mean: 's1'?
s=[1,2,3,4,5,6,7,8,9]
s[0]
1
s[]1
SyntaxError: invalid syntax
s[1]
2
s[6]
7
s[8]
9
s[9]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s[9]
IndexError: list index out of range
min(words)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    min(words)
NameError: name 'words' is not defined
>>> min(s)
1
>>> max(s)
9
>>> grades=[9,7,7,10,3,9,6,6,2]
>>> grades.count(7)
2
>>> grades[-1]=4
>>> grades=[-1]
>>> 4
4
>>> grades
[-1]
>>> grades=[9,7,7,10,3,9,6,6,2]
>>> max(grades)
10
>>> grades.sort()
>>> grades.sort(4)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    grades.sort(4)
TypeError: sort() takes no positional arguments
>>> grades.sort
<built-in method sort of list object at 0x0000020BB3173D40>
>>> sum(grades)
59
>>> len(grades)
9
>>> grades.sorted()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    grades.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> grades.sort()
>>> grades
[2, 3, 6, 6, 7, 7, 9, 9, 10]
>>> 59/9
6.555555555555555
