# Code from: https://earthly.dev/blog/python-makefile/
import random 

head = 'head'
tail = 'tail'

coin = [head, tail]

def flip_coins(n):
    """
        flip_coins(n)
    Flip n coins and return a list with results.
    """
    coins = []
    for _i in range(n): 
        coins.append(random.choice(coin))
    return coins 

def coins_summary(coins): 
    """
        coins_summary(coins)
    Count number of heads and tails in a list. Return a dictionary.
    """
    summary = {head : 0, tail : 0}
    for coin in coins: 
        summary[coin] += 1 
    return summary 

def print_summary(summary):
    """
        print_summary(summary)
    Print a message informing number of heads and tails from summary dictionary.
    """
    print('There are {} heads and {} tails'.format(summary[head], summary[tail]))
