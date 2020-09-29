"""
COMP.CS.100 "bussi" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def find_next_bus():
    """
    Finds the next 3 available buses to Tampere
    """

    bus_times = [630, 1015, 1415, 1620, 1720, 2000]
    index = 0
    bus_counter = 0
    time = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    while index < len(bus_times):
        time_of_bus = int(bus_times[index])
        index += 1

        if (time_of_bus % bus_times[-1]) == 0:
            index = 0
            time = bus_times[0]
            print(time_of_bus)
            bus_counter += 1
        elif time > bus_times[-1]:
            time = bus_times[0]
            index = 0
        elif bus_counter == 3:
            break
        elif time_of_bus >= time:
            bus_counter += 1
            print(time_of_bus)


def main():

   find_next_bus()

if __name__ == "__main__":
    main()
