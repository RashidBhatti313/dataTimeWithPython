#                    DIAMOND PATTERN:

row = int(input("Enter the value of rows: "))
for i in range(row):
    print(" "*(row-i)+" *"*(i+1))

for j in range(row-1):
    print(" "*(j+2)+" *"*(row-1-j))

#                       R PATTERN:

# for row in range(7):
#     for col in range(5):
#         if col==0 or ((col == 4 and (row != 0 and row != 5)) or (row == 0 or row == 3) and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
