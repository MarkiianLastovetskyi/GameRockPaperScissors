import unittest
from server import determine_winner  

class TestRockPaperScissors(unittest.TestCase):
    
    def test_tie(self):
        """Тест на нічийний результат"""
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")
        
    def test_player_wins(self):
        """Тест на перемогу гравця"""
        self.assertEqual(determine_winner('rock', 'scissors'), "You win!")
        self.assertEqual(determine_winner('scissors', 'paper'), "You win!")
        self.assertEqual(determine_winner('paper', 'rock'), "You win!")
        
    def test_player_loses(self):
        """Тест на програш гравця"""
        self.assertEqual(determine_winner('rock', 'paper'), "You lose!")
        self.assertEqual(determine_winner('scissors', 'rock'), "You lose!")
        self.assertEqual(determine_winner('paper', 'scissors'), "You lose!")

if __name__ == '__main__':
    unittest.main()
