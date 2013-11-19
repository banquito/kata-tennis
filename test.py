# -*- coding: utf-8 -*-

import unittest
from tennis import ScoreBoard

def build_game(player1, player2, points1, points2):
    scoreBoard = ScoreBoard(player1, player2)
    for p in range(points1):
        scoreBoard.make_point_player1()
    for p in range(points2):
        scoreBoard.make_point_player2()
    return scoreBoard

class TestTennis(unittest.TestCase):
    
    def test_new_game_should_return_vs(self):
        scoreBoard = build_game("Fer", "Nico", 0, 0)
        self.assertEqual("Fer vs Nico", scoreBoard.get_board())

    def test_new_game_should_return_vs_reverted(self):
        scoreBoard = build_game("Nico", "Fer", 0, 0)
        self.assertEqual("Nico vs Fer", scoreBoard.get_board())

    def test_player1_make_point_should_return_15_0(self):
        scoreBoard = build_game("Nico", "Fer", 1, 0)
        self.assertEqual("15 0", scoreBoard.get_board())

    def test_player1_make_2_points_should_return_30_0(self):
        scoreBoard = build_game("Nico", "Fer", 2, 0)
        self.assertEqual("30 0", scoreBoard.get_board())

    def test_player1_make_3_points_should_return_40_0(self):
        scoreBoard = build_game("Nico", "Fer", 3, 0)
        self.assertEqual("40 0", scoreBoard.get_board())

    def test_player1_make_4_points_should_return_win(self):
        scoreBoard = build_game("Nico", "Fer", 4, 0)
        self.assertEqual("Ganó Nico", scoreBoard.get_board())

    def test_player2_make_point_should_return_0_15(self):
        scoreBoard = build_game("Nico", "Fer", 0, 1)
        self.assertEqual("0 15", scoreBoard.get_board())

    def test_player2_make_2_points_should_return_0_30(self):
        scoreBoard = build_game("Nico", "Fer", 0, 2)
        self.assertEqual("0 30", scoreBoard.get_board())

    def test_player2_make_3_points_should_return_0_40(self):
        scoreBoard = build_game("Nico", "Fer", 0, 3)
        self.assertEqual("0 40", scoreBoard.get_board())

    def test_player2_make_4_points_should_win(self):
        scoreBoard = build_game("Nico", "Fer", 0, 4)
        self.assertEqual("Ganó Fer", scoreBoard.get_board())

    def test_player1_make_4_points_player2_make_4_points_should_return_deuce(self):
        scoreBoard = build_game("Nico", "Fer", 4, 4)
        self.assertEqual("Empate", scoreBoard.get_board())

    def test_player1_make_5_points_player2_make_4_points_should_return_advance(self):
        scoreBoard = build_game("Nico", "Fer", 5, 4)
        self.assertEqual("Ventaja p/Nico", scoreBoard.get_board())

    def test_player1_make_4_points_player2_make_5_points_should_return_advance(self):
        scoreBoard = build_game("Nico", "Fer", 4, 5)
        self.assertEqual("Ventaja p/Fer", scoreBoard.get_board())

if __name__ == "__main__":
    unittest.main() 