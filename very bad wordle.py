import random
word_list = ["plane","stone","phone"]
word = random.choice(word_list)
guesses = ''
game_over = True
while game_over := True:
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
    guess = input(" guess a character: ")
    guesses += guess