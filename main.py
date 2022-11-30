# Initials for who did what, Edward Hong as EH, Alden Panicker as AP, and Noah Yacoub as NY -NY
import pygame  #importing the pygame module -NY
import random  #Importing the random module -NY
def gameboard_drawing(board):
    #This function will 'draw' the game board as a list of 16 (4x4) instead of the usual 9 (3x3) -NY
    #this function takes a list 'board' with 16 strings that correspond to a four by four grid and prints it, including dividers, to create a visual board drawing for the tictactoe board -AP
    print(board[13]) + '|' + print(board[14]) +'|' + print(board[15]) + '|' + print(board[16])
    print('_______')  #Just a horizontal line to separate the rows and make it look a little cleaner -NY
    print(board[9]) + '|' + print(board[10]) + '|' + print(board[11]) + '|' + print(board[12])
    print('_______')
    print(board[5]) + '|' + print(board[6]) + '|' + print(board[7]) + '|' + print(board[8])
    print('_______')
    print(board[1]) + '|' + print(board[2]) + '|' + print(board[3]) + '|' + print(board[4])

def InputPlayerLetter():
    #This function will let the player choose which letter they want to be in the game, then choosing the computers letter based on that
    #
    letter = "" #Initializing the letter variable
    while not (letter == "X" or letter == "O"):
        print("Hello player, do you want to be X or O? ")
        letter = input().upper() #making sure that the letter chosen will be an upper case letter for simplicity
        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"] #Players letter will be shown as the first index and the computer will be the second

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board,int(move)):
        print("What is your next move? (1-16)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    possibleMoves =[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves)!= 0:
        return random.choice(possibleMoves)
    else:
        return None

def isWinner(bo, le): #Checks if the player or computer has placed three X's or O's in a row, winning the game. Checks every single case for this -NY and EH
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or (bo[2] == le and bo[3] == le and bo[4] == le) or (bo[5] == le and bo[6] == le and bo[7] == le) or (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[9] == le and bo[10] == le and bo[11] == le) or (bo[10] == le and bo[11] == le and bo[12] == le) or (bo[13] == le and bo[14] == le and bo[15] == le) or (bo[14] == le and bo[15] == le and bo[16] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[5] == le and bo[9] == le and bo[13] == le) or (bo[2] == le and bo[6] == le and bo[10] == le) or (bo[6] == le and bo[10] == le and bo[14] == le) or (bo[3] == le and bo[7] == le and bo[11] == le) or (bo[7] == le and bo[11] == le and bo[15] == le) or (bo[4] == le and bo[8] == le and bo[12] == le) or (bo[8] == le and bo[12] == le and bo[16] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[4] == le and bo[7] == le and bo[10] == le) or (bo[7] == le and bo[10] == le and bo[13] == le) or (bo[8] == le and bo[11] == le and bo[14] == le) or (bo[2] == le and bo[7] == le and bo[12] == le) or (bo[1] == le and bo[6] == le and bo[11] == le) or (bo[6] == le and bo[11] == le and bo[16] == le) or (bo[5] == le and bo[10] == le and bo[15] == le))

#Now it's time to code the artificial intelligence for our game, which will be split up in sections among the three of us -NY
def getComputerMove(board, computerLetter): #Verifies that the players chosen letter will be the opposite of the computer -NY
    if computerLetter == "X":
        playerLetter == "O"
    else:
        playerLetter == "X"

    for i in range(1, 17):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, i)
            if isWinner(boardCopy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 4, 13, 16])
    if move != None:
        return move

    #No center so cannot have computer put X or O there

    return chooseRandomMoveFromList(board, [2, 3, 5, 9, 14, 15, 8, 12, 6, 7, 10, 11])

def isBoardFull(board):
    for i in range(1, 17):
        if isSpaceFree(board, i):
            return False
        return True

print("Welcome to Tic-Tac-Toe, Player!")

while True:
    theBoard = ['']*10
    playerLetter, computerLetter = InputPlayerLetter()
    turn = whoGoesFirst()
    print("The" + turn + "will go first!")
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                 drawBoard(theBoard)
                 print("The computer wins! Better luck next time!")
                 gameIsPlaying = False
            else:
                turn = 'player'
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break





