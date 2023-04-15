from Perceptron import *

p = Perceptron("sets and data/nouns.txt","sets and data/verbsFixed.txt", 10, -1) #  количество итерация, количество слов в общей выборке (-1 - все слова)
while True:
    print(p.test(input()))




