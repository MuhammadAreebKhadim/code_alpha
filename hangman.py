import random

print("🎮 Welcome to Hangman Game!")

words = ["apple", "python", "table", "chair", "robot"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6
guessed_letters = []

while tries > 0 and "_" in guessed:
    print("\n🔤 Word:", " ".join(guessed))
    print(f"❌ Remaining Tries: {tries}")
    guess = input("👉 Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ Already guessed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Incorrect!")

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 Game over! The word was:", word)
print("Thanks for playing Hangman!")