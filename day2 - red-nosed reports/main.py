import time

# The unusual data (your puzzle input) consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces.
example_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def read_reports_from_file(file_path):
    with open(file_path, "r") as file:
        raw_data = f"""{file.read()}"""
    return raw_data


def parse_reports(raw_data):
    # 1. Get all line, if line is not empty
    # 2. Get numbers from line and convert to integer
    reports = [[int(report) for report in line.split()] for line in raw_data.split("\n") if line]
    return reports


def test_reports(reports):
    safe_reports = [report for report in reports if is_ordered(report)]
    num_safe_reports = len([report for report in safe_reports if is_safe(report)])
    return num_safe_reports


def is_ordered(report):  # Todo: replace sorted() with all()
    if report == sorted(report, reverse=False):
        return True
    if report == sorted(report, reverse=True):
        return True
    return False


def is_safe(report):
    adjacent_levels = [levels for levels in zip(report, report[1:])]  # create list with adjacent levels: [1,2,3,4] -> [1,2],[2,3],[3,4]
    adjacent_levels_distance = [abs(adjacent[0] - adjacent[1]) for adjacent in adjacent_levels]  # calculate distance between levels
    is_safe = all([(distance >= 1 and distance <= 3) for distance in adjacent_levels_distance])
    return is_safe


if __name__ == "__main__":
    file_path = "reports.txt"

    # part 1 - start
    start1_time = time.time()

    reports_data = read_reports_from_file(file_path)
    reports = parse_reports(reports_data)
    safe_reports = test_reports(reports)

    print(f"Number of safe reports: {safe_reports}")
    end1_time = time.time()
    print(f"Runtime part 1: {end1_time - start1_time} seconds.")
    # part 1 - end
