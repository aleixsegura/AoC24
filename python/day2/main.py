"""
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

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