# ------------------------------------------------------------------------------------
    # docx dict 만들기
    print('docx 추출 시작')
    file_lists_docx = {}
    i = 0
    
    # dict에 잘 들어갔는지 test
    docx_test_print_1 = ''
    
    # docx 추출 시작
    for docx_name_list in docx_name_lists:
        i += 1
        # 일단 다 긁어오기 위한 list
        docx_results_pre = []
        with open(docx_name_list, "rb") as docx_file:
            result = mammoth.extract_raw_text(docx_file)
            value = result.value  # The raw text
            text_list= sent_tokenize(value)
            for text in text_list:
                if text == "":
                    continue
                docx_results_pre.append(text)

        docx_results= reg_raw_text(docx_results_pre)
        docx_results = list(filter(None, docx_results))

        if i == 1:
            docx_test_print_1 = docx_name_list[40:-5]
        else:
            print(i, end=' ')

        file_lists_docx[docx_name_list[40:-5]] = docx_results

    print(f'done, file_lists_docx : is {len(file_lists_docx)}')
    print(file_lists_docx.get(docx_test_print_1))
    print(f'docx는 {i}개 가져왔어요')