import os
import time

global file


def lineSearch(word, polishSignAtTheBeginning):
    text = file.readline().decode("utf-8").strip()
    if not polishSignAtTheBeginning:
        while word[0] == text[0]:
            try:
                file.seek(-5000, os.SEEK_CUR)
                while file.read(1) != b"\n":
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(1, 0)
                break
            text = file.readline().decode("utf-8").strip()

    while word[0] != text[0]:
        text = file.readline().decode("utf-8").strip()
    while word[0] == text[0]:
        text = file.readline().decode("utf-8").strip()
        if word == text:
            return True
    else:
        return False


def binarySearch(wordWithoutPolishCharAtTheBeginning, startBit, endBit, wordWithPolishChars, polishSignAtTheBeginning):
    # print("Bits:", startBit, endBit)

    partition = int((endBit + startBit) / 2)
    # print("Partition:", partition)

    file.seek(partition, 0)

    while file.read(1) != b"\n":
        file.seek(-2, os.SEEK_CUR)
    text = file.readline().decode("utf-8").strip()
    if endBit == startBit:
        if word != text:
            return False

    if word == text:
        return True

    if word[0] < text[0]:
        return binarySearch(wordWithoutPolishCharAtTheBeginning, startBit, partition, wordWithPolishChars, polishSignAtTheBeginning)
    elif word[0] == text[0]:
        return lineSearch(wordWithPolishChars, polishSignAtTheBeginning)
    else:
        return binarySearch(wordWithoutPolishCharAtTheBeginning, partition + 3, endBit, wordWithPolishChars, polishSignAtTheBeginning)


word = input("Your word: ").strip().lower()
originalWord = word
polishSignAtTheBeginning = False
if word[0] > "z":
    polishSignAtTheBeginning = True
    if word[0] == "ą":
        word = "a" + word[1:]
        print(word)
    elif word[0] == "ć":
        word = "c" + word[1:]
    elif word[0] == "ę":
        word = "e" + word[1:]
    elif word[0] == "ł":
        word = "l" + word[1:]
    elif word[0] == "ń":
        word = "n" + word[1:]
    elif word[0] == "ó":
        word = "o" + word[1:]
    elif word[0] == "ś":
        word = "s" + word[1:]
    elif word[0] == "ź":
        word = "z" + word[1:]
    elif word[0] == "ż":
        word = "z" + word[1:]

startTime = time.time()
file = open("SJP.txt", "rb")
    # dictionary text file was to big to upload, therefore below I paste it's google-drive link:
    # https://drive.google.com/file/d/1vOnYIJpBqTT8LXzqiXGhshFj0MTLgdWp/view?usp=sharing
    
myEndBit = file.seek(0, os.SEEK_END)

if binarySearch(word, 1, myEndBit, originalWord, polishSignAtTheBeginning):
    print("Your word is contained in the file :>")
else:
    print("Your word is NOT contained in the file :<")
print(time.time() - startTime)

file.close()


