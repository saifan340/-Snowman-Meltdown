import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]
def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    mistakes = 0
    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    while mistakes< len(STAGES):
          guess = input("Guess a letter: ").lower()
          display_game_state(mistakes, secret_word, guess)
          if not is_letter_in_guess(guess, secret_word):
              mistakes += 1

          print("You guessed:", guess)


def  display_game_state(mistakes, secret_word, guessed_letters):
     print(STAGES[mistakes])
     display_word = ""
     for letter in secret_word:
         if letter == guessed_letters:
            #if is_letter_in_guess(guessed_letters,secret_word):
             display_word+= letter
         else:
             display_word+= "_"
     print(display_word)
def is_letter_in_guess(guess_letter,secret_word):

    return guess_letter in secret_word
if __name__ == "__main__":
    play_game()