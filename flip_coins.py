# Code from: https://earthly.dev/blog/python-makefile/
import random 

head = 'head'
tail = 'tail'

coin_sides = [head, tail]

def flip_coins(n):
    """
        flip_coins(n)
    Flip n coins and return a list with results.
    # Example 
    ```
    >>> flip_coins(2)
    ['head', 'tail']
    >>> flip_coins(2)
    ['tail', 'tail']
    ```
    """
    coins = []
    for _i in range(n): 
        coins.append(random.choice(coin_sides))
    return coins 

def coins_to_str(coins): 
    """
    Make a string with information of a list of coins, where 'o' 
    represents heads and 'x' tails, separed by spaces.
    # Example 
    ```
    >>> coins_to_str(['head', 'tail', 'tail'])
    "o x x "
    ```
    """
    symbols = {head : 'o', tail : 'x'} 
    expression = ""
    for coin in coins:
        expression += symbols[coin] + " "
    return expression

def coins_summary(coins): 
    """
        coins_summary(coins)
    Count number of heads and tails in a list. Return a dictionary with keys
    'head' and 'tail'.
    # Example 
    ```
    >>> coins_summary(['head', 'head', 'head', 'tail', 'head'])
    {'head': 4, 'tail': 1}
    ```
    """
    summary = {head : 0, tail : 0}
    for coin in coins: 
        summary[coin] += 1 
    return summary 

def print_summary(coins):
    """
        print_summary(coins)
    Print a message informing number of heads and tails from summary dictionary.
    # Example 
    ```
    >>> print_summary(['head', 'tail', 'head'])
    "There are 2 heads and 1 tails: o x o "
    ```
    """
    summary = coins_summary(coins)
    strcoins = coins_to_str(coins)
    print('There are {} heads and {} tails: {}'.format(summary[head], summary[tail], strcoins))

if __name__ == "__main__": 
    number_of_coins = 5
    flipped_coins = flip_coins(number_of_coins)
    print_summary(flipped_coins)