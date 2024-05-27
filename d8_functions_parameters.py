# DAY 8

# # ////////////////// Functions and parameters /////////
# //check the paint cans quantity
# height = int(input('what is height of wall'))
# width = int(input('what is width of wall'))
# number_of_cans = round((height * width) / 5)
# print(f"number of cans to paint wall are {number_of_cans}")

# //prime number checker
# def prime_number_checker(number):
#     number = int(input("select a number to check ??"))
#     if number % 2 == 0:
#         print(f"{number} is not a prime number")
#     else:
#         print(f"{number} is a prime number")
# prime_number_checker(5)

# /////CEASER CIPHER////////
alphabets = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def ceasercipher(normaltext, shift_num):
    ciphertext = ""
    if direction == 'decrypt':
        shift_num *= -1
    for letter in normaltext:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + shift_num
            new_letter = alphabets[new_position]
            ciphertext += new_letter
        else:
            ciphertext += letter
    print(f"the encrypted result is {ciphertext}")
    
    
again = True
while again == True:
    direction = input("for encryption write'encrpt' and for decryption writev 'decrypt'")
    text = input('write something').lower()
    shift = int(input('type the shift number  '))
    shift = shift % 26
    ceasercipher(normaltext=text,shift_num= shift)
    choice = input("want to do again ?  ")
    if choice == 'no':
        again = False
        print("good bye")

