#TicTacToe Project - Milestone #1

#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 
#1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
	print('|        |         |         |') 
	print(f'|    {board[1]}   |    {board[2]}    |    {board[3]}    |') 
	print('|________|_________|_________|') 
	print('|        |         |         |') 
	print(f'|    {board[4]}   |    {board[5]}    |    {board[6]}    |') 
	print('|        |         |         |') 
	print('|________|_________|_________|') 
	print('|        |         |         |') 
	print(f'|    {board[7]}   |    {board[8]}    |    {board[9]}    |') 
	print('|        |         |         |') 
	print('|        |         |         |') 
test_board = ['#','X','O','X','O','X','O','X','O','X']


#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
#Think about using while loops to continually ask until you get a correct answer.
def player_input():
	player1 = input("Please pick a marker 'X' or 'O':").upper()
	while player1 != 'X' and player1 != 'O': #or while not player1 == 'X' or player 1 == 'O'
		print("Bruh, you have to pick X or O to get lit fam...")
		player1 = input("Please pick a marker 'X' or 'O'").upper()
	if player1 == 'X':
		print("Player 1, You are now, the X-man")
		print("Player 2, O-man... You can see where this is going.")
		player2 = 'O'
		return (player1,player2)
	elif player1 == 'O':
		print("Player 1, O you gotta be like that")
		print("Player 2, the X is bestowed upon you")
		player2 = 'X'
		return (player1,player2)


#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired 
#position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):#puts marker on board
	board[position] = marker


#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see 
#if that mark has won.
def win_check(board,mark): #checks if current marker is in order on board to win
	mark1 = mark.split() * 3
	mark2 = mark.split() * 3
	if mark1 == board[1:4] or mark1 == board[4:7] or mark1 == board[7:10]:
		return True
	elif mark1 == board[1:8:3] or mark1 == board[2:9:3] or mark1 == board[3:10:3]:
		return True
	elif mark1 == board[1:10:4] or mark1 == board[3:8:2]:
		return True
	elif mark2 == board[1:4] or mark2 == board[4:7] or mark2 == board[7:10]:
		return True
	elif mark2 == board[1:8:3] or mark2 == board[2:9:3] or mark2 == board[3:10:3]:
		return True
	elif mark2 == board[1:10:4] or mark2 == board[3:8:2]:
		return True
	else:
		return False
#could use for or while loop for the horizontal / vertical and manually write in diagnols

#Step 5: Write a function that uses the random module to randomly decide which player goes first. 
#You may want to lookup random.randint() Return a string of which player went first.
import random
def choose_first():
	if random.randint(1,2) == 1:
		return True
	else:
		return False


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely
#available.
def space_check(board,position): #Returns true if a space on the board is available
	return board[position] != 'X' and board[position] != 'O'
	# return board[position] == ' '

#Step 7: Write a function that checks if the board is full and returns a boolean value. 
#True if full, False otherwise.
def full_board_check(board): #if board is full of X or O, return True
	for xo in range(1,10):
		if board[xo] == 'X' or board[xo] == 'O':
			continue 
		else:
			return False
	return True


#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the 
#function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
	position = int(input('Please enter a number 1-9:'))
	while position < 1 or position > 9:
		position = int(input('Please enter a number 1-9:'))
	if space_check(test_board,position):
		return position

#Step 9: Write a function that asks the player if they want to play again and returns a boolean
#True if they do want to play again.
def replay():
	play_again = input("Would you like to play again?\n 'Y' for yes, 'N' for no").upper()
	while play_again != 'Y' and play_again != 'N':
		print("Dude you gotta press Y or N")
		play_again = input("Would you like to play again?\n 'Y' for yes, 'N' for no").upper()
	return play_again == 'Y'

#game start
continue_playing = True
while continue_playing:
	# Set the game up here
	print('Welcome to Tic Tac Toe!')
	game_on = True
	test_board = [' ','1','2','3','4','5','6','7','8','9']
	display_board(test_board)
	#marker = player_input() # ('X','O') if player 1 is X... ('O','X') if player 1 is O
	player1_marker,player2_marker = player_input()
	goes_first = choose_first() #true for player 1 or false for player 2
	while game_on:
		#player 1 Turn
		if goes_first == True:
			print("Player 1, your move...")
			position = player_choice(test_board)
			full_board_check(test_board)
			#if marker[0] == 'X':
				#place_marker(test_board,marker[0], position) #'X'
			#elif marker[0] == 'O':
				#place_marker(test_board,marker[0], position) #'O'
			place_marker(test_board,player1_marker,position)
			display_board(test_board)
			if win_check(test_board,player1_marker):
				print("You Win!!")
				game_on = False
			elif full_board_check(test_board):
				print("Looks like it's Tie...")
				game_on = False
			goes_first = False
		#player 2 Turn
		else:
			print("The pleasure is yours, Player 2")
			position = player_choice(test_board)
			full_board_check(test_board)
			#if marker[0] == 'X':
			#	place_marker(test_board,marker[1], position) #'O'
			#elif marker[0] == 'O':
			#	place_marker(test_board,marker[1], position) #'X'
			place_marker(test_board,player2_marker, position) #'X'
			display_board(test_board)
			if win_check(test_board,player2_marker):
				print("You Win!!")
				game_on = False
			elif full_board_check(test_board):
				print("Looks like it's Tie...")
				game_on = False
			goes_first = True
	if not replay():
		continue_playing = False


print('Thanks for Playing!')