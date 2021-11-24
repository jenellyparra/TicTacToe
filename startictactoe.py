from tictactoe import TicTacToe

t = TicTacToe()
#swaping function
def swap():		
	if t.player == 'X':
		t.player = 'O'
	else:
		t.player = 'X'
			

def start_game():

	t.build_board()
	t.first(t.player)
	t.player = 'O'
	while True:	
	
		#show board
		t.show_board()
	
		print ("it's player's", t.player, "turn")
		
		#accept user input
		t.user_input()
		
		

		t.check_place()
		t.fill_board()
		
		
		#Now we check if someone won
		if t.check_winner():
			print ("PLayer", t.player, "has won")
			break

			
		#check for a tie if board is full and there is no winner
		if t.is_board_full():
			print("It's a tie!!")
			break
	
		#swaping player's turn
		swap()
			
	print()
	t.show_board()

start_game()
