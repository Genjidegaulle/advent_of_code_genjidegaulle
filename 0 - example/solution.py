def one_a(input):
    up = input[0].count('(')
    down = input[0].count(')')

    return int(up)-int(down)

def one_b(input):
    up = 0
    down = 0
    count = 0
    for i in input[0]:
        count += 1
        if i == '(':
            up += 1
        elif i == ')':
            down += 1

        if down > up:
            return count
    return len(input)

if __name__ == '__main__':
    input = []
    with open('input.txt') as file:
        input = file.readlines()
    print(one_a(input))
    print(one_b(input))
