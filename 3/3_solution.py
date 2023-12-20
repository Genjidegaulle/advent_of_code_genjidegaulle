def a(input):
    import re

    sum = 0

    for line in range(len(input)):
        # First extract numbers
        nums = re.sub(' +', ' ', re.sub('[^0-9]', '.', input[line]).replace('.', ' ')).split(' ')

        for num in nums:
            if num.isdigit():
                # Check surroundings for symbol
                partition = input[line].partition(num)
                before = partition[0][-1] if partition[0] is not '' else ''
                after = partition[2][0] if partition[2] is not '' else ''
                box = [before, after]
                print(box)



    return sum


def b(input):

    sum = 0

    return sum


if __name__ == '__main__':
    input = []
    with open('input.txt') as file:
        input = file.readlines()

    s_input = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    print(a(s_input))
    print(b(input))
