board = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]
board1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
efef = ""

def show_board():
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)
	print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " ")
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)
	print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)
	print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")
	print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)


def show_board1():
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[1] + " " + "|" + " " + board1[2] + " " + "|" + " " + board1[3] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[4] + " " + "|" + " " + board1[5] + " " + "|" + " " + board1[6] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[7] + " " + "|" + " " + board1[8] + " " + "|" + " " + board1[9] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
# show_board1()

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
		re = input("Play again?(Y or N) Y for Yes and N for No ").upper()
		if re == "Y" :
			for i in range(0,10):
				board[i] = " "
			pos()
		else:
			print("Bye Bye!!")
			break


def tie():
	full_board = True
	for i in range(1,10):
		if board[i] == " ":
			full_board = False
	if full_board is True:
		return True

print("Welcome to 1V1 tic tac toe game!!")

show_board1() 
p1 = input("Player 1, enter your name: ")
p2 = input("Player 2, enter your name: ")
pos()
retry()