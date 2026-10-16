# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
# Section:      555
# Assignment:   Lab8Bonus
# Date:         14 October 2026

# Create the starting checkboard
chessBoardPieces = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                    ["P", "P", "P", "P", "P", "P", "P", "P"],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    ["p", "p", "p", "p", "p", "p", "p", "p"],
                    ["r", "n", "b", "q", "k", "b", "n", "r"]
                   ]
chessBoardCoords = [["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
                    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
                    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
                    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
                    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
                    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
                    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"],
                    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"],
                   ]

# Context for the user
print("This program plays a game of chess without any strict rules against the pieces.")

# Show the user the board
charList = ["A", "B", "C", "D", "E", "F", "G", "H"]
print("    1    2    3    4    5    6    7    8")
for i in range(len(chessBoardPieces)):
    print(charList[i], end=" ")
    print(chessBoardPieces[i])

# Ask the user to move their pieces until they try to move an empty space
validMove = True
indexRow = 0; indexCol = 0
targetRow = 0; targetCol = 0
while validMove:
    tempMove = input("Which piece do you want to move (in terms of coordinates [e.g. A2, D5, F8, etc.])? ").upper()
    target = input("Where do you want to move this piece (in terms of coordinates [e.g. A2, D5, F8, etc.])? ").upper()
    # Find the index of both the piece and target location
    for row in range(len(chessBoardCoords)):
        for column in range(len(chessBoardCoords[row])):
            if tempMove == chessBoardCoords[row][column]:
                indexRow = row; indexCol = column
            if target == chessBoardCoords[row][column]:
                targetRow = row; targetCol = column
    # Move the piece to the target location as long as the user is not trying to move an empty space
    if chessBoardPieces[indexRow][indexCol] == ".":
        print("You have made an invalid movement.")
        break
    else:
        temp = chessBoardPieces[indexRow][indexCol]
        chessBoardPieces[indexRow][indexCol] = "."
        chessBoardPieces[targetRow][targetCol] = temp

    # Display the new layout
    print("    1    2    3    4    5    6    7    8")
    for i in range(len(chessBoardPieces)):
        print(charList[i], end=" ")
        print(chessBoardPieces[i])
