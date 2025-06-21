import random

# Word list
words = ['python', 'snowman', 'winter', 'icicle', 'frost']

# Snowman stages (like Hangman stages)
snowman_stages = [
    """
       ___
      /---\
      (o o)
      ( : )
      ( : )
    
    """,
    """
       ___
      /---\
      (o o)
      ( : )

    """,
    """
       ___
      /---\
      (o o)
      

    """,
    """
       ___
      /---\
      
      
    """

]

# Game setup
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = len(snowman_stages) - 1

# Game loop
while wrong_guesses < max_wrong:
    # Display current snowman stage
    print(snowman_stages[wrong_guesses])

    # Display the word with guessed letters
    display = [letter if letter in guessed_letters else "-" for letter in word]
    print("Word: ", " ".join(display))

    # Check for win
    if "-" not in display:
        print("🎉 You saved the snowman! You guessed the word.")
        break

    # Ask for guess
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess! The snowman is melting...")
        wrong_guesses += 1

else:
    print(snowman_stages[wrong_guesses])
    print("💀 The snowman has melted! The word was:", word)

