import random
wordlist = ['plane','grass','jumbo']

def choose_word():
    return random.choice(wordlist)


def is_valid_guess(guess):
    return len(guess) == 5 and guess.islower()


def check_guess(target_word, guess):
    if guess == target_word:
        return "You guessed the word! Congratulations!"

    letters = []
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            letters.append(guess[i])
        elif guess[i] in target_word:
            letters.append("+")
        else:
            letters.append("-")

    return "".join(letters)

def main():
    word = choose_word()
    attempts = 5
    max_attempts = 0
    while attempts >= max_attempts:
        print("Attempts left: ",attempts)
        guess = input("Input your word: ")
        attempts -= 1

        if not is_valid_guess(guess):
            print("please enter a valid 5 letter lower case word")
            continue

        letters = check_guess(word,guess)
        print(letters)

        if guess == word:
            print("congrats you won")
            break

        if attempts == max_attempts:
            print("sorry you run out of attempts")
            break

main()
