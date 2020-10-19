"""
COMP.CS.100 "sanakirja_a" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found "
                                        "from the dictionary.")

        elif command == "A":
            engl_word = input("Give the word to be added in English: ")
            span_word =  input("Give the word to be added in Spanish: ")
            english_spanish[engl_word] = span_word

        elif command == "R":
            del_word = input("Give the word to be removed: ")
            if del_word in english_spanish:
                del english_spanish[del_word]
            else:
                print(f"The word {del_word} could not be "
                      f"found from the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            sentence = sentence.split(" ")
            translation = ""
            index = 0
            for word in range(0, len(sentence)):
                word = sentence[index]
                if word in english_spanish:
                    word = english_spanish[word]
                    sentence[index] = word
                index += 1

            print("The text, translated by the dictionary:")
            index = 0

            for word in range(0, len(sentence)):
                translation += sentence[index] + " "
                index += 1

            print(translation)

        elif command == "Q":
            print("Adios!")
            return
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
