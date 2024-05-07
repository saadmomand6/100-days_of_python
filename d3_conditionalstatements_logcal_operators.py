# DAY 3

# # //////////////////CONDITIONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCKS/////////

# IF / ELSE
# height = int(input("whats' your height ? "))
# if height >=120:
#     print("youu are taller")
# else:
#     print("ypu are shorter")


# /////////////EXERCISE 3.1 ::  check even or odd ///////////
# numb = int(input("choose number ? "))
# if numb % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# ////////// AND OR STATEMENTS IN IF/ELSE////////////

# height = int(input("whats' your height ? "))
# age = int(input("whats' your age ?"))

# if height <=100 and age >=18:
#     print("you are adult")
# elif height <= 60 and age >= 12:
#     print("you are teenage")
# elif height <= 30 and age >= 8:
#     print("you are young")
# else:
#     print("you are baby")


# ////////// AND OR STATEMENTS IN IF/ELSE:: TO CHECK A LEAP YEAR////////////
# year = int(input("whats' year ?"))
# if year % 4==0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("it is leap year")
#         else:
#             print("not leap year")
#     else:
#         print("this is leap year")
# else:
#     print("not a leap year") 

# ////////// LOVE CALCULATOR////////////

# your_name = input("whats' your name ?")
# her_name = input("whats' her name ?")
# both_name = your_name + her_name
# lowercase_names = both_name.lower()
# t= lowercase_names.count('t')
# print(f't {t}')
# r= lowercase_names.count('r')
# print(f'r {r}')
# u= lowercase_names.count('u')
# print(f'u {u}')
# e= lowercase_names.count('e')
# print(f'e {e}')
# true = t + r + u + e
# l= lowercase_names.count('l')
# print(f'l {l}')
# o= lowercase_names.count('o')
# print(f'o {o}')
# v= lowercase_names.count('v')
# print(f'v {v}')
# love = l + o + v
# love_score = str(true) + str(love)
# print(love_score)


# ////////// TREASURE ISLAND STORY GAME////////////

# print("WELCOME TO TREASURE ISLAND")
# decision1  = input("want to take left or right")
# if str(decision1) == "left":
#     decision2 = input("want to swim or wait")
#     if decision2 == "wait":
#         decision3 = input("choose a door : yellow , red , blue")
#         if decision3 == "yellow":
#             print("you win")
#         else:
#            print("games over") 
#     else:
#         print("gamess over")
# else:
#     print("gamesss over")
