# 11. Lo Shu Magic Square
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The
# Lo Shu Magic Square has the following properties:
# •	 The grid contains the numbers 1 through 9 exactly.
# •	 The sum of each row, each column, and each diagonal all add up to the same number.
# This is shown in Figure 7-19.
# In a program you can simulate a magic square using a two-dimensional list. Write a function that accepts a
# two-dimensional list as an argument and determines whether the list is
# a Lo Shu Magic Square. Test the function in a program

def rowColum(listUser):
    rowNum = len((listUser))
    colNum = len (listUser[0])
    return rowNum, colNum


def getSumFirstRow(listUser, colNum):
    sumFirstRow = 0
    for rowIndex in range(1):
        for colIndex in range(colNum):
            sumFirstRow += listUser[rowIndex][colIndex]
    return  sumFirstRow


def sumRowSame(listUser, sumFirstRow, rowNum, colNum):
    sumRow = 0
    for rowIndex in range(rowNum):
        for colIndex in range(colNum):
            sumRow += listUser[rowIndex][colIndex]
        if sumRow != sumFirstRow:
            return False
        sumRow = 0
    return True


def sumColSame(listUser, sumFirstRow, rowNum, colNum):
    sumCol = 0
    for colIndex in range(colNum):
        for rowIndex in range(rowNum):
            sumCol += listUser[rowIndex][colIndex]
        if sumCol != sumFirstRow:
            return False
        sumCol = 0
    return True


def sumRowColSame(listUser, sumFirstRow, rowNum, colNum):
    if sumRowSame(listUser, sumFirstRow, rowNum, colNum) and sumColSame(listUser, sumFirstRow, rowNum, colNum):
        return True
    else:
        return False


def sumLeftDiagSame(listUser, lengthRowCol, sumFirstRow):
    sumLeftDiag = 0
    for leftDiagIndex in range(lengthRowCol):
        sumLeftDiag += listUser[leftDiagIndex][leftDiagIndex]
    if sumLeftDiag != sumFirstRow:
        return True
    else:
        return False


def sumRightDiagSame(listUser, lengthRowCol, sumFirstRow):
    sumRightDiag = 0
    colDiagIndex = lengthRowCol - 1
    for rowDiagIndex in range(lengthRowCol):
        sumRightDiag += listUser[rowDiagIndex][colDiagIndex]
        colDiagIndex -=1
    if sumRightDiag != sumFirstRow:
        return True
    else:
        return False


def sumDiagSame (listUser, lengthRowCol, sumFirstRow):
    if sumLeftDiagSame(listUser, lengthRowCol, sumFirstRow) and sumRightDiagSame(listUser, lengthRowCol, sumFirstRow):
        return True
    else:
        return False


def loShuMagiqSquare (listUser, sumFirstRow, rowNum, colNum, lengthRowCol):
    if sumRowColSame(listUser, sumFirstRow, rowNum, colNum) and sumDiagSame (listUser, lengthRowCol, sumFirstRow):
        return True
    else:
        return False


def main():
    listUser = [[4, 9, 1],
                [3, 5, 7],
                [8, 1, 6]]
    rowNum, colNum = rowColum(listUser)
    lengthRowCol = rowNum
    sumFirstRow = getSumFirstRow(listUser, colNum)
    if loShuMagiqSquare (listUser, sumFirstRow, rowNum, colNum, lengthRowCol):
        print("It is Lo Shu Magic Square")
    else:
        print("It is not Lo Shu Magic Square")


main()
