from typing import Tuple, List
from collections import Counter

def get_lists() -> Tuple[List[int], List[int]]:
    left, right = [], []
    with open('./input.txt', 'r') as file:
        for line in file:
            left_value  = int(line[:5])
            right_value = int(line[-6:])
            left.append(left_value)
            right.append(right_value)
    return left, right

def get_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

def get_similarity(left: list[int], right: list[int]) -> int:
    right_count = Counter(right)
    return sum(val * right_count[val] for val in left)    

if __name__ == '__main__':
    left, right = get_lists()
    distance = get_distance(left, right)
    print(f'The distance between the lists is {distance}')
    similarity = get_similarity(left, right)
    print(f'The similarity score between the lists is {similarity}')

