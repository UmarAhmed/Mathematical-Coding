import random
from matplotlib import pyplot as plt
 
snakes_and_ladders = {98:78, 95:75, 93:73, 87:24, 64:60, 62:10, 56:53, 49:11, 48:26, 16:6, 
		      80:100, 71:91, 28:84, 51:67, 21:42, 36:44, 9:31, 4:14, 1:38}
max_turns_per_game = 1000


# Simulates a single player game and returns how long it lasted
def play():
    position = 0
    turns = 0
    while position < 100 and turns < max_turns_per_game:
        position += random.randint(1, 6)
        # Check for snakes and ladders
        if position in snakes_and_ladders:
            position = snakes_and_ladders[position]
        turns += 1
    return turns

# Gets data on n games
def get_data(n):
    data = [play() for _ in range(n)]
    freq = [data.count(i) for i in set(data)]
    data = list(set(data))
    return {'data': data, 'freq': freq}


# Makes a frequency graph, showing how often a game lasts n turns
def make_table(dict_of_data):
    data = dict_of_data['data']
    freq = dict_of_data['freq']
    plt.title('Probability of finishing a game in n-moves')
    plt.xlabel('Number of Moves')
    plt.ylabel('Probability')
    plt.plot(data, freq)
    plt.show()
