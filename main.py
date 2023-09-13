SCRABBLE_SCORE = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2,
                  'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1,
                  'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1,
                  'v':8, 'w':4, 'x':8, 'y':4, 'z':10,
                  '-':0, '0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                  '6':0, '7':0, '8':0, '9':0}


def calculateScrabbleScore(name):
    total = 0
    for letter in name:
        total += SCRABBLE_SCORE[letter]
    return total


def main():
    f = open("pokemonList.txt", "r")
    pokeList = []

    pattern = r'[0-9]'
    for line in f.readlines():
        line = line.strip()
        pokeList.append(line.split(" "))
    for i in pokeList:
        i.append(calculateScrabbleScore(i[0]) * int(i[1]))
    highest = pokeList[[i[2] for i in pokeList].index(max([i[2] for i in pokeList]))]
    print(highest)


if __name__ == '__main__':
    main()
