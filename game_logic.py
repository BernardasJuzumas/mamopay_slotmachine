import random
from config import SYMBOLS, SYMBOL_REWARDS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)
def roll(credits):
    if credits < 40:
        return roll_slots()
    elif 40 <= credits < 60:
        return cheat_roll(0.3)
    else:
        return cheat_roll(0.6)
    

def roll_slots():
    logger.info("Rolled {symbols}")
    return [random.choice(SYMBOLS) for _ in range(3)]


def cheat_roll(reroll_chance):
    symbols = roll_slots()
    #if all symbols are the same check of reroll and reroll
    if len(set(symbols)) == 1 and random.random() < reroll_chance:
        logger.info("Rerolling")
        return cheat_roll(reroll_chance)
    return symbols

def calculate_reward(symbols):
    if len(set(symbols)) == 1:
        return SYMBOL_REWARDS[symbols[0]]
    return 0



