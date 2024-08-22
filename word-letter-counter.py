# Prompt the user to enter a word and remove any leading or trailing spaces.
word = input("Please enter a word: ").strip()
# Check if the word contains any spaces.
if " " in word:
    print("Invalid input: The word should not contain any spaces.")
else:
    # If the word is valid (no spaces), count the number of characters in the word.
    character_count = len(word)
    print(f"The word {word} has {character_count} characters.")