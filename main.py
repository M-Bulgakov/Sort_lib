def bubble_sort(l):

    for i in range(len(l)):

        for j in range(len(l) - i -1):

            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

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

def nes_quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
            nes_quick_sort(less)
            nes_quick_sort(pivot)
            nes_quick_sort(greater)











