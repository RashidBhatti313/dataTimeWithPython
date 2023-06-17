# line1 = 'Welcome to UIT.....learning world of python!'
# line2 = 'Aslam o alaikum, my dear students'
# print(line1)
# print(line2)

# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# line1 = 'Hello ' + first+'  ' + last+'  '
# print(line1)
# print('Welcome to the world of python!')

# x = input('enter the value of x :')

# temp = eval(input("Enter the current of temp: "))

# if temp > 86:
#     print('It is Hot')
#     print('Be sure to drink liquids')
#     print('Goodbye.')




# #               PRACTICE PROBLEM 3.1

# #Question no 01:
# age = eval(input("enter the age: "))
# if age > 62:
#     print('You can get your pension benefits')
# #Question no 02:
# name = input("enter any name:")
# lst = ["Rashid" , "Ali" , "Waqas" , "Asif" , "Kashif"]
# if name in lst:
#     print('One of the top five')
# #Question no 03:
# hits = eval(input("enter the Hits: "))
# shield = 0
# if hits > 10 and shield == 0:
#     print("You are dead")
# #Qestion no 04:
# East = True
# North = False
# South = False
# West = False
# if East or North or South or West :
#     print( "I can escape")


#                   [LECTURE 02:]

# temp = eval(input("Enter the current temp: "))
# if temp > 86:
#     print('It is Hot')
#     print('BE sure to drink liquid')
# else:
#     print('It is not hot')
#     print('Bring a jacket')
# print('Goodbye')

name = input("Enter the name: ")
print('The word spelled out: ')
for char in name:
    print(char)

# animals = ['fish','dog','cat']
# for animal in animals:
#     print(animal)
# print("This program will seperate the vowels from the given sentence")
# phrase = input("Enter the phrase: ")
# for c in phrase:
#     if c in 'AEIOUaeiou':
#         print(c)

# print("Following program will print the values from 0 to 4")
# for i in range(7):
#     print(i)

# print("Following program will print the value starts from 0 to 4")
# for i in range (2,5):
#     print(i)

# print("Following program will print the value starts from 1 to 13 with gap of 3")
# for i in range (1,14,3):
#     print(i) 



#                               PRACTICE PROBLEM 3.3:

# year = eval(input("Enter the year: "))
# if year % 4 == 0:
#     print('Could be leap year')
# else:
#     print("Definitly not a leap year")


#                               PRACTICE PROBLEM 3.4:

# list = ['jeo','sue','hani','sophie']
# user = input("Login: ")
# if user in list:
#     print('You are in!')
# else:
#     print("Unknown")
# print('Done')

#                               PRACTICE PROBLEM 3.5:

# list = ['stop','desktop','top','post']
# for word in list:
#     if len(word) == 4:
#         print(word)

# list = ['stop','desktop','top','post']
# for word in list:
#     if len(word) == 4:
#         print(word)

#                               PRACTICE PROBLEM 3.6:

# for i in range (0,10):
#     print(i)

# for i in range (0,2):
#     print(i)

#                               PRACTICE PROBLEM 3.7:

# for i in range (3,13):
#     print(i)

# for i in range (0,10,2):
#     print(i)

# for i in range (0,24,3):
#     print(i)

# for i in range (3,50,5):
#     print(i)

#                               PRACTICE PROBLEM 3.8:

# l = int(input ("Enter the value of l: "))
# w = int(input ("Enter the value of w: "))
# p = ((l + w) * 2)
# print(p)


#                               PRACTICE PROBLEM 3.9:
# Rashid = 43
# Kashif = 45
# av = (Rashid + Kashif)/2
# print(av)

# s = 2
# r = 3.5
# av = (s + r)/2
# print(av)

#                               PRACTICE PROBLEM 3.10:


#                               PRACTICE PROBLEM 3.11:

# def alleven(x):
#     i = 0
#     re = True
#     while(i<= len(x)):
#         if i%2 == 0:
#             return re
#         i +=1
#     return False
# print(alleven([2,4,6,8]))

# def alleven(x):
#     i = 0
#     re = False
#     while(i<= len(x)):
#         if i%2 == 0:
#             return re
#         i +=1
#     return True
# print(alleven([2,3,4,5,6]))
#                               PRACTICE PROBLEM 3.12:




#                                   [LECTURE 03: ]
# def f(x):
#     res = x**2 + 1
#     return res

# print(f(4))


# def dum(x,e,r,y):
#     return x+e+r+y
# print(dum(5,5,6,5))

# def squareSum(x, y):
#     return x**2 + y**2
# print(squareSum(5,7))


# def hello(name):
#      print('Hello'+name +'!')
# hello("Rashid")

# def f(x):
#     print(x**2+1)


# s =input("Enter the square or Cube: ")
# if s == 'square':
#     def f(x):
#         return x*x
#     print(f(2))
# else:
#     def f(x):
#         return x*x*x
#     print(f(3))

# def f(x):
#     return x**2+1
# print(f(3))

# def g(x):
#     return f(x)
# def f(x):
#     return x**3

# print(g(4))

# def g(y):
#     return f(y)
# def f(x):
#     return x**2+1

# print(f(4)) 

# def f(x):
#     res = x**2+1
#     return res
# print(f(3))

# def g(x):
#     res = x**3+1
#     return res 
# print(g(4))