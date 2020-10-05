"""
COMP.CS.100 "rot13_c" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.isupper() == True:
        text = text.lower()
        index = regular_chars.index(text)
        text = encrypted_chars[index]
        text = text.upper()
    elif text not in regular_chars:
        return text
    else:
        index = regular_chars.index(text)
        text = encrypted_chars[index]

    return text

def row_encryption(row_of_chars):
    """
    Encrypts the whole row of given characters with the help of function
    encrypt, which uses ROT13 technology.

    :param row_of_chars: Row of characters given by the user.
    :type row_of_chars: str
    :return: New encrypted row.
    :rtype: str
    """

    index = 0
    final_row = ""
    for char in range(0, len(row_of_chars)):
        character = row_of_chars[index]
        final_row += encrypt(character)
        index += 1

    return final_row

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
    print("ROT13:")
    index = 0
    sentence = ""
    for word in range(0, len(msg)):
        word = msg[index]
        word = row_encryption(word) + "\n"
        sentence += word
        index += 1

    print(sentence)

if __name__ == "__main__":
    main()
