from typing import List


def is_sorted_ascending(report: List[int]) -> bool:    
    return all(1 <= (report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

def is_sorted_descending(report: List[int]) -> bool:
    return all(1 <= (report[i] - report[i + 1]) <= 3  for i in range(len(report) - 1))

def count_safe_reports(reports: List[List[int]]) -> int:
    return sum(1 for report in reports if is_sorted_ascending(report) or is_sorted_descending(report))

def get_reports():
    with open('./input.txt', 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

def is_safe_after_removal(report: List[int]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # [] + [1, 2, 3, ..., n - 1],  [0] + [2, 3, 4, ..., n - 1], ...
        if is_sorted_ascending(modified_report) or is_sorted_descending(modified_report):
            return True
    return False

def tolerate_single_level(reports: List[List[int]]) -> int:
    new_safe_reports = 0
    for report in reports:
        if is_sorted_ascending(report) or is_sorted_descending(report):
            new_safe_reports += 1
        elif is_safe_after_removal(report):
            new_safe_reports += 1
    return new_safe_reports

if __name__ == '__main__':
    reports = get_reports()
    safe_reports = count_safe_reports(reports)
    print(f'The number of safe reports is {safe_reports}')
    safe_reports_with_dampener = tolerate_single_level(reports)
    print(f'Then number of safe reports after tolerating one bad level increased to {safe_reports_with_dampener}')

"""
Keys Part-II:
    - In Python a list slice like l[:0] returns []
    - Python lists permit using slicing indices out of range (indices only not permitted)
"""
