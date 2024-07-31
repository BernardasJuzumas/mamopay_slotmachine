import random
from config import SYMBOLS, SYMBOL_REWARDS


def roll(credits):
    if credits < 40:
        return roll_slots()
    elif 40 <= credits < 60:
        return cheat_roll(0.3)
    else:
        return cheat_roll(0.6)
    

def roll_slots():
    return [random.choice(SYMBOLS) for _ in range(3)]


def cheat_roll(reroll_chance):
    symbols = roll_slots()
    #if all symbols are the same check of reroll and reroll
    if len(set(symbols)) == 1 and random.random() < reroll_chance:
        return cheat_roll(reroll_chance)
    return symbols

def calculate_reward(symbols):
    if len(set(symbols)) == 1:
        return SYMBOL_REWARDS[symbols[0]]
    return 0



