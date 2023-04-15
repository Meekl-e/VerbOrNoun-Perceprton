from Perceptron import *

p = Perceptron("sets and data/nouns.txt","sets and data/verbsFixed.txt", 10, -1) # 100 - количество итерация, 1000 - количество слов в общей выборке
while True:
    print(p.test(input()))




