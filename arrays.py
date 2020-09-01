import os
import time


def handleArrays(filename):
    array = []
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "arrays", filename)
    file1 = open(filename, "r")
    Lines = file1.readlines()
    for line in Lines:
        array.append(int(line.strip()))

    return array


def writeresult(type, size, time):
    text_file = open("results.txt", "a")
    text_file.write(f"{type}, {size}, {time}s\n")
    text_file.close()


def clearresult():
    text_file = open("resultados.txt", "w")
    text_file.write("")
    text_file.close()


def gnomeSort(arr):
    index = 0
    n = len(arr)
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr


def combSort(arr):
    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True
    return arr


def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = int(gap / 2)

    return arr


types = ["aleatorio", "ordenado", "repetido", "reverso", "semiOrdenado"]
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
clearresult()
for size in sizes:
    for type in types:
        filename = f"{type}{size}.txt"
        start_time = time.time()
        array = handleArrays(filename)
        ##array = gnomeSort(array)
        ##array = combSort(array)
        array = shellSort(array)
        timeElapsed = time.time() - start_time
        print(f"Array {type} com {size} posições demorou {timeElapsed} segundos")
        writeresult(type, size, timeElapsed)
