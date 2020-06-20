import random


def hangMan():
    words = ['python', 'java', 'kotlin', 'javascript']
    duplicate = []
    word = random.choice(words)
    # print(word)
    hint = ""
    j = 0
    for x in range(len(word)):
        hint = hint + "-"
    # print("H A N G M A N")
    while j != 8:
        print()
        print(hint)
        guess = input('Input a letter: ')
        if len(guess) > 1 or len(guess) == 0:
            print("You should input a single letter")
            print()
            print(hint)
        elif guess.isalpha() == False or guess.islower() == False:
            print("It is not an ASCII lowercase letter")
            print()
            print(hint)
        elif guess in duplicate and guess not in word:
            print("You already typed this letter")
            print()
            print(hint)
        elif guess in duplicate and guess in word:
            print("You already typed this letter")
        elif guess not in word:
            j += 1
            if j != 8:
                print("No such letter in the word")
                print()
                print(hint)
            if j == 8:
                print("No such letter in the word")
                print("You are hanged!")
                break
        duplicate.append(guess)
        for i in range(len(word)):
            if guess == word[i]:
                hint = hint[:i] + guess + hint[i + 1:]
        # if guess in word:
        #     print()
        #     print(hint)

        if hint == word:
            print("You guessed the word!")
            print("You survived!")
            break
print("H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "play":
        hangMan()
    if choice == "exit":
        break
    elif choice != "exit":
        continue





