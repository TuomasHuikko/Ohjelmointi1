"""
COMP.CS.100 "yogi_bear" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def repeat_name(bear_name, repeated_times):
    """repeats the bears name chosen number of times in verse"""

    for repeat in range(0, repeated_times):
        print(f"{bear_name}, {bear_name} Bear")


def verse(open_line, bear_name):
    """prints the verse of the song"""

    print(open_line)
    print(f"{bear_name}, {bear_name}")
    print(open_line)
    repeat_name(bear_name, 3)
    print(open_line)
    print(f"{bear_name}, {bear_name} Bear")
    print()



def main():

    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
        main()
