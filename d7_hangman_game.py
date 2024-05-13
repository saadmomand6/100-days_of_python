# DAY 7

# # ////////////////// HANGMAN GAME /////////
import random
words_list = ["mouse", "staires", "pet","gift", "turtle"]
selected_word = random.choice(words_list)
lives = 6
print(selected_word)
display = []
for d in selected_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("select a alphabet").lower()
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in selected_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You Lost")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win")
