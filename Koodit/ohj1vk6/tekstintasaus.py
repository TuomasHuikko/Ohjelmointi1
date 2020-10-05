"""
COMP.CS.100 "tekstintasaus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def text_input():
    """

    :return:
    :rtype: list
    """

    text_list = []
    while True:
        text = input()
        if text != "":
            text_list.append(text)
            continue
        else:
            break




def main():

    print("Enter text rows. Quit by entering an empty row.")
    text_input()

    char_per_line = int(input("Enter the number of characters per line: "))

if __name__ == "__main__":
    main()