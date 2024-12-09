from typing import List, Tuple

def read_map() -> List[List[str]]:
    with open('./input.txt', 'r') as input_file:
        return [list(line.strip()) for line in input_file]

def get_start_pos(map_: List[List[str]]) -> Tuple[int, int]:
    ROWS, COLUMNS = len(map_), len(map_[0])
    for i in range(ROWS):
        for j in range(COLUMNS):
            if is_guard(map_[i][j]):
                return i, j
    raise Exception('No guard in map')

def turnclockwise(guard_position: str) -> str:
    directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return directions.get(guard_position, None)

def get_next_dir(guard_position: str) -> str:
    direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    return direction.get(guard_position, None)

def is_guard(symbol: str) -> bool:
    return symbol in ['^', '>', 'v', '<',]

def is_out_of_map(i: int, j: int, ilimit: int, jlimit: int) -> bool:
    return i < 0 or i > ilimit or j < 0 or j > jlimit


i_initial, j_initial = get_start_pos(read_map())

def count_distinct_positions(map_: List[List[str]]) -> int:
    distinct_positions = 0
    escaped = False
    ROWS, COLUMNS = len(map_), len(map_[0])
    current_pos_i, current_pos_j = i_initial, j_initial
    current_pos = map_[current_pos_i][current_pos_j]
    distinct_positions += 1
    
    while not escaped:
        map_[current_pos_i][current_pos_j] = 'X'
        guard_position = current_pos

        next_pos_i, next_pos_j = get_next_dir(guard_position) 
        future_pos_i = current_pos_i + next_pos_i
        future_pos_j = current_pos_j + next_pos_j

        if is_out_of_map(future_pos_i, future_pos_j, ROWS - 1, COLUMNS - 1):
            escaped = True
            break
        forward_element = map_[future_pos_i][future_pos_j]
        if forward_element != '#':
            if forward_element != 'X':
                distinct_positions += 1
            current_pos_i = future_pos_i
            current_pos_j = future_pos_j
            map_[current_pos_i][current_pos_j] = current_pos
        else:
            current_pos = turnclockwise(guard_position)
    return distinct_positions

def is_cycle(map_: List[List[str]]) -> bool:
    ROWS = len(map_)
    COLUMNS = len(map_[0])
    visited = set()
    
    i, j = i_initial, j_initial
    visited.add((i, j, '^'))
    
    current_pos = map_[i][j]
    while True:
        delta_i, delta_j = get_next_dir(current_pos)
        if 0 <= i + delta_i < ROWS and 0 <= j + delta_j < COLUMNS:
            if map_[i + delta_i][j + delta_j] == '#':
                current_pos = turnclockwise(current_pos)
                map_[i][j] = current_pos
                visited.add((i, j, current_pos))
            else:
                new_i = i + delta_i
                new_j = j + delta_j
                if (new_i, new_j, current_pos) in visited:
                    return True
                visited.add((new_i, new_j, current_pos))
                map_[new_i][new_j] = current_pos
                i, j = new_i, new_j
        else:
            return False

def count_cycles(map_: List[List[str]]) -> int:
    cycles = 0
    ROWS = len(map_)
    COLUMNS = len(map_[0])

    for i in range(ROWS):
        for j in range(COLUMNS):
            if map_[i][j] in ['^', '#']:
                continue
            else:
                map_[i][j] = '#'
                if is_cycle(map_):
                    cycles += 1
                map_ = read_map() # reset map
    return cycles


if __name__ == '__main__':
    map_ = read_map()
    positions_visited = count_distinct_positions(map_)
    print(f'The guard has visited {positions_visited} distinct positions')
    map_ = read_map()
    cycles = count_cycles(map_)
    print(f'{cycles} have been found after inserting obstacles')