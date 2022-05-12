import time


def recursiveHanoi(n: int, source: list, destination: list, buff: list):
    global recursiveCounter
    recursiveCounter += 1
    # print(recursiveCounter, mySource, myDestination, myBuff)

    if n > 1:
        recursiveHanoi(n - 1, source, buff, destination)
        destination.append(source.pop())
        recursiveHanoi(n - 1, buff, destination, source)

    if n == 1:
        destination.append(source.pop())


def move(currentSource: list, currentDestination: list):
    if len(currentDestination) == 0 and len(currentSource) != 0:
        currentDestination.append(currentSource.pop())
    elif len(currentSource) == 0 and len(currentDestination) != 0:
        currentSource.append(currentDestination.pop())
    elif currentSource[- 1] < currentDestination[- 1]:
        currentDestination.append(currentSource.pop())
    elif currentSource[- 1] > currentDestination[- 1]:
        currentSource.append(currentDestination.pop())


def iterativeHanoi(n: int, source: list, destination: list, buff: list):
    global iterativeCounter
    iterativeCounter = 1
    while len(source) != 0 or len(buff) != 0:
        # print(i, source, destination, buff)
        if iterativeCounter % 3 == 1:
            if n % 2 == 1:
                move(source, destination)
            else:
                move(source, buff)

        if iterativeCounter % 3 == 2:
            if n % 2 == 1:
                move(source, buff)
            else:
                move(source, destination)

        if iterativeCounter % 3 == 0:
            move(buff, destination)

        iterativeCounter += 1

    # print(iterativeCounter, source, destination, buff)


mySource = []

myBuff = []

myDestination = []

recursiveCounter = 0
iterativeCounter = 0

size = 20


def restart():
    mySource.clear()
    myBuff.clear()
    myDestination.clear()
    for i in range(size):
        mySource.append(size - i)


restart()
startTime = time.time()
recursiveHanoi(size, mySource, myDestination, myBuff)
print("Recursive time:", time.time() - startTime, "Operations:", recursiveCounter)

restart()
startTime = time.time()
iterativeHanoi(size, mySource, myDestination, myBuff)
iterativeCounter -= 1
print("Iterative time:", time.time() - startTime, "Operations:", iterativeCounter)
