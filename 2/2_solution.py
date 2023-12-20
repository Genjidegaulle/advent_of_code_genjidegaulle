def a(input):
    sum = 0

    colors = {
        'blue' : 14,
        'green': 13,
        'red' : 12
    }

    for text in input:
        game = text.split(':')

        # Parse hands
        hands = game[1].split(';')
        valid = True
        for hand in hands:
            draws = hand.split(',')
            for draw in draws:
                for color in colors.keys():
                    if color in draw:
                        # Extract number
                        num_balls = int(draw.split(color)[0].strip())

                        if num_balls > colors[color]:
                            valid = False

        # Case if all counts are valid
        gameid = int(game[0].split(' ')[-1].strip())
        if valid:
            sum += gameid


    return sum


def b(input):
    import numpy as np

    sum = 0

    for text in input:
        game = text.split(':')

        colors = {
            'blue' : -1,
            'green': -1,
            'red' : -1
        }

        # Parse hands
        hands = game[1].split(';')
        for hand in hands:
            draws = hand.split(',')
            for draw in draws: # 3 loops max
                for color in colors.keys(): # 3 loops
                    if color in draw:
                        # Extract number
                        num_balls = int(draw.split(color)[0].strip())

                        # More balls than minimum
                        if colors[color] <= num_balls:
                            colors[color] = num_balls

        sum += np.prod(list(colors.values()))

    return sum


if __name__ == '__main__':
    input = []
    with open('input.txt') as file:
        input = file.readlines()

    s_input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    ]
    print(a(input))
    print(b(input))
