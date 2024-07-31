import os
import secrets

# Session configuration
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True
SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)

# Game configuration
ROLL_COST = 1
STARTING_CREDITS = 10
SYMBOLS = ['C', 'L', 'O', 'W']  # Cherry, Lemon, Orange, Watermelon
SYMBOL_REWARDS = {
    'C': 10,
    'L': 20,
    'O': 30,
    'W': 40
}