"""
COMP.CS.100 "ruutu" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def print_box(widht, height, mark):
    """prints the box with chosen attributes"""
    for box in range(0, height):
        print(widht * mark)

def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = str(input("Enter a print mark: "))

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()