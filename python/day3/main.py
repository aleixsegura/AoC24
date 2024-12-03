import re
from typing import List, Tuple

def extract_raw() -> str:
    with open('./input.txt', 'r') as file:
        t = file.read()
    return t

def extract_p1_ops(t: str) -> List[Tuple[str, str]]: 
    return re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', t)

def operate(ops: List[Tuple[int, int]]) -> int:
    return sum(int(x) * int(y) for x, y in ops)

def extract_p2_ops(t: str) -> List[Tuple[str, str]]:
    t_pre_dont  = t[:t.find("don't()")]
    p2_ops = extract_p1_ops(t_pre_dont)
    
    t_post_dont = t[t.find("don't()"):]
    while 'do()' in t_post_dont and "don't()" in t_post_dont:
        do_idx = t_post_dont.find('do()')
        do_len = len('do()')
        t_post_dont = t_post_dont.replace(t_post_dont[:do_idx + do_len], '')
        validtext = t_post_dont[:t_post_dont.find("don't()")]
        p2_ops.extend(re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', validtext))
        t_post_dont = t_post_dont.replace(validtext, '')
    return p2_ops

if __name__ == '__main__':
    raw_text = extract_raw()
    p1_ops = extract_p1_ops(raw_text)
    p1_result = operate(p1_ops)
    print(f'Result of part I is {p1_result}')
    p2_ops = extract_p2_ops(raw_text)
    p2_result = operate(p2_ops)
    print(f'Result of part II is {p2_result}')
