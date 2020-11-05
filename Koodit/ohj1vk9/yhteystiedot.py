"""
COMP.CS.100 "yhteystiedot" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def read_file(file_name):
    """
    Reads given .csv file and makes a dictionary of the contact
        details of person(s) in the file. You can get a single detail of a
        person by calling the functions dictionary with [name][key(e.g. phone)].

    :param file_name: Name of given file.
    :type file_name: str
    :return: Dictionary of contact details in file.
    :rtype: dict
    """

    file = open(file_name, mode="r")

    names = {}
    line_number = 1
    info_keys = []

    for line in file:
        line = line.strip()
        line = line.split(";")
        if not line[0] == "key":
            names[line[0]] = {}
        index = 1

        if line_number == 1:
            info_keys = line[1:]
            line_number += 1
            continue
        else:
            for key in info_keys:
                if not index > len(line)-1:
                    names[line[0]][key] = line[index]
                index += 1

    return names

def main():

    info = read_file("contacts.csv")
    print(info)

if __name__ == "__main__":
    main()