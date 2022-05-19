import time


def naiveStringMatcher2D(pattern, filePathname):
    file = open(filePathname)

    data = file.readlines()

    coordinates = []
    for i in range(len(data) - len(pattern)):
        for j in range(len(data) - len(pattern)):
            if data[i][j: j + len(pattern)].__eq__(pattern):
                match = True
                for k in range(1, len(pattern)):
                    if data[i + k][j] != pattern[k]:
                        match = False
                        break
                if match:
                    coordinates.append([i, j])
    return coordinates


def rabinKarpMatcher(pattern, text, d, q):
    coordinates = []
    n = len(text)
    m = len(pattern)
    h = d ** (m - 1) % q
    p = 0
    ts = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        ts = (d * ts + ord(text[i])) % q

    for i in range(n - m):
        if p == ts:
            if text[i: i + len(pattern)] == pattern:
                coordinates.append([i])
        if i < n - m:
            ts = (d * (ts - ord(text[i]) * h) + ord(text[i + m])) % q

    return coordinates


def rabinKarpMatcher2D(pattern, filePathname, d, q):
    file = open(filePathname)
    data = file.readlines()

    coordinates = []

    m = len(pattern)
    h = d ** (m - 1) % q
    for row in range(len(data) - m):
        p = 0
        ts = 0
        n = len(data[row])
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            ts = (d * ts + ord(data[row][i])) % q

        for i in range(n - m):
            if p == ts:
                if data[row][i: i + len(pattern)] == pattern:
                    verticalText = ""
                    for l in range(m):
                        verticalText += data[row + l][i]
                    if verticalText.__eq__(pattern):
                        coordinates.append([row, i])

            if i < n - m:
                ts = (d * (ts - ord(data[row][i]) * h) + ord(data[row][i + m])) % q

    return coordinates


def execute(pattern, filePaths: list):
    for file in filePaths:
        print(file, "\tTime\tOccurrences")

        startNaiveTime = time.time()
        naiveCoords = naiveStringMatcher2D(pattern, file)
        executionNaiveTime = round(time.time() - startNaiveTime, 10)

        startRKTime = time.time()
        RKCoords = rabinKarpMatcher2D(pattern, file, 256, 13)
        executionRKTime = round(time.time() - startRKTime, 10)

        print("Naive:\t\t", executionNaiveTime, "\t\t", len(naiveCoords))
        print("Rabin-Karp:\t", executionRKTime, "\t\t", len(RKCoords))
        # print(executionRKTime / executionNaiveTime)

        print()


if __name__ == '__main__':
    pattern = "ABC"

    files = ["1000_pattern.txt", "2000_pattern.txt", "3000_pattern.txt",
             "4000_pattern.txt", "5000_pattern.txt"]

    execute(pattern, files)
