"""
COMP.CS.100 "alkioiden_suuruusjärjestys" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def is_the_list_in_order(list):
    """Checks if the given list is in order of growing value
    :param list = a list
    """

    value = False
    if list == sorted(list):
        value = True

    return value

def main():

    print(is_the_list_in_order([]))


if __name__ == "__main__":
    main()