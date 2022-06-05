tree = [
    [1.5, [1.3], [1.6]],
    [3.5, [3.7]],
    [4.5, [4.0], [4.99]],
    [7.5, [7.3], [7.8, [7.7, [7.6]], [7.9]]],
    [9.5, [9.3]]
]


# każdy węzeł jest pierwszym elementem listy wierzchołków wychodzących z tego węzła,
# dzięki czemu można dodawać nowe węzły w dowolnym miejscu

def visualize(structure: list, level=0):
    # for node in structure:
    #     currentNode = node
    #     print(currentNode[0], end=" - ")
    #     while type(currentNode) == list:
    #         while len(currentNode) == 2:
    #             print(currentNode[0], end=" - ")
    #             currentNode = currentNode[1]
    #         if len(currentNode) == 3:
    #             copyCurrNode = currentNode
    #             while type(copyCurrNode) == list and len(copyCurrNode) > 1:
    #                 print(copyCurrNode[0], end=" - ")
    #                 copyCurrNode = copyCurrNode[1]
    #
    #             while type(currentNode) == list:
    #                 print(currentNode[0], end=" - ")
    #                 currentNode = currentNode[1]
    return 0


def partition(tree: list, beginIndex, endIndex):
    pivot = tree[endIndex][0]
    i = beginIndex - 1
    for j in range(beginIndex, endIndex + 1, 1):
        if tree[j][0] < pivot:
            i += 1
            tree[i], tree[j] = tree[j], tree[i]
    tree[i + 1], tree[endIndex] = tree[endIndex], tree[i + 1]
    return i + 1


def quickSortTree(tree: list, beginIndex, endIndex):
    if beginIndex < endIndex:
        pi = partition(tree, beginIndex, endIndex)
        quickSortTree(tree, beginIndex, pi - 1)
        quickSortTree(tree, pi + 1, endIndex)


def insert(x: float, structure: list):
    if (x - int(x)) * 100 == 50:
        for node in structure:
            if x == node:
                print("Root already contained.")
                break
        else:
            structure.append([x])
            quickSortTree(tree, 0, len(tree) - 1)
    else:
        if search(x, structure):
            print("Element", x, "is already contained.")
            return None

        added = False
        for node in structure:
            if abs(int(node[0] * 100) - int(x * 100)) <= 50 and int(node[0]) == int(x):
                swap = False
                while type(node) == list and len(node) > 1:
                    if x > node[0]:
                        if len(node) == 2:
                            if x > node[1][0] and node[1][0] < node[0]:
                                break
                            else:
                                node = node[1]
                        elif len(node) == 3:
                            node = node[2]
                    elif x < node[0]:
                        if len(node) == 2:
                            if x < node[1][0] and node[1][0] > node[0]:
                                swap = True
                                break
                            else:
                                node = node[1]
                        elif len(node) == 3:
                            node = node[1]
                node.append([x])
                if swap:
                    node[1], node[2] = node[2], node[1]
                added = True
                break
            else:
                continue
        if not added:
            print("There is no root for number ->", x)


def maximum(root: float, structure: list, shortened=False):
    if not shortened:
        for node in structure:
            if node[0] == root:
                structure = node
                shortened = True

    if type(structure) == float:
        return structure
    elif len(structure) == 3:
        return maximum(structure[0], structure[2], shortened)
    elif len(structure) == 2 and structure[1][0] > structure[0]:
        return maximum(structure[0], structure[1], shortened)
    elif len(structure) == 1:
        return structure[0]


def minimum(root: float, structure: list, shortened=False):
    if not shortened:
        for node in structure:
            if node[0] == root:
                structure = node
                shortened = True

    if type(structure) == float:
        return structure
    elif len(structure) == 3:
        return minimum(structure[0], structure[1], shortened)
    elif len(structure) == 2 and structure[1][0] < structure[0]:
        return minimum(structure[0], structure[1], shortened)
    elif len(structure) == 1:
        return structure[0]


def maximumQuicker(root: float, structure: list):
    for node in structure:
        if node[0] == root:
            structure = node

    while type(structure) == list:

        if len(structure) == 3:
            structure = structure[2]
        elif len(structure) == 2 and structure[1][0] > structure[0]:
            structure = structure[1]
        else:
            structure = structure[0]

    return structure


def minimumQuicker(root: float, structure: list):
    for node in structure:
        if node[0] == root:
            structure = node

    while type(structure) == list:

        if len(structure) >= 2 and structure[1][0] < structure[0]:
            structure = structure[1]

        else:
            structure = structure[0]
    return structure


def search(x: float, structure: list, rootFound=False):
    if not rootFound:
        for node in structure:
            if int(node[0]) == int(x):
                rootFound = True
                return search(x, node, rootFound)
    else:
        if type(structure) == float:
            if x == structure:
                return True
        else:
            if len(structure) == 1:
                return search(x, structure[0], rootFound)
            elif len(structure) == 2 and structure[0] != x:
                return search(x, structure[1], rootFound)
            elif len(structure) == 3 and structure[0] != x:
                return search(x, structure[1], rootFound) or search(x, structure[2], rootFound)
            else:
                return True

    return False


if __name__ == '__main__':

    insert(1.1, tree)
    insert(1.05, tree)

    print(maximum(7.5, tree))
    print(minimum(1.5, tree))

    print(maximumQuicker(7.5, tree))
    print(minimumQuicker(1.5, tree))

    found = False
    print(search(1.3, tree))
    print(search(3.5, tree))
    insert(3.9, tree)
    print(search(3.9, tree))

    for node in tree:
        print(node)
