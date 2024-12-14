import time


def check_equal_length(listA, listB):
    return len(listA) == len(listB)


def get_locations_from_file(filename):
    with open(filename) as file:
        lines = [line.strip().split("   ") for line in file]

    left, right = [], []
    for list in lines:
        left.append(int(list[0]))
        right.append(int(list[1]))

    return left, right


def main():
    start_time = time.time()
    left_list, right_list = get_locations_from_file("coordinates.txt")
    # left_list = [3, 4, 2, 1, 3, 3]
    # right_list = [4, 3, 5, 3, 9, 3]

    if not check_equal_length(left_list, right_list):
        raise Exception("Lists have different length")

    distance = 0

    left_list.sort()
    right_list.sort()

    for a, b in zip(left_list, right_list):
        distance += abs(a - b)
        print(f"A: {a}, B: {b}, {a}-{b} = {a - b} ")

    print(distance)
    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds.")


main()
