# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

# 마지막 인덱스인지 체크
def _whether_last_idx(idx, words_list):
    length = len(words_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False