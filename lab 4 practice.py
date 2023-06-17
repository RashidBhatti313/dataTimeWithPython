#                                       PRAGRAM 01:
# a = 400
# b = 500
# if a == 400:
#     print("The value of a is equal to 400 ")
# if a < b:
#     print("The value of a is less to b ")
# if a > b:
#     print("The value of a is greater than b ")

# a = 500
# b = 400
# if a != b:
#     print("The value of is equal to 500 ")
# if a <= b:
#     print("The value of is less or equal to than b ")
# if a >= b:
#     print("The value of is greater or equal to than b ")

#                                        PROGRAM 02:
# a = 10
# b = 5
# c = 20
# if a>b and c>b:
#     print("Both condition are True")

#                                        PROGRAM 03:

# a = 150
# b = 50
# c = 200
# if a > b or c > a:
#     print(True)
# else:
#     print(False)

#                                       PROGRAM 04:

# l_limit = int(input("Enter lower limit range: "))
# u_limit = int(input("Enter upper limit range: "))
# print("Prime number between",l_limit and u_limit)
# for number in range(l_limit,u_limit+1):
#     if number > 1:
#         for i in range(2,number):
#             if(number%i) == 0:
#                 break
#         else:
#              print(number)



# #                                       PROGRAM 05:

# initial_value = eval(input("Enter the initial value for range: "))
# final_value = eval(input("Enter the final value for range: "))
# numbers = range(initial_value,final_value)
# sum = 0
# for value in numbers:
#     sum = sum+value
# print("The sum is", sum)


#                                     List Comprehansion

# l = [ i for i in range(6) if i%2==0]
# for i in range(5):
#      if i % 2 == 0:
          
#         l.append(i)

# print(l)

# l = []
# for i in range(6):
#     if i % 2 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(6) if i % 2 == 0]
# print(l)
# l = [i for i in range(7) if i % 2 == 0]
# print(l)
# l = []
# for i in range(7):
#     if i % 2 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(9) if i % 2 == 0 ]
# print(l)
# l = []
# for i in range(9):
#     if i % 2 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(8) if i % 3 == 0]
# print(l)
# l = []
# for i in range(8):
#     if i % 3 == 0:
#         l.append(i)
# print(l)
# l = [i for i in range(8) if i % 3 == 0]
# print(l)
# l = [[0 for col in range(3)] for row in range(3)]
# print(l)
# [[0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0]]
# for row in range(3):
#     for col in range(3):
#         l[row][col] = row * col
# print(l)


# datalist = [300, 12.65, 5+6j, True, 'Faisal', (5, -7), [8, 52],{"color":'blue', "color":'red'}]
# for i in datalist:
#     print(type(i), end=" ")

# for code in range(0,256):
#     # print(chr(code), end=" ")
#     print(f"Deci {code} = binary {bin(code)} = Hexa {hex(code)}    octal {oct(code)}   chartar = {chr(code)}")
   
#                                      PROGRAM 06:

# row_num = int(input("Input number of row: "))
# col_num = int(input("Input number of col: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row * col
# print(multi_list)

#                                      PROGRAM 07:

# datalist = [300,12.56,2 + 3j, True, "Rashid", (5, -7),[8,52], {"color":"blue","color":"red"}]
# for i in datalist:
#     print(i, type(i))

#                                      PROGRAM 08:

# for code in range(65,91):
#     print(chr(code), end=" ")

# for i in range(0,256):
#     print(i, "=", chr(i), end="\t")
#     print("\n")

#                                      PROGRAM 09:

# for code in range(0,17):
#     print(f"Deci {code} = binary {bin(code)} = Hexa {hex(code)} octal {oct(code)} chartar = {chr(code)} ")

#         ASCII WORD:

for code in range(0,256):
    print(chr(code))

#                      pattern practice:
# for i in range(2,10,2):
#     for j in range(i):
#         print(i+j, end = " ")
#     print() # line break
# n = 5
# for i in range(n): # [ 0,1,2,3,4]
#     for j in range(i):
#         print("i", end=" ")
#     print()   
# for i in range(n,0,-1):
#     for j in range(i,):
#         print("i",end=" ")
#     print()

#                            PROGRAM 10:

n = 5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#                           PROGRAM 11:

# print("This program will count total number of vowelsfrom user defined sentences ")
# string = input("Enter your string: ")
# vowels = 0
# for i in string:
#     if (i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels=vowels+1
# print("Number of vowels")
# print(vowels) 

# s = " zaKAriya "
# c = 0
# for letter in s.lower():

#     if letter == 'a' or letter =='i'  or letter == 'e' or letter == 'u' or letter=='o':
#         c += 1
#         print(letter, c)
# print(c)

#                            PROGRAMMING EXERCISE:

# QUESTION NUMBER 01:
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c = int(input("Enter the value of c: "))
# x1 = (-b + (b**2 - (4*a*c))**0.5)/(2*a)
# x2 = (-b - (b**2 - (4*a*c))**0.5)/(2*a)
# print(x1,x2) 

# QUESTION NUMBER 02:
# a = int(input("Enter the value of a: "))
# n = int(input("Enter the value of n: "))
# d = int(input("Enter the value of d: "))
# an = (a + (n - 1) *d)
# print(an)

# QUESTION NUMBER 03:
# string = input("Enter the string: ")
# print("Checking palandrom")
# if string == string[::-1]:
#     print("Its palandrom")
# else:
#     print("It is not palandrom")

# QUESTION NNUMBER 04:
name = input("Enter name: ")
father_name = input("Enter father name: ")
Roll_number = input("Enter roll number: ")
sub = []
total_mark = 0
for i in range(1,6):
    sub_name = input(f"enter subject {i}name")
    sub_marks = int(input(f"enter {sub_name}  marks: "))
    total_mark += sub_marks
    sub.append((sub_name,sub_marks))
ave = total_mark/5
print(sub, total_mark, ave)

name = input("Enter name:  ")
father_name = input("Enter father name: ")
Roll_number = input("Enter roll number: ")
sub = []
total_mark = 0
for i in range(1,6):
    sub_name = input("enter subject name: ")
    sub_marks = int(input(f"enter {sub_name} marks: "))
    total_mark += sub_marks
    sub.append((sub_name,sub_marks))
av = total_mark/5
print(f"{sub}    , {total_mark},     {av}  ")