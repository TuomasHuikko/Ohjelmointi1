"""
COMP.CS.100 "fibonacci" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    main_loop = 0
    numbers = int(input("How many Fibonacci numbers do you want? "))
    previous_previous_fib = 1
    previous_fib = 1

    while main_loop < numbers:

        main_loop += 1


        print(f"{main_loop}. {previous_previous_fib}")
        new_fib = (previous_fib + previous_previous_fib)
        previous_previous_fib = previous_fib
        previous_fib = new_fib






if __name__ == "__main__":
        main()
