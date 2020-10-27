"""
COMP.CS.100 "tiedostot_virhe" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    line_number = 1
    for file_line in file:
        file_line = file_line.rstrip()

        print(f"{line_number} {file_line}")
        line_number += 1

    file.close()

if __name__ == "__main__":
    main()