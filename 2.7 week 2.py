Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pets=['goldfish','cat','dog']
pets
['goldfish', 'cat', 'dog']
pets[l]='cymricat'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pets[l]='cymricat'
NameError: name 'l' is not defined
pets[1]
'cat'
pets[1]='cymricat'
pets
['goldfish', 'cymricat', 'dog']
myCat='cymricat'
myCat[7]='c'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myCat[7]='c'
TypeError: 'str' object does not support item assignment
myCat[7]
't'
myCat='Cymric Cat'
myCat
'Cymric Cat'
days=('Monday','Tuesday','Wednessday')
days
('Monday', 'Tuesday', 'Wednessday')
days=('Monday','Tuesday','Wednessday','Thursdsy')
days
('Monday', 'Tuesday', 'Wednessday', 'Thursdsy')
'friday' in days
False
'monday' in days
False
'Monday' in days
True
week=('friday','saturday','sunday')
week
('friday', 'saturday', 'sunday')
week=days
week
('Monday', 'Tuesday', 'Wednessday', 'Thursdsy')
week+days
('Monday', 'Tuesday', 'Wednessday', 'Thursdsy', 'Monday', 'Tuesday', 'Wednessday', 'Thursdsy')
days+week
('Monday', 'Tuesday', 'Wednessday', 'Thursdsy', 'Monday', 'Tuesday', 'Wednessday', 'Thursdsy')
days=('mo','tu','we','th')
week=days+('fr','sa','su')
week
('mo', 'tu', 'we', 'th', 'fr', 'sa', 'su')
len(week)
7
2*week
('mo', 'tu', 'we', 'th', 'fr', 'sa', 'su', 'mo', 'tu', 'we', 'th', 'fr', 'sa', 'su')
days[2]
'we'
days[3]
'th'
days[0]
'mo'
pets.
SyntaxError: incomplete input
pets.append('duck')
pets
['goldfish', 'cymricat', 'dog', 'duck']
pets.append('dog')
pets
['goldfish', 'cymricat', 'dog', 'duck', 'dog']
pets=['goldfish','cat','dog')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
pets=['goldfish','cat','dog']
pets.append9('duck')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    pets.append9('duck')
AttributeError: 'list' object has no attribute 'append9'. Did you mean: 'append'?
pets.append('duck')
pets.append('dog')
print(pets)
['goldfish', 'cat', 'dog', 'duck', 'dog']
pets.count('dog')
2
pets.remove('dog')
print(pets)
['goldfish', 'cat', 'duck', 'dog']
type([1,2,3,4,5,6,7,8,9])
<class 'list'>
type(3)
<class 'int'>
type(3.0)
<class 'float'>
type('Hello World')
<class 'str'>
s=3
type(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
type(s)
<class 'int'>
a =[3,5,6,7]
a[3]=8
a
[3, 5, 6, 8]
b =(2,4,5)
b[1]=3
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b[1]=3
TypeError: 'tuple' object does not support item assignment
grades=[9,7,7,10,3,9,6,6,2]
grades[1]
7
grades[7]
6
grades[1,2]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    grades[1,2]
TypeError: list indices must be integers or slices, not tuple
grades[2]
7
grades[5]=4
grades
[9, 7, 7, 10, 3, 4, 6, 6, 2]
max(grades)
10
sum(grades)/9
6.0
av
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    av
NameError: name 'av' is not defined. Did you mean: 'a'?
>>> av = (grades)/9
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    av = (grades)/9
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> av =sum(grades)/
SyntaxError: incomplete input
>>> av = sum(grades)/9
>>> av
6.0
>>> grages.sort()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    grages.sort()
NameError: name 'grages' is not defined. Did you mean: 'grades'?
>>> grades.sort()
>>> grades
[2, 3, 4, 6, 6, 7, 7, 9, 10]
>>> 2+3==4 or a>=5
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    2+3==4 or a>=5
TypeError: '>=' not supported between instances of 'list' and 'int'
>>> 2+3==4
False
>>> a=2+3==4
>>> a
False
>>> 2+3==4 or a>=5
False
>>> lst[1]*-3<-10==0
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    lst[1]*-3<-10==0
NameError: name 'lst' is not defined. Did you mean: 'list'?
>>> 2*3**2
18
>>> 4\2 in [1,2,3]
SyntaxError: unexpected character after line continuation character


