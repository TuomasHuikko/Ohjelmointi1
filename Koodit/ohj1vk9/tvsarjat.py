"""
COMP.CS.100 "tvsarjat" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: Name of the file from which the series and their genres
        are taken.
    :type filename: str
    :return: Dictionary of given genres and the series in that genre.
    :rtype: dict
    """

    all_genres = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:
                if genre not in all_genres:
                    all_genres[genre] = []
                    all_genres[genre].append(name)
                elif name not in all_genres[genre]:
                    all_genres[genre].append(name)
                else:
                    all_genres[genre].append(name)

        file.close()
        return  all_genres

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    none = ", "

    print("Available genres are:", none.join(sorted(genre_data.keys())))

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        elif genre not in genre_data:
            continue
        else:
            for genre_name in sorted(genre_data[genre]):
                print(genre_name)


if __name__ == "__main__":
    main()
