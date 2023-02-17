import random

#Устанавливаем факторы, приводим значения слов к стандартному виду

def checkWord(i, sep):
    finalSp = ""
    i = i.removesuffix("\n").lower()
    if i.endswith("ть"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("ти"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("ся"):
        finalSp += "1"
    else:
        finalSp += "0"

    if "онок" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ёнок" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ик" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ичек" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "чик" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ник" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ек" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if "ище" in i:
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("ы"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("а"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("я"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("о"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("е"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("и"):
        finalSp += "1"
    else:
        finalSp += "0"

    if i.endswith("й"):
        finalSp += "1"
    else:
        finalSp += "0"

    finalSp += sep
    return finalSp

class SetFactor:


    def check(self, nameFile, sep):
        allWords = []
        for i in open(nameFile, "r", encoding="UTF-8").readlines():
            allWords.append(checkWord(i,sep))
        return allWords

    def setWords(self, allWords):
        self.allWordsFactorsLearning = []
        self.allWordsFactorsTesting = []
        self.allWordsResultLearning = []
        self.allWordsResultTesting = []
        if self.words == -1:
            self.words = len(allWords)
        allWords = random.sample(allWords, self.words)
        for i in range(self.words//10*9):
            line = allWords[i].removesuffix(" \n")
            self.allWordsResultLearning.append(int(line[-1]))
            line = line.removesuffix(line[-1])
            self.allWordsFactorsLearning.append(list(map(int, line.split())))
        for i in range(self.words//10*9, self.words):
            line = allWords[i].removesuffix(" \n")
            self.allWordsResultTesting.append(int(line[-1]))
            line = line.removesuffix(line[-1])
            self.allWordsFactorsTesting.append(list(map(int, line.split())))






    def __init__(self, nameNouns,nameVerbs, words=7000 ):
        self.words = words
        try:
            to = open("Factors.txt", "x", encoding="UTF-8")
            factorsList = self.check(nameNouns, "1")
            factorsList += self.check(nameVerbs, "0")
            random.shuffle(factorsList)
            for line in factorsList:
                for f in line:
                    to.write(f+" ")
                to.write("\n")
            to.close()
        except FileExistsError:
            pass
        self.setWords(open("Factors.txt", "r", encoding="UTF-8").readlines())



