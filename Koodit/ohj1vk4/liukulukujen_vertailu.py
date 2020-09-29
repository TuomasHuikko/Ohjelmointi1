"""
COMP.CS.100 "liukulukujen_vertailu" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""
EPSILON = 0.000000001

def compare_floats(float_1, float_2, EPSILON):
    """Compares two given floats with a margin of error of EPSILON.
    Returns value in boolean, true if floats close enough to each other,
    which is determined by abs(float_1-float_2)<EPSILON
    """
    result = bool(abs(float_1 - float_2) < EPSILON)
    return result

def main():

    print(compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON))

if __name__ == "__main__":
            main()
            