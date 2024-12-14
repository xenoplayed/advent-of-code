import time


def check_equal_length(listA, listB):
    return len(listA) == len(listB)


def extract_smalles_number(list):
    smallest_number = min(list)
    index = list.index(smallest_number)
    return list.pop(index)


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

    if not check_equal_length(left_list, right_list):
        raise Exception("Lists have different length")

    distances = []

    for _ in range(len(left_list)):
        x = extract_smalles_number(left_list)
        y = extract_smalles_number(right_list)

        # if x > y:
        #     print(f"{x}-{y} = {x-y}")
        #     distances.append(x-y)
        # else:
        #     print(f"{y}-{x} = {y-x}")
        #     distances.append(y-x)

        print(f"{x}-{y} = {x - y}")
        distances.append(abs(x - y))

    total_distance = sum(distances)
    print(total_distance)
    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds.")


main()
