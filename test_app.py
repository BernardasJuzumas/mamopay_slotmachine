#Test written by Claude Sonnet with a context of code file created

import unittest
from unittest.mock import patch
from app import app
import game_logic
from config import STARTING_CREDITS, SYMBOLS

class TestGameLogic(unittest.TestCase):
    def test_roll_slots(self):
        result = game_logic.roll_slots()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(symbol in SYMBOLS for symbol in result))

    def test_calculate_reward(self):
        self.assertEqual(game_logic.calculate_reward(['C', 'C', 'C']), 10)
        self.assertEqual(game_logic.calculate_reward(['L', 'L', 'L']), 20)
        self.assertEqual(game_logic.calculate_reward(['O', 'O', 'O']), 30)
        self.assertEqual(game_logic.calculate_reward(['W', 'W', 'W']), 40)
        self.assertEqual(game_logic.calculate_reward(['C', 'L', 'O']), 0)

    @patch('game_logic.roll_slots')
    def test_cheat_roll(self, mock_roll_slots):
        # Test that cheat_roll re-rolls when all symbols are the same
        mock_roll_slots.side_effect = [['C', 'C', 'C'], ['C', 'L', 'O']]
        with patch('random.random', return_value=0.1):  # Ensure re-roll
            result = game_logic.cheat_roll(0.3)
        self.assertEqual(result, ['C', 'L', 'O'])

    def test_roll_with_different_credit_levels(self):
        # Test roll with less than 40 credits
        result = game_logic.roll(30)
        self.assertEqual(len(result), 3)
        
        # Test roll with credits between 40 and 60
        with patch('game_logic.random.random', return_value=0.2):  # Ensure re-roll
            result = game_logic.roll(50)
        self.assertEqual(len(result), 3)
        
        # Test roll with more than 60 credits
        with patch('game_logic.random.random', return_value=0.5):  # Ensure re-roll
            result = game_logic.roll(70)
        self.assertEqual(len(result), 3)

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_start_game(self):
        response = self.app.post('/start_game', json={'username': 'testuser'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['credits'], STARTING_CREDITS)

    def test_roll(self):
        # First, start a game
        self.app.post('/start_game', json={'username': 'testuser'})
        
        # Then, test rolling
        response = self.app.post('/roll')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('symbols', data)
        self.assertIn('reward', data)
        self.assertIn('credits', data)

    def test_cash_out(self):
        # First, start a game
        self.app.post('/start_game', json={'username': 'testuser'})
        
        # Then, test cashing out
        response = self.app.post('/cash_out')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('credits', data)

    def test_roll_without_session(self):
        response = self.app.post('/roll')
        self.assertEqual(response.status_code, 404)

    def test_cash_out_without_session(self):
        response = self.app.post('/cash_out')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()