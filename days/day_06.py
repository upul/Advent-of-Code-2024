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


def move(grid, row, col):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    curr_iter = 0
    num_cells = 0
    unique_positions = set()
    m, n = len(grid), len(grid[0])

    while is_not_end(row, col, m, n):
        dx, dy = directions[curr_iter % 4]
        new_row, new_col = row + dy, col + dx
        if not is_not_end(new_row, new_col, m, n):
            break

        if grid[new_row][new_col] == "#":
            # move right
            curr_iter += 1
        else:
            row, col = new_row, new_col
            unique_positions.add((row, col))

            # Just for debugging
            grid[row][col] = "*"
            num_cells += 1

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
