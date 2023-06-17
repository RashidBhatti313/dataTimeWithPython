# tem =float(input("enter temperature: "))
# if tem > 86:
#     print("Its Too Hot baby")
#     print("You should drink some cold ")
# print("End") 
# tem =float(input("enter temperature: "))
# if tem > 86:
#     print("Its Too Hot baby")
#     print("You should drink some cold")
# else:
#         print("Its not too hot")
# print("End")

# answer = input ("Do you agree: ")
# if answer == 'yes' :
#     print("Agreed")
# else:
#     print("Not Agree")

# using .string () method for removing last spaces 

# answer = input ("Do you agree: ").strip().lower()
# if answer == 'yes' or answer =='y' :
#     print("Agreed")
# else:
#     print("Not Agree")

answer = input ("Do you agree: ").strip().lower()
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not Agree")