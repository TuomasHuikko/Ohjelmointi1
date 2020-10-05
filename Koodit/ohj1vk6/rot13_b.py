"""
COMP.CS.100 "rot13_b" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def read_message():
    """
    Lukee käyttäjän syöttämän viestin ja tallentaa sen.

    :return: Syötetty viesti listana sanoja.
    :rtype: list
    """

    text = []
    while True:
        text_input = str(input())
        if text_input == "":
            break
        else:
            text.append(text_input)


    return text

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print()
    print("The same, shouting:")

    index = 0
    sentence = ""
    for word in range(0, len(msg)):
        word = msg[index]
        word = word.upper() + "\n"
        sentence += word
        index += 1

    print(sentence)

if __name__ == "__main__":
    main()
