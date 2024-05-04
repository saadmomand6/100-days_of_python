# DAY 2

# # //////////////////PRINT FIRST ALPHABET OF STRING/////////
# print("hello"[0])


# # //////////////////EXCERSICE 2.1 = ADD DIGITS OF A NUMBER LIKE 45 => 4 + 5/////////
# number = input("write 2 digits number? ")
# sum = int(number[0]) + int(number[1])
# print(sum)

# # //////////////////EXCERSICE 2.1 = BMI CALCULATOR ////////////////
# height = float(input("your height in m: "))
# weight = float(input("your weight in kg: "))
# bmi = weight / (height ** 2)
# print(bmi)

# # //////////////////EXCERSICE 2.2 = YOUR LIFE IN WEEKS ////////////////
# age = input("current age ?  ")
# years_remaining = 63 - int(age)
# day_remaing = years_remaining * 365
# week_remaing = years_remaining * 52
# month_remaing = years_remaining * 12
# print(f"you have {day_remaing} days, {week_remaing} weeks , {month_remaing} months remaining")

# # //////////////////EXCERSICE 2.3 = TIP CALCULATOR ////////////////
bill = input("current bill ?  $")
no_of_person = input("number of person to split bill ?  ")
tip_percent = input("percentage of tip ?  10, 12 , 15 ")
tip_in_percent =  int(tip_percent) / 100
bill_amount_after_adding_tip = float(bill) + float(tip_in_percent)
amount_after_spliting_bill = float(bill_amount_after_adding_tip) / int(no_of_person)
amount_after_spliting_bill = int(amount_after_spliting_bill)
print(f"you have {amount_after_spliting_bill} to pay")