lower = [chr(l) for l in range(97, 119, 1)] # a - v 까지


def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx



def html_tag_creator():
    # 꺽세 괄호 시작도 포함
    html_tag_delegates = ['p', 'span', 'a', 'b', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'hr', 'img', 'strong']
    return html_tag_delegates



