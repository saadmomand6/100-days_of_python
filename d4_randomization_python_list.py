# DAY 4

# # //////////////////RANDOMIZATION AND PYTHON LIST/////////

# EXCERCISE 4.1 :: HEAD OR TAIL//////////
# import random
# coin = random.randint(0,1)
# if coin == 1:
#     print("head")
# else:
#     print("tail")

# EXCERCISE 4.2 :: LIST :: CHOOSE RANDAM NAME TO PAY BILL//////////
# import random
# list_0f_names = ['saad', 'mulla', 'qan', 'lg']

# selected_name = random.choice(list_0f_names)
# print(f"{selected_name} has to pay the bill")

# # to split list
# names = list_0f_names.split(", ")
# print(names)

# EXCERCISE 4.3 :: LIST/ RANDOM :: TREASURE MAP GAME//////////
# row1= ['💼', '💼' , '💼']
# row2= ['💼', '💼' , '💼']
# row3= ['💼', '💼' , '💼']
# map = [row1, row2, row3]
# print(f"{row1},\n{row2},\n{row3}")
# position = input("where do you want to put treasure? (Choose row and column) ")
# horizontal= int(position[0])
# vertical= int(position[1])
# selected_row = map[vertical - 1][horizontal - 1] = "👑"
# print(f"{row1},\n{row2},\n{row3}")


# EXCERCISE 4.4 :: ROCK PAPER SISSOR GAME//////////
import random
rock = 1
paper = 2
sissor =3
obj = int(input("choose 1 for rock, 2 for paper, 3 for sissor?  "))
print(obj)
if obj == rock:
    print("you choose rock")
elif obj == paper:
    print("you choose paper")
else:
    print("you choose sissor")
print("computer choose")
computer_choice = random.randint(1,3)
print(computer_choice)
if computer_choice == rock:
    print("computer choose rock")
elif computer_choice == paper:
    print("computer choose paper")
else:
    print("computer choose sissor")

if obj == rock and computer_choice == sissor:
    print("you won")
elif obj == rock and computer_choice == paper:
    print("you lose")
elif obj == paper and computer_choice == rock:
    print("you win")
elif obj == paper and computer_choice == sissor:
    print("you lose")
elif obj == sissor and computer_choice == rock:
    print("you lose")
elif obj == sissor and computer_choice == paper:
    print("you win")
else:
    print("match drow")

