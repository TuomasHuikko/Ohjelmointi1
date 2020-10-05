"""
COMP.CS.100 "järjestetty_alimerkkijono" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def longest_substring_in_order(text):
    """
    Tarkastelee annettua merkkijonoa ja palauttaa merkkijonon kohdan, jossa on
    eniten aakkosjärjestyksessä olevia merkkejä.

    :param text: Syötetty merkkijono.
    :type text: str
    :return: Pisin aakkosjärjestyksessä oleva merkkijono.
    :rtype: str
    """

    index = 0

    longest_string_in_order = ""
    final_string = []

    if len(text) == 0:
        return ""
    elif len(text) == 1:
        return text


    for word in range(0, len(text)):
        character = text[index-1]
        character_2 = text[index]

        if index == 0:
            character = text[index]
            character_2 = text[index+1]
        elif character < character_2:
            longest_string_in_order += character
        elif character > character_2 and character > text[index-2]:
            longest_string_in_order += character
            longest_string_in_order += ","


        index += 1

    longest_string_in_order += text[-1]
    final_string = longest_string_in_order.split(",")

    index = 0
    for word in range(0, len(final_string)-1):

        if len(final_string[index]) < len(final_string[index+1]):
            del final_string[index]
        elif len(final_string[index]) > len(final_string[index+1]):
            del final_string[index+1]

    return final_string[0]

def main():

    print(longest_substring_in_order("abcabcdefgabab"))
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
    print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))

if __name__ == "__main__":
    main()
