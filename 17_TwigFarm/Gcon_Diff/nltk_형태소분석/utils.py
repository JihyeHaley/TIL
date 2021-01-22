import mammoth

def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


# mammoth 사용하여 docx raw test parsing
def in_docx_to_raw_text(file_name):
    with open(f'./{file_name}.docx', 'rb') as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
    
    contents = text.split('\n')

    return contents



