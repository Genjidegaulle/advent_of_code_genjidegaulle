def a(input):
    sum = 0

    for line in input:
        forward = line
        backward = line[::-1]

        f = -1
        b = -1
        for c in range(len(line)):
            if forward[c].isdigit() and f == -1:
                f = int(forward[c])
            if backward[c].isdigit() and b == -1:
                b = int(backward[c])

        sum += f*10 + b

    return sum


def b(input):
    sum = 0

    digits = [
        'one', '1',
        'two', '2',
        'three', '3',
        'four', '4',
        'five', '5',
        'six', '6',
        'seven', '7',
        'eight', '8',
        'nine', '9'
    ]

    digits_dic = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for line in input:
        f_i = 1000000
        b_i = 0

        f = -1
        b = -1

        for d in digits:
            f_index = line.find(d)
            b_index = line.rfind(d)
            if f_i >= f_index and f_index > -1:
                f_i = f_index
                if d.isdigit():
                    f = int(d)
                else:
                    f = digits_dic[d]

            if b_i <= b_index and b_index > -1:
                b_i = b_index
                if d.isdigit():
                    b = int(d)
                else:
                    b = digits_dic[d]

        sum += f*10 + b

    return sum

if __name__ == '__main__':
    input = []
    with open('input.txt') as file:
        input = file.readlines()

    s_input = ['two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'b6kpxgcv71six1',
            '7pqrstsixteen'
    ]
    print(a(input))
    print(b(input))
