"""
COMP.CS.100 "tiedostot_lukeminen" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    file_name = input("Enter the name of the file: ")

    file = open(file_name, mode="r")

    line_number = 1
    for file_line in file:
        file_line = file_line.rstrip()

        print(f"{line_number} {file_line}")
        line_number += 1

    file.close()

if __name__ == "__main__":
    main()