Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1='ant'
>>> s2='bat'
>>> s3='cod'
>>> s1+' '+s2+' '+s3
'ant bat cod'
>>> (s1+' ')* 8
'ant ant ant ant ant ant ant ant '
>>> (s1+' ')+(s2+' ')* 2+(s3+' ')* 3
'ant bat bat cod cod cod '
>>> (s1+' '+s2)* 5
'ant batant batant batant batant bat'
>>> (s1+' ' +s2)* 5
'ant batant batant batant batant bat'
>>> (s1+' ') + (s2)* 5
'ant batbatbatbatbat'
>>> (s1+' ') + (s2+' ')* 5
'ant bat bat bat bat bat '
>>> ((s1+' ') + (s2+' '))* 5
'ant bat ant bat ant bat ant bat ant bat '
>>> (s1+s2+s3)* 4
'antbatcodantbatcodantbatcodantbatcod'
>>> (s1+s2+s3+' ')* 4
'antbatcod antbatcod antbatcod antbatcod '
>>> ((s2+'')* 2) + (s3)
'batbatcod'
>>> (((s2+'')* 2) + (s3))* 4
'batbatcodbatbatcodbatbatcodbatbatcod'
>>> (((s2+'')*2) + (s3+' '))*4
'batbatcod batbatcod batbatcod batbatcod '
>>> (((s2+'')*2) + (s3+' '))*4
