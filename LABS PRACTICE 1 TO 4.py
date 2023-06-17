# LAB 01:
#                                      PROGRAM NUMBER 01:
# x = 2
# y = 4
# sum = x + y
# av = sum/2
# print(av)
#                                      PROGRAM NUMBER 02:
# w = int(input("Enter the value of w: "))
# h = int(input("Enter the value of h: "))
# area = (w * h)
# print(area)
#                                PROGRAM NUMBER 03:
# name = input("Enter your name: ")
# age = int(input("How old are you: "))
# year = str((2023 - age)+100)
# print(name + " You will be age 100 old in the year " + year)

#                                      PROGRAM 04: 
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#                                PROGRAM 05:
# import datetime
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

#                                       PRAGRAM 06: 
# c = int(input("Input the value of c: "))
# r = (c /2*3.124)
# print(r)

#                                        PROGRAM 07: 
# First_name = input("Enter your first name: ")
# Last_name = input("Enter last name: ")
# print("Hello " + First_name+" "+ Last_name)

#                                    PROGRAM NUMBER 08:
# import calendar
# y = int(input("Enter the year: "))
# m = int(input("Enter the month: "))
# print(calendar.month(y , m))

# PROGRAMMING EXERCISE:
 
# c=int(input("Enter the value of c:"))
# print((9/5)*c+32)
# f=int(input("Enter the value of f:"))
# print((f-32)*5/9)
# l=int(input("Enter the value of l:"))
# w=int(input("Enter the value of w:"))
# print(l*w)
# r=int(input("Enter the value of r:"))
# print(((4/3)*3.142)*r**3)
# name='M RASHID BHATTI'
# print("The given name is :",name)
# print("The name is title case is:",name.title())
# print("The name is lower case is:",name.lower())
# print("The name is upper case is:",name.upper())

# LAB 02:
#                                  PROGRAM 01:
# orignal_list1 = [10,22,44,23,4]
# new_list2 = list(orignal_list1)
# print(orignal_list1)
# print(new_list2)

#                                  PROGRAM 02: 
# x = ()
# print(x)
# tuple1 = tuple()
# print(tuple1)

#                               PROGRAM 03:
# tuple2 = ("tuple",False,3.2,1)
# print(tuple2)

#                          PROGRAM 04:
# tuplex = ("U","I","T","2","0","2","3","a","b","t","h")
# print(tuplex)
# item = tuplex[3]
# print(item)
# item1 = tuplex[-4]
# print(item1)

#                             PROGRAM 05:
# lst = [2,3,4]
# lst.extend([5,6])
# print(lst)
# lst2 = lst.copy()
# print(lst2)
# # lst.clear()
# # print(lst)
# # print(lst2)

# # PROGRAMMING EXERCISE: 

# # import datetime



# # LAB 03:
# #                                    PROGRAM 09:
# import math
# velocity = float(input("Give me to velocity to fire (in m/s): "))
# angle = float(input("Give to angle at a fire: "))
# distance = float(input("Give me how far away you are from the structure: "))
# heigth = float(input("Give me the heigth of the structure (in meters): "))


#
l = []
for i in range(21):
    i = int(input(f"enter {i} no"))
    l.append(i)


print(l)
ne = []
p =[]
even = []
o = []
for i in l:
    if i> 0:
        p.append(i)
    if i<0:
        ne.append(i)
    if i%2 ==0:
        even.append(i)
    else:
        o.append(i)

print(ne)
print(p)
print(even)
print(o)
print(len(ne))
print(len(p))
print(len(even))
print(len(o))

