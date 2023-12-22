import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

def choose_word(word_list):
    # Randomly select a word from the list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    word = choose_word(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman! Guess the fruit")

    while attempts > 0:
        display = display_word(word, guessed_letters)

        print(f"Word: {display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print("Incorrect guess.")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(word):
            print("Congratulations! You've guessed the word:", word)
            break

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()
