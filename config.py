import os
import secrets

# Session configuration
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True
SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)

# Game configuration - TBA
STARTING_CREDITS = 10