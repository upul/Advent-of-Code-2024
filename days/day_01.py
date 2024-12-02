from collections import Counter
from typing import List, Tuple


def read_data(file: str) -> Tuple[List[int], List[int]]:
    """
    Reads a file containing pairs of integers on each line, separated by whitespace,
    and returns two lists: one with the first integers of each pair
    and another with the second integers.

    Args:
        file (str): The path to the input file. Each line in the file should contain two integers
                    separated by whitespace.

    Returns:
        tuple: A tuple containing two lists:
            - The first list contains the first integers from each line.
            - The second list contains the second integers from each line.
    """
    with open(file, "r", encoding="UTF-8") as fp:
        data = fp.readlines()

    left, right = zip(*(map(int, line.split()) for line in data))
    return list(left), list(right)


def total_distance_diff(left: List[int], right: List[int]) -> int:
    """
    Calculates the total distance difference between two lists of integers by sorting both lists
    and summing the absolute differences between corresponding elements.

    Args:
        left (List[int]): A list of integers representing the first set of values.
        right (List[int]): A list of integers representing the second set of values.

    Returns:
        int: The sum of the absolute differences between corresponding elements
        of the two sorted lists.
    """
    left = sorted(left)
    right = sorted(right)
    return sum([abs(l - r) for l, r in zip(left, right)])


def calculate_similarity_score(left: List[int], right: List[int]) -> int:
    """
    Calculates a similarity score based on the product of elements from the `left` list and their
    frequencies in the `right` list.

    The function counts the occurrences of each element in the `right` list using a `Counter`.
    It then iterates through the `left` list, adding the product of each element and its frequency
    in the `right` list to the similarity score.

    Args:
        left (List[int]): A list of integers representing the first set of values.
        right (List[int]): A list of integers representing the second set of values.

    Returns:
        int: The calculated similarity score.
    """
    right_counter = Counter(right)

    sim_score = 0
    for left_number in left:
        sim_score += left_number * right_counter[left_number]
    return sim_score


def process_dataset(file_path: str, label: str) -> None:
    """
    Processes a dataset by reading the data, calculating the total distance difference,
    and computing the similarity score.

    Args:
        file_path (str): Path to the dataset file.
        label (str): Label to identify the dataset (e.g., "Test Dataset", "Day #1 Dataset").
    """
    left, right = read_data(file_path)
    tot_diff = total_distance_diff(left, right)
    similarity_score = calculate_similarity_score(left, right)

    print(f"{label} total difference: {tot_diff}")
    print(f"{label} similarity score: {similarity_score}\n")


if __name__ == "__main__":
    # Define dataset paths
    datasets = {
        "Test Dataset": "./data/tests/day_01.txt",
        "Day #1 Dataset": "./data/day_01.txt",
    }

    # Process each dataset
    for label, file_path in datasets.items():
        print(f"Processing {label}...")
        process_dataset(file_path, label)
