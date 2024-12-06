import re
from functools import reduce

mul_pattern = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"
num_pattern = r"[0-9]{1,3}"
do_dons_pattern = r"don|do|mul\([0-9]{1,3}\,[0-9]{1,3}\)"


def parse_do_don(data):
    arr = []
    for element in re.findall(do_dons_pattern, data):
        arr.append(element)
    return arr


def extract_do(do_don_arr):
    state = "do"
    do_arr = []
    for curr in do_don_arr:
        if curr == "do":
            state = "do"
        elif curr == "don":
            state = "don"

        if state == "do" and "mul" in curr:
            do_arr.append(curr.strip())
    return do_arr


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as fp:
        return fp.read()


def parse_multiplication_instructions(data):
    mul_data = re.findall(mul_pattern, data)
    return [data.strip() for data in mul_data]


def parse_numbers_from_mul_instructions(data):
    num_ptr = list(re.findall(num_pattern, data))
    return reduce(lambda x, y: x * y, [int(x) for x in num_ptr])


def task_one(data):
    mul_ins = parse_multiplication_instructions(data)
    result = 0
    for mul_in in mul_ins:
        result += parse_numbers_from_mul_instructions(mul_in)
    return result


def task_two(data):
    data = parse_do_don(data)
    do_mul = extract_do(data)
    result = 0
    for curr_do in do_mul:
        result += parse_numbers_from_mul_instructions(curr_do)
    return result


if __name__ == "__main__":
    test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    print("Running the testing")
    print(task_one(test_str))

    print("Running the real test")
    output = read_file("./data/day_03.txt")
    print(task_one(output))

    print("Part #2")
    test_str = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    print(task_two(test_str))

    print("Running the real test")
    output = read_file("./data/day_03.txt")
    print(task_two(output))
    # do_mul = extract_do(data)
    # output = parse_numbers_from_mul_instructions(do_mul)
    # print(output)

    # output = read_file("./data/day_03.txt")
    # output = parse_multiplication_instructions(output)
    # for x in output:
    #     res = parse_numbers_from_mul_instructions(x)
    #     print(res)
    #     break
    # print(output)
