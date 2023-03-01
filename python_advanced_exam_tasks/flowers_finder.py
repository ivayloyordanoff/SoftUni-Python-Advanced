from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = [
    "rose",
    "tulip",
    "lotus",
    "daffodil",
]

found_word = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for i in range(len(words)):
        if vowel in words[i]:
            words[i] = words[i].replace(vowel, "")

        if words[i] == "":
            found_word = True
            break

        if consonant in words[i]:
            words[i] = words[i].replace(consonant, "")

        if words[i] == "":
            found_word = True
            break

    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
else:
    found_index = words.index("")
    if found_index == 0:
        print("Word found: rose")
    elif found_index == 1:
        print("Word found: tulip")
    elif found_index == 2:
        print("Word found: lotus")
    elif found_index == 3:
        print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
