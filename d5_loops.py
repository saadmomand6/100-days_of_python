# DAY 5

# # ////////////////// LOOPS /////////
# //////FOR LOOP ////////
# /////EXSERCISE 5.1 :: AVERAGE OF LIST OF HEIGHTS ////////
# list_of_heigths = [10,102,99,82,115,141,120,130,123,108]
# avg = 0
# lengt = 0
# for h in list_of_heigths:
#     avg += h
#     lengt +=1
# avg = avg / lengt
# print(avg)

# /////EXSERCISE 5.2 :: HEIGHEST SCORE ////////
# list_of_score = [100,102,99,82,115,141,120,130,123,108]
# highets_score = 0
# for s in list_of_score:
#     if s > highets_score:
#         highets_score = s
# print(f"highest score is : {highets_score}")

# //////RANGE IN FOR LOOP ////////
# range(start, end(will not be included), steps)
# for i in range(1,10):
#     print(i)
# for i in range(1,10,3):
#     print(i)

# ///////ADD 1 TO 100 NUMBERS //////
# total = 0
# for i in range(0,101):
#     total += i
# print(total)

# ///////ADDING EVENS TILL 100 //////
# total = 0
# for i in range(0,101,2):
#     total += i
# print(total)


# /////EXSERCISE 5.3 :: FIZZ BUZZ ////////
for num in range(0,101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0 :
        print("buzz")
    else:
        print(num)