import random
import sys

sys.tracebacklimit = -1
errors = (AttributeError, ValueError)

#let's make it a class so it's easier to modify
class TicTacToe():
	def __init__ (self, gameboard = None):
		self.gameboard = gameboard
		self.gameboard = []
		self.player = None
#let's build the Gameboard		
	def build_board(self):
		for i in range (3):
			row = []
			for j in range (3):
				row.append('-')
			self.gameboard.append(row)

#let's define how the board is going to look
#everytime the user plays.

	def show_board(self):
		for row in self.gameboard:
			for item in row:
				print(item, end = " ")
			print ()
#let's check if the board if full
	def is_board_full(self):
		for row in self.gameboard:
			for item in row:
				if item == '-':
					return False
		return True
		
#user input
	def user_input(self):
		
		try:
			self.row, self.col = list (map(int, input("\n Enter row and column number: ").split()))
			print()
		except errors:
			print ("Please enter a valid input")

	
#check if place is taken
	def check_place(self):
		if self.gameboard [self.row -1][self.col -1] != '-':
			print("This position is taken, choose a different position player:", self.player)
			self.row, self.col = (list (map(int, input("\n Enter row and column number: ").split())))
			print()
		else:
			pass
			

#function to fill the board
	def fill_board(self):
		if self.gameboard [self.row -1][self.col -1] == '-':
			self.gameboard [self.row -1][self.col -1] = self.player		
			print()
			
#first player
	def first(self, player):
		if random.randint (0,1) == 0:
			return ('X','O')
		return ('O','X')
		
	
#let's define the win variable
	def win_variable(self):
		win = None
	
#let's check the winner
	def check_winner(self):
		n = len(self.gameboard)
		win = True
		for i in range (3):
			if all ((self.gameboard[i][j] == self.player for j in range(3))):
				return True
			if all ((self.gameboard[j][i] == self.player for j in range(3))):
				return True
			if all ((self.gameboard[j][j] == self.player for j in range(3))):
				return True
			if all ((self.gameboard[n - 1 -i][i]  == self.player for j in range(3))):
				return True
			else:
				return False
