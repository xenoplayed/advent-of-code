import time


def read_coordinates_from_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def calulate_similarity_score(left_list, right_list):
    similarity_score = [value * right_list.count(value) for value in left_list]
    return sum(similarity_score)


if __name__ == "__main__":
    start_time = time.time()

    # example list
    # left_list = [3, 4, 2, 1, 3, 3]
    # right_list = [4, 3, 5, 3, 9, 3]

    file_path = "coordinates.txt"
    left_list, right_list = read_coordinates_from_file(file_path)

    print(f"similarity score: {calulate_similarity_score(left_list, right_list)}")

    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds.")
