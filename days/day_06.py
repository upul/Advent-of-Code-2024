from utilities.file_io import read_file


def build_grid(text):

    return [
        [chr for chr in row if chr in [".", "#", "^"]]
        for row in text.split("\n")
        if len(row) > 0
    ]


def print_grid(grid):
    out = ""
    for row in grid:
        for col in row:
            out += col
        out += "\n"
    return out


def starting_coordinates(grid):
    m = len(grid)
    n = len(grid[0])
    print(m, n)
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "^":
                return row, col
    return (-1, -1)


def is_not_end(row, col, m, n):
    return 0 <= row < m and 0 <= col < n


def next_move(curr_row, curr_col, curr_dir, grid):
    def _is_valid(row, col, m, n):
        return 0 <= row < m and 0 <= col < n

    dir_delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    m, n = len(grid), len(grid[0])

    dx, dy = dir_delta[curr_dir % 4]
    new_row, new_col = curr_row + dy, curr_col + dx

    valid = _is_valid(new_row, new_col, m, n)
    if not valid:
        return -1, -1, False, curr_dir

    curr_cell = grid[new_row][new_col]
    if curr_cell == "#":
        curr_dir += 1
        dx, dy = dir_delta[curr_dir % 4]
        new_row, new_col = curr_row + dy, curr_col + dx

    return new_row, new_col, True, curr_dir


def move(grid, row, col):
    curr_dir = 0
    unique_positions = {(row, col)}

    while True:
        new_row, new_col, move_flag, curr_dir = next_move(row, col, curr_dir, grid)
        if not move_flag:
            break
        unique_positions.add((new_row, new_col))
        row, col = new_row, new_col
        grid[row][col] = "x"
    return len(unique_positions)


if __name__ == "__main__":
    simple_data = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#..."""

    grid = build_grid(simple_data)
    print()
    print("Initial Grid")
    print("====================")
    print(print_grid(grid))
    start_x, start_y = starting_coordinates(grid)
    print(start_x, start_y)

    num_moves = move(grid, start_x, start_y)
    print(f"Number of distinct cells visited: {num_moves}")
    print()
    print("Final Grid")
    print("====================")
    print(print_grid(grid))

    print("Running the puzzle input")
    puzzle_text = read_file("./data/day_06.txt")
    puzzle_grid = build_grid(puzzle_text)
    # print(print_grid(puzzle_grid))
    start_x, start_y = starting_coordinates(puzzle_grid)
    print(start_x, start_y)
    puzzle_distinct_moves = move(puzzle_grid, start_x, start_y)
    print(puzzle_distinct_moves)
    # print(print_grid(puzzle_grid))
