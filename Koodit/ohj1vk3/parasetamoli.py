"""
COMP.CS.100 "parasetamoli" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def calculate_dose(weight, hours_from_dose, total_dose):
    """Calculate needed dose of parasetamol based on the given parameters of patient"""

    needed_dose = (weight * 15)

    if hours_from_dose <6:
        needed_dose = 0
    elif total_dose > 4000:
        needed_dose = 0
    elif total_dose > 3300 and total_dose < 4000:
        needed_dose = 4000 - total_dose


    return needed_dose



def main():


    weight = int(input("Patient's weight (kg): "))
    hours_from_dose = int(input("How much time has passed "
    "from the previous dose (full hours): "))
    total_dose = int(input("The total dose for the last 24 hours (mg): "))


    print(f"The amount of Parasetamol to give to the patient:"
          f" {calculate_dose(weight, hours_from_dose, total_dose)}")


    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()