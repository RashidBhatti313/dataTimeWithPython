#                       PROGRAM 01:
# count = 3
# f = eval(input("Enter your final condition where you want to break the loop: "))
# while(count < f):
#     print("The value of count: ", count)
#     count = count+1
#     print("I am using while loop", count, "time.")
#                       PROGRAM 02:
# var = 1
# while var == 1:  #This will generate an infinity loop, as condition is always true
#     num = eval(input("Enter a number: "))
#     print("You entered:",num)
# print("End of loop!")

#                        PRAGRAM 03:
# n = eval(input("Enter the value of execute the while loop: "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum+i
#     i = i+1
# print("The sum is", sum)

#                        PORGRAM 04:
# i = 0
# f = 10
# while i<f:
#     print(i, "is less than final condition")
#     i = i+1
# else:
#     print(i, "Is not less than final condition")

#                       PROGRAM 05:
# def f(x):
#     res = x**2 + 1
#     return res

# print(f(3))

#                       PROGRAM 06:
def CubeValues():
    lst = list()
    for i in range(1,31):
        lst.append(i**3)
    print(lst[:6])
    print(lst[-6])
CubeValues()

#                       PROGRAM 07:
def caesar_enerypt(realText, step):
    outtext = []
    crypttext = []

    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            crypttext.append(crypting)
            newLetter = uppercase[crypting]
            outtext.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            crypttext.append(crypting)
            newLetter = lowercase[crypting]
            outtext.append(newLetter)
    return outtext
print(caesar_enerypt("Arshad", 5))

