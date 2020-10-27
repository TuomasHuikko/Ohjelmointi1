"""
COMP.CS.100 "poikkeukset" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def print_box(width, height, mark):
    """prints the box with chosen attributes"""

    for box in range(0, height):
        print(width * mark)

def read_input(integer):
  """checks if the given information is valid and usable"""

  loop = True


  while loop:
    try:
        value = int(input(integer))
    except ValueError:
        continue
    if value <= 0:
        continue
    else:
        loop = False
        return value


def main():


    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input(str("Enter a print mark: "))


    print_box(width, height, mark)


if __name__ == "__main__":
    main()