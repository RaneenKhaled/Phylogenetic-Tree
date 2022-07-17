#Matrix
m = [
    [],
    [20],
    [60, 50],
    [100, 90, 40],
    [90, 80, 50, 30],
]
# Initializing the letters
def matrix_letters(first, last):
    letters = []
    for i in range(ord(first), ord(last) + 1):
        letters.append(chr(i))
    return letters

m_letters = matrix_letters("A", "E")

# Getting the index of the smallest number
def get_minVal(matrixx):
    minVal = float("inf")

    for i in range(len(matrixx)):
        for j in range(len(matrixx[i])):
            if matrixx[i][j] < minVal:
                minVal = matrixx[i][j]
                min_index1, min_index2 = i, j
    return min_index1, min_index2

# Merging the letters in the same cell
def merge_letters(letters, index1, index2):
    letters[index1] = "(" + letters[index1] + "," + letters[index2] + ")"
    del letters[index2]
    print(letters)

# Merging the matrix by getting average
# Deleting the row and column
def merge_matrix(matrix, index1, index2):

    if index2 < index1:
        index1, index2 = index2, index1
    r = []
    for i in range(0, index1):
        r.append((matrix[index1][i] + matrix[index2][i]) / 2)
    matrix[index1] = r

    for i in range(index2 + 1, len(matrix)):
        average = (matrix[i][index1] + matrix[i][index2]) / 2
        matrix[i][index1] = average
        del matrix[i][index2]
    del matrix[index2]
    print(matrix)

# UPGMA method
def Phylogenetic_Tree(matrix, letters):
    while len(letters) > 1:
        min_index1, min_index2 = get_minVal(matrix)
        merge_matrix(matrix, min_index1, min_index2)
        merge_letters(letters, min_index1, min_index2)
    return letters


print(Phylogenetic_Tree(m,m_letters))