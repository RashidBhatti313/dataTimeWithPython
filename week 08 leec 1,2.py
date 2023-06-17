# sharks = ['hammerhead','great white','dogfish','frilled','bullhead','requiem']
# for item in range (len(sharks)):
#     sharks.append('shark')
# print(sharks)

# count = 0 
# while (count < 9):
#     print('The count is: ', count)
#     count = count + 1
# print("We love programming! ")

# for i in range(1,11):
#     for j in range(1,11):
#         k = i * j
#         print(k, end=" ")
#     print()

# i = 2
# while (i < 15):
#     j = 2
#     while (j <= (i/j)):
#         if not (i%j):
#             break
#         j = j + 1
#     if (j > i/j):
#         print(i, "is prime")
#     i = i + 1

# i = 2
# print("Line 1-> The value of i is: ", i)
# while (i<15):
#     print("Line 2-> The value of i < 15 is: ", i<15)

#     j = 2
#     print("Line 3-> The value of j is: ", j)

#     while(j <= (i/j)):
#         print("Line 4-> The value of j <= (i/j) is: ", j)
#         if not (i%j):
#             print("Line 5-> The value of not (i%j) is ", not(i%j))
#             break
#         j = j + 1
#         print("Line 6-> The value of j after j+1 = ", j)
#     if (j>i/j):
#         print("Line 7-> The value of j > i/j is: ", (j>i/j))
#         print(i, "is prime")
#     i = i + 1
#     print("Line 9-> The value of i after i = i + 1 is: ", i)

# for letter in 'python':
#     if letter == 'h':
#         break
#     print('Current Letter: ', letter)

# var = 10
# while var > 0:
#     print('Current variable value: ', var)
#     var = var - 1
#     if var == 5:
#         break

# print("Thanks for using this program!")

# def series (n):
#     a,b = 0, 1
#     for i in range(n-1):
#         a,b = b, a+b
#     return (a)
# for i in range(1,16):
#     print(series(i), end=" ")

# def print_rectangle(n, m):
#     for i in range (1, n+1):
#         for j in range (1, m+1):
#             if (i == 1 or i == n or j == 1 or j == m):
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# print_rectangle(6, 6)

# Tuple1 = tuple('Usman institute of technology')
# print("Removal of first element: ")
# print(Tuple1[1:])

# print("\nTuple after seqence of Element is reversed: ")
# print(Tuple1[::-1])

# print("\nPrinting elements between range 4-9: ")
# print(Tuple1[4:9])

        
# side = int(input("Please Enter any side of a square: "))
# print("square Star pattern")
# for i in range(side):
#     for i in range(side):
#         print('*', end=" ")
#     print()


# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         if j <= i:
#             print(j+1, end="")
#         j +=1
#     print("")
#     i +=1

# correctnumber = 5
# guess = 0 
# while guess != correctnumber:
#     guess = int(input("Guess the number: "))
#     if guess != correctnumber:
#         print("False guess")
# print("You guessed the correct number")

# correctnumber = 5
# guess = 0
# while guess != correctnumber:
#     guess = int(input("Guess the number: "))
#     if guess != correctnumber:
#         print('False guess')

# numBuildings = 2
# aptsperBuilding = 3
# aptnum = 1

# while aptnum <= aptsperBuilding:
#     month = 1
#     while month <= 12:
#         building = 1
#         while building <= numBuildings:
#             print("-Payment Coupon-------")
#             print("Building", building)
#             print("aptnum", aptnum)
#             print("Month:", month)
#             print("Rent Due:800 ")
#             print("----------------")
#             building = building + 1
#         month = month + 1
#     aptnum = aptnum + 1 

# print('You guess the correct number')

# c = 1
# while c < 5:
#     print(c, "This is inside of while loop")
#     c+=1
# else:
#     print(c, "This is outside of while loop")

# word = "Anaconda"
# pos = 0
# while pos < len(word):
#     print(word[pos])
#     pos+=1


# print("Printing multiples of 3 from 1 to 10")
# i = 1
# while i < 11:
#     print(3*i)
#     i = i + 1
# print("Rest of the program")

# i = 1
# while i < 11:
#     j = 0
#     while j < i:
#         print('*', end=" ")
#         j = j + 1
#     print()
#     i = i + 1
# print("Rest of the program")


# for name in ('Rafey','Rashid','Naeem','Kashif','Shahzeb'):
#     print(name, end=" CS Studenet")
#     print()

# i = 1
# j = 5
# while i < 4:
#     while j < 8:
#         print(i, ",", j)
#         j = j + 1
#         i = i + 1

num = eval(input("Enter the number to check: "))
if 9 < num < 99:
    print("Two digits number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number") 
else:
    print("number is <= 9 or >= 9999")