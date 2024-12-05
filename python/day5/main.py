from typing import List, Tuple

def parse_input_file() -> Tuple[List[str], List[str]]:
    ordering, updates = [], []
    update_part = False
    with open('./input.txt', 'r') as input_file:
        for line in input_file:
            if line == '\n':
                update_part = True
                continue
            ordering.append(line.strip()) if not update_part \
                else updates.append(line.strip().split(','))
    return ordering, updates

def is_valid(update: str, ordering: List[str]) -> bool:
    for i in range(len(update) - 1):
        current = update[i]
        for j in range(i + 1, len(update)): 
            compare_to = update[j]
            comparison = f'{current}|{compare_to}'
            if comparison not in ordering: 
                return False
    return True

def get_next_priority_page(update: List[str], ordering: List[str]) -> str:
    for current in update:
        if all(f'{current}|{compared}' in ordering for compared in update if current != compared):
            return current
    return ''

def correct(ordering: List[str], unvalid_updates: List[List[str]]) -> List[List[str]]:
    corrected = []
    for update in unvalid_updates:
        options = list(update)
        ordered = []
        while options:
            priority_page = get_next_priority_page(options, ordering)
            ordered.append(priority_page)
            options.remove(priority_page)
        corrected.append(ordered)
    return corrected
                 
def filter_valid(ordering: List[str], updates: List[List[str]]) -> List[List[str]]:
    return [update for update in updates if is_valid(update, ordering)]

def filter_invalid(ordering: List[str], updates: List[List[str]]) -> List[List[str]]:
    return [update for update in updates if not is_valid(update, ordering)]

def sum_medians(updates: List[str]) -> int:
    return sum(int(update[(len(update) // 2)]) for update in updates)

if __name__ == '__main__':
    ordering, updates = parse_input_file()
    valid_updates = filter_valid(ordering, updates)
    p1_result = sum_medians(valid_updates)
    print(f'Result of Part I = {p1_result}')
    unvalid_updates = filter_invalid(ordering, updates)
    corrected_updates = correct(ordering, unvalid_updates)
    p2_result = sum_medians(corrected_updates)
    print(f'Result of Part II = {p2_result}')
