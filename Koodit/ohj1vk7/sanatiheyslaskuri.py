"""
COMP.CS.100 "sanatiheyslaskuri" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""


def main():
    words = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    loop = True
    all_sentences = []
    index = 0

    while loop:
        sentence = input()
        if sentence == "":
            loop = False

        sentence = sentence.lower()
        sentence = sentence.split(" ")


        all_sentences += sentence

    del all_sentences[-1]
    all_sentences = sorted(all_sentences)


    for word in range(0, len(all_sentences)):

        if all_sentences[index] in words:
            index += 1
            continue
        elif all_sentences[index] not in words:
            words[all_sentences[index]] = all_sentences.count(all_sentences[index])
            index += 1

    for word in words:
        print(f"{word} : {words[word]} times")

if __name__ == "__main__":
    main()
