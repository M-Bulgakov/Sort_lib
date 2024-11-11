def bubble_sort(l):

    for i in range(len(l)):

        for j in range(len(l) - i -1):

            if l[j] > l[j + 1]:
                l[j], l[j + 1)] = l[j + 1], l[j]

    return l


def selection_sort(listochek):

    for i in range(len(listochek)):

        for j in range(i,len(listochek)):
            minimus = listochek[j]

            if listochek[j] < minimus:
                minimus = listochek[j]

        listochek[i] = minimus

    return listochek


def insertion_sort(listium):

    for i in range(1, len(listium)):

        if listium[i - 1] < listium[i]:
            b =listium[i]
            j = i - 1

            while listium[j] > listium[i]:
                j -= 1

            listium.pop(i)
            listium.insert(j + 1, b)

    return listium


def nes_quik_sort(listus):
    from random import randint
    b = listus[randint(0, len(listus))]

    for i in range()















'''def pizda_sort(xuem):
    xyem =[]
    return xuem,('po ebalu')'''




