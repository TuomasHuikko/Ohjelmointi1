"""
COMP.CS.100 "merkkijononkirjaimet" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    word = str(input("Enter a word: "))

    index = 0
    vowel_counter = 0
    consonant_counter = 0
    for index in range(0, len(word)):
        letter = word[index]
        vocals = ["a", "o", "u", "e", "i", "ä", "ö", "y"]
        if letter in vocals:
            vowel_counter += 1
        else:
            consonant_counter += 1
        index += 1

    print(f"The word {word} contains {vowel_counter} vowels and"
          f" {consonant_counter} consonants")



if __name__ == "__main__":
    main()