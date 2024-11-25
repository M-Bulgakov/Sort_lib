import Sort_lib
import time
import random
from random import choice
from random import randint


a1 = []
for i in range(100):
    t = randint(1, 100000)
    a1.append(t)

a2 = []
for i in range(1000):
    t = randint(1, 100000)
    a2.append(t)

a3 = []
for i in range(10000):
    t = randint(1, 100000)
    a3.append(t)

print("Cортировка пузырьком")
print("10^2:")
a = a1[::]
Start = time.time()
Sort_lib.bubble_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^3:")
a = a2[::]
Start = time.time()
Sort_lib.bubble_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^4:")
a = a3[::]
Start = time.time()
Sort_lib.bubble_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)

print()
print()
print("Cортировка выбором")
print("10^2:")
a = a1[::]
Start = time.time()
Sort_lib.insertion_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^3:")
a = a2[::]
Start = time.time()
Sort_lib.insertion_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^4:")
a = a3[::]
Start = time.time()
Sort_lib.insertion_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)

print()
print()
print("Cортировка вставками")
print("10^2:")
a = a1[::]
Start = time.time()
Sort_lib.selection_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^3:")
a = a2[::]
Start = time.time()
Sort_lib.selection_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^4:")
a = a3[::]
Start = time.time()
Sort_lib.selection_sort(a)
Finish = time.time()
print((Finish - Start) * 1000)

print()
print()
print("Быстрая сортировка")
print("10^2:")
a = a1[::]
Start = time.time()
Sort_lib.quicksort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^3:")
a = a2[::]
Start = time.time()
Sort_lib.quicksort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^4:")
a = a3[::]
Start = time.time()
Sort_lib.quicksort(a)
Finish = time.time()
print((Finish - Start) * 1000)

print()
print()
print("Cортировка слиянием")
print("10^2:")
a = a1[::]
Start = time.time()
Sort_lib.msort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^3:")
a = a2[::]
Start = time.time()
Sort_lib.msort(a)
Finish = time.time()
print((Finish - Start) * 1000)
print("10^4:")
a = a3[::]
Start = time.time()
Sort_lib.msort(a)
Finish = time.time()
print((Finish - Start) * 1000)