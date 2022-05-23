class City:
    ID = None
    x = None
    y = None

    def __init__(self, data: list):
        self.ID = data[0]
        self.x = data[1]
        self.y = data[2]

    @staticmethod
    def distance(A, B):
        return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** (1 / 2)


def entireDistance(cities: list):
    distance = 0
    for i in range(1, len(cities), 1):
        distance += City.distance(cities[i - 1], cities[i])
    return distance


def shortestPath(currentPathLength: 0, source: City, leftCities: list):
    minimalDistance = 999
    nextNode = None
    nextNodeIndex = None
    for city in leftCities:
        currentDistance = City.distance(source, city)
        if currentDistance < minimalDistance:
            minimalDistance = currentDistance
            nextNodeIndex = leftCities.index(city)
            nextNode = city

    currentPathLength += minimalDistance
    leftCities.pop(nextNodeIndex)
    if len(leftCities) == 0:
        return currentPathLength
    else:
        return shortestPath(currentPathLength, nextNode, leftCities)


if __name__ == '__main__':

    cities = []

    with open("TSP.txt") as file:
        for i in range(100):
            cities.append(City([float(x) for x in next(file).split()]))

    print("Route length in given in file order:\t\t\t", entireDistance(cities))

    for i in range(0, len(cities) - 1):
        for j in range(0, len(cities) - 1):
            if cities[j + 1].x < cities[j].x:
                cities[j + 1], cities[j] = cities[j], cities[j + 1]

    print("Route length after sorting by x-coordinates:\t", entireDistance(cities))

    for i in range(0, len(cities) - 1):
        for j in range(0, len(cities) - 1):
            if cities[j + 1].y + 11 < cities[j].y:                              # + 11, because it provided significant reduction of route
                cities[j + 1], cities[j] = cities[j], cities[j + 1]             # length, wchich will not be as efficient, if array was just sorted by y,
                                                                                # because then there would have been large y value differences between cities
                                                                                # being placed at similar x-coordinate (identical according to int value)

    print("Additionally sorted by y-coordinates:\t\t\t", entireDistance(cities))

    citiesCopy = None
    minimalRouteLength = 999
    ultimateSource = None
    sourceIndex = None
    for i in range(100):
        citiesCopy = cities.copy()
        currentSource = citiesCopy[i]
        citiesCopy.pop(i)
        currentRouteLength = shortestPath(0, currentSource, citiesCopy)
        if currentRouteLength < minimalRouteLength:
            minimalRouteLength = currentRouteLength
            ultimateSource = currentSource
            sourceIndex = i

    cities.pop(i)
    ultimatePathLength = shortestPath(0, ultimateSource, cities)
    print("Path calculated by Dijkstra algorithm:\t\t\t", ultimatePathLength)
