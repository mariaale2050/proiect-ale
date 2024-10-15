class WordHint:
    def __init__(self, index: int, hint: str, word: str):
        self.mIndex = index
        self.mWord = word
        self.mHint = hint

    def __str__(self):
        return f"Index: {self.mIndex}, Hint: {self.mHint}, Word: {self.mWord}"

    def __repr__(self):
        return self.__str__()


loadedWords = []


def loadWordsFromFile():
    """Incarca cuvintele din fisierul specificat."""
    file = open("cuvinte_de_verificat.txt", "r", encoding='utf-8')
    for line in file:
        elements = line.split(';')
        loadedWords.append(WordHint(int(elements[0]), elements[1], elements[2].rstrip()))


def getKnownLetterIndices(word_pattern: str) -> list[int]:
    """Obtine indicii literelor cunoscute in modelul cuvantului."""
    return [i for i, char in enumerate(word_pattern) if char != '*']


def getHint(letter: str, wordChosen: WordHint) -> list[int]:
    """Returneaza indicii literei in cuvantul ales."""
    return [i for i, char in enumerate(wordChosen.mWord) if char == letter]


def resolveHangman(hint: str, wordChosen: WordHint):
    """Rezolva jocul Hangman pe baza indiciului."""
    askCounter = 0
    totalHints = 0
    possibleWords = [x.mWord for x in loadedWords if len(x.mHint) == len(hint)]
    knownLetters = getKnownLetterIndices(hint)

    possibleWords = [word for word in possibleWords if all(word[i] == hint[i] for i in knownLetters)]

    while True:
        if len(possibleWords) == 1:
            print(f"Cuvantul tau este: {possibleWords[0]}")
            print(f"Cuvantul a fost gasit in: {askCounter} incercari")
            break

        if askCounter >= len(possibleWords[0]):
            print("Nu mai sunt litere de ghicit.")
            break

        lastLetter = possibleWords[0][askCounter]
        lettersFound = getHint(lastLetter, wordChosen)
        totalHints += 1

        possibleWords = [word for word in possibleWords if all(word[i] == lastLetter for i in lettersFound)]
        possibleWords = [word for word in possibleWords if all(word[i] == hint[i] for i in knownLetters)]

        askCounter += 1


if __name__ == "__main__":
    print("Bine ai venit la jocul Hangman!")
    print("Primul pas, sa incarcam cuvintele!")

    loadWordsFromFile()
    print(f"Numarul de cuvinte: {len(loadedWords)}")

    print("Sa incepem!")
    totalHints = 0
    for word in loadedWords:
        resolveHangman(word.mHint, word)

    print("Lista a fost parcursa.")