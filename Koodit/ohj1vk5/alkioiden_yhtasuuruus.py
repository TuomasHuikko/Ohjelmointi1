"""
COMP.CS.100 "alkioiden_yhtäsuuruus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def are_all_members_same(list):
    """
    Checks if all members of given list are valued the same
    :param list = list of numbers
    """

    boolean = True
    index = 0
    for value in range(0, len(list)+1):
        while index < len(list)-1:
            if len(list) == 0:
                break
            elif list[index] != list[index+1]:
                boolean = False
                break
            index += 1

    return boolean

def main():

    print(are_all_members_same([]))

if __name__ == "__main__":
        main()
