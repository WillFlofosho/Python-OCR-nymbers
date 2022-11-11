# Given a 3 x 4 grid of pipes, underscores, and spaces, determine which number is represented, or whether it is garbled.

# Defining the binary font
digits = {
    (' _ ', '| |', '|_|', '   '): '0',
    ('   ', '  |', '  |', '   '): '1',
    (' _ ', ' _|', '|_ ', '   '): '2',
    (' _ ', ' _|', ' _|', '   '): '3',
    ('   ', '|_|', '  |', '   '): '4',
    (' _ ', '|_ ', ' _|', '   '): '5',
    (' _ ', '|_ ', '|_|', '   '): '6',
    (' _ ', '  |', '  |', '   '): '7',
    (' _ ', '|_|', '|_|', '   '): '8',
    (' _ ', '|_|', ' _|', '   '): '9'
}


def convert(input_grid):
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not divisible by four")
    line_len = set()
    for line in input_grid:
        line_len.add(len(line))
        if len(line) % 3:
            raise ValueError("Number of input columns is not divisible by three")
    ret = ''
    for y_index in range(0, len(input_grid), 4):
        for x_index in range(0, len(input_grid[y_index]), 3):
            number_grid = tuple(input_grid[y][x_index:x_index + 3] for y in range(y_index, y_index + 4))
            ret += digits.get(number_grid, '?')
        ret += ','
    return ret[:-1]
