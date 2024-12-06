def is_safe(numbers):
    direction = "INC"
    pairs = [(x, y) for x, y in zip(numbers, numbers[1:])]
    if pairs[0][0] > pairs[0][1]:
        direction = "DEC"

    for x, y in pairs:
        if direction == "INC":
            diff = y - x
        else:
            diff = x - y
        if diff not in [1, 2, 3]:
            return False
    return True


def is_near_safe(numbers):
    def _is_strictly_ascending(arr):
        return all([x < y for x, y in zip(arr, arr[1:])])

    def _is_strictly_descending(arr):
        return all([x > y for x, y in zip(arr, arr[1:])])

    direction = "INC"
    first = numbers[0]
    last = numbers[-1]
    if last < first:
        direction = "DEC"

    num_bad = 0
    pairs = [(x, y) for x, y in zip(numbers, numbers[1:])]
    for x, y in pairs:
        if direction == "INC":
            diff = y - x
        else:
            diff = x - y
        if diff not in [1, 2, 3]:
            num_bad += 1

        if num_bad > 1:
            return False

    return True


def parse_file(file_name):
    with open(file_name, "r", encoding="utf-8") as fp:
        data = fp.readlines()
    return [[int(y.strip()) for y in x.strip().split()] for x in data]


def safe_calculator(reports):
    return sum([is_safe(report) for report in reports])


def near_safe_calculator(reports):
    counter = 0
    for report in reports:
        if is_safe(report):
            counter += 1
        else:
            if is_near_safe():
                pass


if __name__ == "__main__":
    # print(is_safe([7, 6, 4, 2, 1]))
    # print(is_safe([1, 2, 7, 8, 9]))
    # print(is_safe([8, 6, 4, 4, 1]))
    # print(is_safe([1, 3, 6, 7, 9]))
    reports = parse_file("./data/day_02.txt")
    print(safe_calculator(reports))
