import random

# List of words to choose from
word_list = ['python', 'hangman', 'developer', 'programming', 'computer', 'software', 'algorithm']

# Function to choose a random word
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with blanks
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6
    guessed_word = False
    
    print("Welcome to Hangman!")
    
    while attempts_left > 0 and not guessed_word:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif guess not in word:
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            attempts_left -= 1
        else:
            print(f"Good guess! The letter '{guess}' is in the word.")
            guessed_letters.append(guess)
        
        # Check if the word is completely guessed
        if display_word(word, guessed_letters) == word:
            guessed_word = True
    
    if guessed_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nSorry, you ran out of attempts. The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_game()
