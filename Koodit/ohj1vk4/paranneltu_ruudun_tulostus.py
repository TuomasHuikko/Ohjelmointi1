"""
COMP.CS.100 "paranneltu_ruudun_tulostus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def print_box(width, height, border_mark="#", inner_mark=" "):
    """Prints a box with given parameters width, height and
    the outer and  inner marks to create the box. The inner and outer_mark
    have a default value of " " and "#". """

    for box in range(1, height+1):

        if box == 1 or box == height:
            print(width * border_mark)
        else:
            print(f"{border_mark}{(width-2)*inner_mark}{border_mark}")


def main():

    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
        main()