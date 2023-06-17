#                      CALCULATING THE AREA OF CYLINDER:
# r = int(input("Enter the value of r: "))
# h = int(input("Enter the value of h: "))
# A = (2)*(3.14)*r*h + (2)*(3.14)*r**2
# print(A)

#                          THE AREA OF TRIANGLE:
# l = int(input("Enter the value of l: "))
# w = int(input("Enter the value of w: "))
# A = (l * w)
# print(A) 

#            CALCULATE TEH ARTHIMATIC SEQUENCE OF N TERM:
# a1 = int(input("Enter the value of a1: "))
# n = int(input("Enter the value of n: "))
# d = int(input("Enter the value of d: "))
# an = (a1 + (n - 1)* d)
# print(an)

#                  CHECKING THE PALENDROM:
# string = input("Enter the string: ")
# print("Checking palendrom")
# if string == string[::-1]:
#     print("Its palendrom")
# else:
#     print("It is not palendrom")

#              FIRST LAW OF MOTION:
# Vi = int(input("Enter the value of Vi: "))
# a = int(input("Enter the value of a: "))
# t = int(input("Enter the value of t: "))

# def firstEquationOfMotion(a,t,Vi):
#     Vf = (Vi + (a)*(t))
#     return Vf
# print(firstEquationOfMotion(a,t,Vi))

#                SECOND LAW OF MOTION: 
# Vi = int(input("Enter the value of Vi: "))
# t = int(input("Enter the value of t: "))
# a = int(input("Enter the value of a: "))

# def SecondEquationOfMotion(a,t,Vi):
#     S = ((Vi)*(t) + 0.5* (a)*(t**2))
#     return S
# print(SecondEquationOfMotion(a,t,Vi))

#              THIRD LAW OF MOTION:
Vi = int(input("Enter the value of Vi: "))
Vf = int(input("Enter the value of Vf: "))

def ThirdEquationOfmotion(Vi,Vf):
    TwoaS = (Vi**2) - (Vf**2)
    return TwoaS
print(ThirdEquationOfmotion(Vi,Vf)) 

#                     PROJECTILE MOTION:



