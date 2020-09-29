"""
COMP.CS.100 "kolmion_kulmat" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def calculate_angle(angle_1, angle_2 = 90):
    """Calculates the third angle of a triangle with two other angles given as
    parameters"""

    angle_3 = 180 - angle_1 - angle_2
    return angle_3

def main():

   print(calculate_angle(30))


if __name__ == "__main__":
        main()