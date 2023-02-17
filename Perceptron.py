

import SetFactors


#Класс Перцептрона

def sign(x):
    if x > 0:
        return 1  # сущ
    return 0  # глагол

class Perceptron:

    def __init__(self, nounsFileName, verbsFileName, k=100, words=1000):
        self.weightList = []
        try:
            data = open("weightList.txt", "r")
            for line in data.readlines():
                self.weightList.append(int(line.removesuffix("\n")))
        except FileNotFoundError:
            self.learning(nounsFileName, verbsFileName, k, words)


    def learning(self, nounsFileName, verbsFileName, k, words):
        factors = SetFactors.SetFactor(nounsFileName, verbsFileName, words)
        self.weightList = self.perceptron_train_solution(factors.allWordsFactorsLearning, factors.allWordsResultLearning, 1, k)
        count = 0
        for o in range(len(factors.allWordsResultTesting)):
            if self.perceptron_classify_solution(self.weightList, [factors.allWordsFactorsTesting[o]])[0] != factors.allWordsResultTesting[o]:
                count +=1
        error= 100/len(factors.allWordsResultTesting)*count
        print("Точность модели: ", 100-error )
        weightListFile = open("weightList.txt","w")
        for w in self.weightList:
            weightListFile.write(str(w)+"\n")




    def test(self, string):
        res = self.perceptron_classify_solution(self.weightList,[list(map(int, SetFactors.checkWord(string, "3").removesuffix("3")))], sign)
        if res == [1]:
            return "Существительное"
        elif res ==[0]:
            return "Глагол"
        else:
            return res



    def perceptron_classify_solution(self,ws, xs, f=sign):
        res = []
        for o in xs:

            summ = ws[-1]
            for w, x in zip(range(len(ws)), range(len(o))):
                summ += ws[w] * o[x]
            res.append(f(summ))
        return res

    def perceptron_train_solution(self, xs, ys, learning_rate=1, k=5):
        """
        Обучает перцептрон с функцией активации sign проводить классификацию переданного набора данных.
        В результате работы возвращает веса обученного перцептрона.

    """
        wList = [0] * (len(xs[0]) + 1)

        for iteration in range(k):
            print(iteration)
            result = self.perceptron_classify_solution(wList, xs)
            for res in range(0, len(result)):

                if result[res] != ys[res]:
                    for w in range(0, len(wList) - 1):
                        wList[w] = wList[w] + learning_rate * (ys[res] - result[res]) * xs[res][w]
                    wList[-1] = wList[-1] + learning_rate * (ys[res] - result[res])
                    result = self.perceptron_classify_solution(wList, xs)
            summ = 0
            for y, yp in zip(ys, result):
                summ += abs(y - yp)
            if summ / 2 * len(ys) <= 0:
                return wList

        return wList




