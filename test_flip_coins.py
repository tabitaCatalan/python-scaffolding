import flip_coins

def test_flip_coins(): 
    n = 10 
    coins = flip_coins.flip_coins(n) 
    assert len(coins) == n 
    for coin in coins: 
        assert coin in ['head', 'tail']


def test_coins_summary(): 
    real_summary = {'head' : 5, 'tail' : 3} 
    coins = ['head', 'head', 'tail', 'head', 'head', 'head', 'tail', 'tail']
    calculated_summary = flip_coins.coins_summary(coins)
    assert real_summary['head'] == calculated_summary['head']
    assert real_summary['tail'] == calculated_summary['tail'] 
z