from collections import Counter


def read_data(file):
    with open(file, "r") as fp:
        raw_data = fp.readlines()

    left, right = [], []
    for line in raw_data:
        splitted = line.split()
        left_str = splitted[0].strip()
        right_str = splitted[1].strip()

        left.append(int(left_str))
        right.append(int(right_str))

    return left, right


def total_distance_diff(left, right):
    left = sorted(left)
    right = sorted(right)
    return sum([abs(l - r) for l, r in zip(left, right)])


def calculate_similarity_score(left, right):
    right_counter = Counter(right)

    sim_score = 0
    for left_number in left:
        sim_score += left_number * right_counter[left_number]
    return sim_score


if __name__ == "__main__":
    #  working with the testing dataset
    left, right = read_data("./data/tests/day_01.txt")
    tot_diff = total_distance_diff(left, right)
    print(f"Test dataset total deference: {tot_diff}")

    # similarity score calculator
    print("Calculating similarity scores")
    print(f"Test Dataset: {calculate_similarity_score(left, right)}")

    # working with the real dataset
    left, right = read_data("./data/day_01.txt")
    tot_diff = total_distance_diff(left, right)
    print(f"Day # 1, dataset total deference: {tot_diff}")

    # similarity score calculator
    print("Calculating similarity scores")
    print(f"Day #1 Dataset: {calculate_similarity_score(left, right)}")
