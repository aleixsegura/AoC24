from typing import List

directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
]
word = 'XMAS'
word_len = len(word)

xmas1 = 'MAS'
xmas2 = 'SAM'

def count_mas(matrix: List[List[str]], i: int, j: int) -> int:
    right_diagonal = ''.join([matrix[i][j], matrix[i + 1][j + 1], matrix[i + 2][j + 2]])
    left_diagonal  = ''.join([matrix[i][j + 2], matrix[i + 1][j + 1], matrix[i + 2][j]])
    
    return 1 if right_diagonal in [xmas1, xmas2] and left_diagonal in [xmas1, xmas2] else 0

def count_xmasP2(matrix: List[List[str]]) -> int:
    ocurrences = 0
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if 0 <= (i + 2) < N and 0 <= (j + 2) < N:
                ocurrences += count_mas(matrix, i, j)
    return ocurrences

def save_to_matrix() -> List[List[str]]: 
    with open('./input.txt', 'r') as input_file:
         return [[c for c in line.strip()] for line in input_file] 
    
def count_xmas(matrix: List[List[str]]) -> int: 
    ocurrences = 0 
    N = len(matrix) 
    for i in range(N): 
        for j in range(N):
            for dx, dy in directions:
                if 0 <= i + (word_len - 1) * dx < N and 0 <= j + (word_len - 1) * dy < N: 
                    ocurrences += int(is_word_at_pos(matrix, i, j, dx, dy)) 
    return ocurrences 

def is_word_at_pos(matrix: List[List[str]], i: int, j: int, dx: int, dy: int) -> bool: 
    for index in range(word_len):
        if matrix[i + index * dx][j + index * dy] != word[index]:
            return False
    return True

if __name__ == '__main__':
    charmatrix = save_to_matrix()
    ocurrences = count_xmas(charmatrix) 
    print(f'Ocurrences for part I: {ocurrences}')
    occurences_P2 = count_xmasP2(charmatrix)
    print(f'Ocurrences for part II: {occurences_P2}')