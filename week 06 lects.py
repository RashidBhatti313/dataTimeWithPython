#               METHOD DEBUGGING YOUR CODE

# number = 3
# print(number)
# for i in range(1,3):
#     number = number + 5
#     print(number)
# print("?")

#QUESTION 01:
# global = 1
# print("The output will be: ",global)


#QUESTION 02:
# emailgmail = input("Enter your email address : ")
# print("My email address is: ", emailgmail)

#QUESTION 03:
# print("In python, what do you call a 'box' used to store data? ")
# answer = input()
# if answer == "variable":
#     print(" :) " * 100)
# print("Thank you for playing!")

#QUESTION 04:
# print("Q1 - In python, what do you call a 'box' used store data? \n a - text \n b - variable \n c - a shoe box")
# answer = input().lower()
# if answer == "a":
#     print("Nope - text is a type of data:(")
# elif answer == "b":
#     print("Correct!:) ")
# elif answer == "c":
#     print("Dont be silly!:(")
# else:
#     print("You didn't choose a,b or c:( ")
    
#QUESTION 05:
# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

#QUESTION 06:
# if True:
#     print('Hello')
#     a = 5

#QUESTION 07:
# a = 0b1010
# b = 100
# c = 0o310
# d = 0x12c
# float_1 = 10.5
# float_2 = 1.5e2
# x = 3.14j
# print(a,b,c,d)
# print(float_1,float_2)
# print(x, x.imag, x.real)

#QUESTION 08:
# a = 0b1010
# b = 100
# c = 0o310
# d = 0x12c
# float_1 = 10.5
# float_2 = 1.5e2
# x = 3.14j
# print(a*b, b//c , c^d, d**a)

#QUESTION 09:
# drink = "Available"
# food = None
# def menu(x):
#     if x == drink:
#         print(drink)
#     else:
#         print(food)
# menu(drink)
# menu(food)

#QUESTION 10:
# a = 5
# print(a, "Is type of", type(a))
# a = 2.0
# print(a, "Is type of", type(a))
# a = 1+2j
# print(a, "a is complex number?", isinstance(1+2j, complex))

#QUESTION 11:
# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("positive numbers")
# else:
#     print("Negative numbers")

# OR
# a = int(input("Enter a number: "))
# def checknumber (num):
#     if num >= 0:
#         if num == 0:
#             print("Zero")
#         else:
#             print("Positive number")
#     else:
#         print("Negative number")

# checknumber (a)

#QUESTION 12:
genre = ['pop','rock','jazz']
for i in range(len(genre)):
    print("I like", genre[i])
