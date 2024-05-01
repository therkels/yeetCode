def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return str
    arr_2d = [[] for i in range(numRows)]
    row_idx = 0
    trail_up = False
    for pos, s in enumerate(s):
        if row_idx < numRows and not trail_up:
            arr_2d[row_idx].append(s)
            row_idx += 1

            if row_idx == numRows:
                trail_up = True
                row_idx -= 1
        else:
            if row_idx != 0:
                row_idx -= 1
                arr_2d[row_idx].append(s)

            if row_idx == 0:
                trail_up = False
                row_idx += 1
    ret_str = ''
    for ele in arr_2d:
        ret_str += "".join(ele)
    return ret_str