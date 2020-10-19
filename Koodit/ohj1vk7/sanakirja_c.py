"""
COMP.CS.100 "sanakirja_c" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}
    contents_print = True

    while True:

        if contents_print:
            print("Dictionary contents:")
            dic_words = sorted(english_spanish)
            words = ", ".join(dic_words)
            print(words)

        contents_print = True
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found "
                                        "from the dictionary.")
            contents_print = False

        elif command == "A":
            engl_word = input("Give the word to be added in English: ")
            span_word = input("Give the word to be added in Spanish: ")
            english_spanish[engl_word] = span_word
            spanish_english[span_word] = engl_word


        elif command == "R":
            del_word = input("Give the word to be removed: ")

            if del_word in english_spanish:
                del english_spanish[del_word]
            else:
                print(f"The word {del_word} could not be "
                      f"found from the dictionary.")
            for word in spanish_english:

                if spanish_english[word] == del_word:
                    del spanish_english[word]

            contents_print = False

        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")

            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(f"{word} {spanish_english[word]}")

            print()
            contents_print = False


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