"""
COMP.CS.100 "listan_indeksointi_b" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():


    numbers = []
    index = -1
    print("Give 5 numbers: ")

    for number in range(0, 5):
        number = int(input("Next number: "))
        numbers.append(number)
    print("The numbers you entered, in reverse order:")
    for number in numbers:
        print(numbers[index])
        index -= 1



if __name__ == "__main__":
        main()