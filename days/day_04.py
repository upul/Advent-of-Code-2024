def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as fp:
        data = fp.read()
        return data


def parse(data):
    # Split the data into lines and remove empty lines
    lines = [line for line in data.splitlines() if line.strip()]
    # Convert each line into a list of characters
    grid = [list(line) for line in lines]
    return grid


def validate_grid(grid):
    row_len = len(grid[0])
    for row in grid:
        assert len(row) == row_len
    return True


def part_two(grid):
    def validate(row, col):
        def valid_move(row, col):
            return 0 <= row < m and 0 <= col < n

        pos_direction = [(1, 1), (-1, -1)]
        valid_pos_dir = [
            grid[(row + y)][(col + x)]
            for x, y in pos_direction
            if valid_move(row + y, col + x)
        ]

        neg_direction = [(-1, 1), (1, -1)]
        valid_neg_dir = [
            grid[(row + y)][(col + x)]
            for x, y in neg_direction
            if valid_move(row + y, col + x)
        ]
        if len(valid_pos_dir) != 2 or len(valid_neg_dir) != 2:
            return 0

        pos_word = valid_pos_dir[0] + "A" + valid_pos_dir[1]
        neg_word = valid_neg_dir[0] + "A" + valid_neg_dir[1]
        if pos_word in ["MAS", "SAM"] and neg_word in ["MAS", "SAM"]:
            return 1
        return 0

    m = len(grid)
    n = len(grid[0])

    num_valid_words = 0
    for row in range(m):
        for col in range(n):
            curr_char = grid[row][col]
            if curr_char == "A":
                num_valid_words += validate(row, col)
    return num_valid_words


def part_one(grid):
    def validate(row, col):
        def valid_move(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        counter = 0
        for dx, dy in directions:
            word = grid[row][col]

            for i in range(1, 4):
                # TODO: (Upul) this is not an optimized solution
                new_row, new_col = row + dy * i, col + dx * i
                if valid_move(new_row, new_col):
                    word += grid[new_row][new_col]
            if word == "XMAS":
                counter += 1
        return counter

    m = len(grid)
    n = len(grid[0])

    num_valid_words = 0
    for row in range(m):
        for col in range(n):
            curr_char = grid[row][col]
            if curr_char == "X":
                num_valid_words += validate(row, col)

    return num_valid_words


if __name__ == "__main__":
    sample_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

    grid = parse(sample_data)
    valid_words = part_one(grid)
    print(valid_words)

    test_data = parse(read_file("./data/day_04.txt"))
    valid_words = part_one(test_data)
    print(valid_words)

    valid_words = part_two(grid)
    print(valid_words)
    valid_words = part_two(test_data)
    print(valid_words)
