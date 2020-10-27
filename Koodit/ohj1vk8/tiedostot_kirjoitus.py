"""
COMP.CS.100 "tiedostot_kirjoitus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, mode="w")
    except OSError:
        print(f"Writing the file {file_name} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    line_number = 1
    while True:
        text_line = input()

        if text_line == "":
            break

        print(line_number, text_line, file=file)
        line_number += 1

    print(f"File {file_name} has been written. ")

    file.close()

if __name__ == "__main__":
    main()