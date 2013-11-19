# -*- coding: utf-8 -*-

class ScoreBoard:
	
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.player1_points = 0
		self.player2_points = 0

	def make_point_player1(self):
		self.player1_points += 1

	def make_point_player2(self):
		self.player2_points += 1

	def get_board(self):
		score = { 0: "0", 1: "15", 2: "30", 3: "40" }

		if (self.player1_points == 0 and self.player2_points == 0):
			return self.player1 + " vs " + self.player2
		elif (self.player1_points == self.player2_points):
			return "Empate"
		elif (self.player1_points > 3 and self.player1_points > self.player2_points + 1):
			return "Ganó " + self.player1
		elif (self.player1_points > 3 and self.player1_points > self.player2_points):
			return "Ventaja p/" + self.player1
		elif (self.player2_points > 3 and self.player2_points > self.player1_points + 1):
			return "Ganó " + self.player2
		elif (self.player2_points > 3 and self.player2_points > self.player1_points):
			return "Ventaja p/" + self.player2
		else:
			return score[self.player1_points] + " " + score[self.player2_points]
