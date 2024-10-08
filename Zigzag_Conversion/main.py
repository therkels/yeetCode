def convert(s: str, numRows: int) -> str:
    display_matrix = [[] for i in range(numRows)]
    pos = 0
    is_up = False

    for char in s:
        if pos <= 0:
            pos = 0
            is_up = False
        if pos < numRows and not is_up:
            display_matrix[pos].append(char)
            pos += 1
        elif pos > 0 and is_up:
            display_matrix[pos].append(char)
            pos -= 1
        if pos == numRows:
            is_up = True
            pos -= 2
    
    ret_str = []
    for i in display_matrix:
        ret_str.extend(i)
    return "".join(ret_str)

print(convert("A", numRows=1))