import copy
import random
import sys
import time


class Object:

    def __init__(self, data):
        self.ID = data[0]
        self.width = data[1]
        self.height = data[2]
        self.value = data[3]
        self.valueRatio = self.value / (self.width * self.height)
        self.volume = self.width * self.height

    def rotate(self):
        rotatedObject = self
        rotatedObject.height = self.width
        rotatedObject.width = self.height

        return rotatedObject


def partition(items: list, beginIndex, endIndex):
    pivot = items[endIndex]
    i = beginIndex - 1
    for j in range(beginIndex, endIndex + 1, 1):
        if items[j].valueRatio > pivot.valueRatio:
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[endIndex] = items[endIndex], items[i + 1]
    return i + 1


def quickSort(items: list, beginIndex, endIndex):
    if beginIndex < endIndex:
        pi = partition(items, beginIndex, endIndex)
        quickSort(items, beginIndex, pi - 1)
        quickSort(items, pi + 1, endIndex)


def partitionVersion2(data: list, beginIndex, endIndex):
    pivot = data[endIndex]
    i = beginIndex - 1
    for j in range(beginIndex, endIndex + 1, 1):
        if data[j][1] > pivot[1]:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[endIndex] = data[endIndex], data[i + 1]
    return i + 1


def quickSortVersion2(data: list, beginIndex, endIndex):
    if beginIndex < endIndex:
        pi = partitionVersion2(data, beginIndex, endIndex)
        quickSortVersion2(data, beginIndex, pi - 1)
        quickSortVersion2(data, pi + 1, endIndex)


class Backpack:
    width = None
    height = None
    freeVolume = None
    slots = []
    itemsValue = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.slots.clear()
        for i in range(height):
            self.slots.append([])
            for j in range(width):
                self.slots[i].append(0)

        self.freeVolume = width * height

    def showSlots(self):
        i = 0
        for row in self.slots:
            print(i, row)
            i += 1

    def putInside(self, item: Object, coordinates: list):

        for i in range(item.height):
            for j in range(item.width):
                self.slots[coordinates[0] + i][coordinates[1] + j] = item.ID

        self.freeVolume -= item.volume
        self.itemsValue += item.value

    def fits(self, item: Object):
        if self.freeVolume < item.volume:
            return False

        i = 0
        while i + item.height <= self.height:
            j = 0
            while j + item.width <= self.width:
                if self.slots[i][j] == 0:
                    occupied = False
                    for k in range(i, i + item.height, 1):
                        for m in range(j, j + item.width, 1):
                            if self.slots[k][m] != 0:
                                occupied = True
                                break
                        if occupied:
                            break
                    if not occupied:
                        coordinates = [i, j]
                        return coordinates
                j += 1
            i += 1
        return False


def executeGreedily(paths: list):
    for pathname in paths:
        file = open(pathname)
        bagMeasurements = file.readline()
        bagMeasurements = bagMeasurements[9:-8]
        backpack = Backpack(int(bagMeasurements[0: bagMeasurements.find("x")]),
                            int(bagMeasurements[bagMeasurements.find("x") + 1:]))

        file.readline()
        items = []
        while True:
            try:
                data = [int(v) for v in file.readline().strip("\n").split(",")]
                items.append(Object(data))
            except ValueError:
                break

        quickSort(items, 0, len(items) - 1)
        sum = 0
        for item in items:
            inputTrial = backpack.fits(item)
            if type(inputTrial) == list:
                backpack.putInside(item, inputTrial)
                sum += item.value

            else:
                inputTrial = backpack.fits(item.rotate())
                if type(inputTrial) == list:
                    backpack.putInside(item.rotate(), inputTrial)
                    sum += item.value

        backpack.showSlots()
        resultsGreedily.append(sum)

        print("\n\n")


def combine(items: list, firstGenotype: list, secondGenotype: list, edgeSize):
    if len(secondGenotype) > len(firstGenotype):
        firstGenotype, secondGenotype = secondGenotype, firstGenotype
    elif len(secondGenotype) == len(firstGenotype):
        return firstGenotype

    backpack = Backpack(edgeSize, edgeSize)

    newGenotype = firstGenotype[0][0:] + secondGenotype[0][len(firstGenotype):]
    for i in range(newGenotype):
        coordinates = backpack.fits(items[i])
        if type(coordinates) == list:
            backpack.putInside(items[i], coordinates)
        else:
            newGenotype[0][i] = 0

    return [newGenotype, backpack.itemsValue]


def createRandomGenotype(items: list, backpack: Backpack):
    currentVectorOfItems = []
    currentValue = 0
    currentIndex = 0
    sequenceLength = 0
    while currentIndex < len(items):
        itemPresence = random.randint(0, 9)
        if itemPresence > 0:
            coordinates = backpack.fits(items[currentIndex])
            if type(coordinates) == list:
                backpack.putInside(items[currentIndex], coordinates)
                currentValue += items[currentIndex].value
                sequenceLength = 0
            else:
                itemPresence = 0

        if itemPresence == 0:
            sequenceLength += 1
            if sequenceLength > 10:
                break

        currentVectorOfItems.append(itemPresence)
        currentIndex += 1
    x = [currentVectorOfItems, backpack.itemsValue]

    return x


def executeGenetically(paths: list):
    for pathname in paths:

        file = open(pathname)
        bagMeasurements = file.readline()
        bagMeasurements = bagMeasurements[9:-8]
        backpack = Backpack(int(bagMeasurements[0: bagMeasurements.find("x")]),
                            int(bagMeasurements[bagMeasurements.find("x") + 1:]))

        file.readline()
        items = []
        while True:
            try:
                data = [int(v) for v in file.readline().strip("\n").split(",")]
                items.append(Object(data))
            except ValueError:
                break

        quickSort(items, 0, len(items) - 1)

        vectorsWithValues = []
        for i in range(10000):
            file = open(pathname)
            bagMeasurements = file.readline()
            bagMeasurements = bagMeasurements[9:-8]
            backpack = Backpack(int(bagMeasurements[0: bagMeasurements.find("x")]),
                                int(bagMeasurements[bagMeasurements.find("x") + 1:]))
            file.close()
            vectorsWithValues.append(createRandomGenotype(items, backpack))

        newVectors = []
        while len(vectorsWithValues) > 10:
            quickSortVersion2(vectorsWithValues, 0, len(vectorsWithValues) - 1)

            for i in range(0, len(vectorsWithValues) - 1, 2):
                newGenotypeWithValue = combine(items, vectorsWithValues[i], vectorsWithValues[i + 1], backpack.width)
                newVectors.append(newGenotypeWithValue)

            vectorsWithValues = newVectors.copy()
            newVectors.clear()

        quickSortVersion2(vectorsWithValues, 0, len(vectorsWithValues) - 1)
        resultsGenetically.append(vectorsWithValues[0][1])


if __name__ == '__main__':
    directory = ['packages20.txt', 'packages100.txt', 'packages500.txt', 'packages1000.txt']

    print(directory)

    sys.setrecursionlimit(5000)

    startTime = time.time()
    resultsGreedily = []
    resultsGenetically = []

    print(directory)
    executeGreedily(directory)

    executeGenetically(directory)

    print("Results:", resultsGreedily)
    print()
    print()
    print("Results:", resultsGenetically)

