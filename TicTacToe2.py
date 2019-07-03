import os

board = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]
board1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_board():
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')
	print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " " + '        7 | 8 | 9 ')
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3 + '       -----------')
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')
	print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " " + '        4 | 5 | 6 ')
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3 + '       -----------')
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')
	print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " " + '        1 | 2 | 3 ')
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3 + '          |   | ')


def show_board1():
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[7] + " " + "|" + " " + board1[8] + " " + "|" + " " + board1[9] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[4] + " " + "|" + " " + board1[5] + " " + "|" + " " + board1[6] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[1] + " " + "|" + " " + board1[2] + " " + "|" + " " + board1[3] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
    
p1 = input("Player 1, enter your name: ")
p2 = input("Player 2, enter your name: ")

def pos():
	while True:
		pos1 = int(input("{}, Enter the position for X : ".format(p1)))
		if board[pos1] == " ":
			board[pos1] = "X"
			show_board()
		elif board[pos1] == "X":
			print("Warning!! Don't use already occupied position!! This is already taken by X!!")
			pos1 = int(input("{}, Enter the position for X : ".format(p1)))
			if board[pos1] != " ":
				print("Game over as you've given a pre-occupied position twice!!!")
				break
			board[pos1] = "X"
			show_board()
		else:
			print("Warning!! Don't use already occupied position!! This is already taken by O!!")
			pos1 = int(input("{}, Enter the position for X : ".format(p1)))
			if board[pos1] != " ":
				print("Game over as you've given a pre-occupied position twice!!!")
				break
			board[pos1] = "X"
			show_board()
		if board[1] == board[2] == board[3] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[2] == board[3] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[4] == board[5] == board[6] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[4] == board[5] == board[6] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[7] == board[8] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[7] == board[8] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[4] == board[7] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[4] == board[7] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[2] == board[5] == board[8] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[2] == board[5] == board[8] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[6] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[6] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[5] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[5] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[5] == board[7] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[5] == board[7] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		if tie():
			print("Ended up in a tie!!")
			break
		pos2 = int(input("{}, Enter the position for O: ".format(p2)))
		if board[pos2] == " ":
			board[pos2] = "O"
			show_board()
		elif board[pos2] == "X":
			print("Warning!! Don't use already occupied position!! This is already taken by X!!")
			pos2 = int(input("{}, Enter the position for O: ".format(p2)))
			if board[pos2] != " ":
				print("Game over as you've given a pre-occupied position twice!!!")
				break
			board[pos2] = "O"
			show_board()
		else:
			print("Warning!! Don't use already occupied position!! This is already taken by O!!")
			pos2 = int(input("{}, Enter the position for O: ".format(p2)))
			if board[pos2] != " ":
				print("Game over as you've given a pre-occupied position twice!!!")
				break
			board[pos2] = "O"
			show_board()
		if board[1] == board[2] == board[3] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[2] == board[3] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[4] == board[5] == board[6] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[4] == board[5] == board[6] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[7] == board[8] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[7] == board[8] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[4] == board[7] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[4] == board[7] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[2] == board[5] == board[8] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[2] == board[5] == board[8] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[6] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[6] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[5] == board[9] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[5] == board[9] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[5] == board[7] == "X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[5] == board[7] == "O":
			print("Game Over!! {} wins!!".format(p2))
			break
		if tie():
			print("Ended up in a tie!!")
			break


def retry():
	while True:
		re = input("Do you want to play again? (yes or no)").upper()
		if re == "Y" :
			for i in range(0,10):
				board[i] = " "
			pos()
		else:
			menu()
			


def tie():
	full_board = True
	for i in range(1,10):
		if board[i] == " ":
			full_board = False
	if full_board is True:
		return True

def menu():
    print("//////////Tic Tac Toe//////////")
    print()

    choice = input("""
                      A: Play 1vs1
                      B: Play 1vsAI
                      Q: Exit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        game()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        exit()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def game():
    show_board1()
    pos()
    retry()

import random

def drawBoard(board):
    print('   |   |' + '            |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '        7 | 8 | 9 ')
    print('   |   |' + '            |   | ')
    print('-----------' + '      -----------')
    print('   |   |' + '            |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '        4 | 5 | 6 ')
    print('   |   |' + '            |   | ')
    print('-----------' + '      -----------')
    print('   |   |' + '            |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '        1 | 2 | 3 ')
    print('   |   |' + '            |   | ')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    if input().lower().startswith('y'):
        login()
    else:
        menu()


def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

    
def login():
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        menu()

menu()

