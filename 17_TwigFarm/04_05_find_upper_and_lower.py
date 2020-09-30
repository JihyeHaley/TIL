def file_to_excel():
    start = timeit.default_timer()
    # -----------------------------------------------------------------------
    # file 다 져오기

    # file_name_lists = [f for f in glob.glob(f'./4.2019한국표준협회/*.*')]
    pptx_file_lists = get_filename_list(file_path, '.pptx')
#     docx_name_lists = get_filename_list(file_path, '.docx')
#     doc_name_lists = get_filename_list(file_path, '.doc')
#     ppt_name_lists = get_filename_list(file_path, '.ppt')
#     rtf_name_lists = get_filename_list(file_path, '.rtf')
#     etc_name_lists = []


#     print(file_path + f'\ndocx: {len(docx_name_lists)}, pptx: {len(pptx_name_lists)}, ppt: {len(ppt_name_lists)}, doc: {len(doc_name_lists)}, rtf: {len(rtf_name_lists)}')
    print(file_path + f'pptx: {len(pptx_name_lists)}' )
    
    # ------------------------------------------------------------------------------------
    # ppt dict 만들기
    file_lists_pptx = {}
    i = 0

    # dict에 잘 들어갔는지 test
    pptx_test_print_1 = ''
    pptx_test_print_2 = ''
    # completed_log = open(f'/Users/jihyeoh/Desktop/Farm/4_2019한국표준협회/log_36' + '.txt', "w+")
    
    # 대문자 하나만 추출될때 문장 만을어주기 위해서 
    lower, upper = lower_or_upper()
    
    # ppt 추출 시작
    print('ppt 추출 시작')
    for pptx_file_list in pptx_file_lists:
        i += 1
        # 일단 다 긁어오기 위한 list
        pptx_results_pre = []
        
        # pptx 분석 하기위해 넣어주기
        prs = Presentation(pptx_file_list)
        
        # 1개의 pptx 분석시작
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                # 전처리 및 라인별 넣어주기
                for paragraph in shape.text_frame.paragraphs:
                    if paragraph.text == "":
                        continue
                    text_list = sent_tokenize(paragraph.text)
                    for text in text_list:
                        pptx_results_pre.append(text)
                        
        pptx_results = []
        # 대, 소문자 구분해서 문장으로 만을어주기
        for idx in range(len(pptx_results_pre)):
            stop_lower_idx = 0
            found_upper_idx = 0
            finally_sentenced = ''
            print(pptx_results_pre[idx])
            if pptx_results_pre[idx][:3] == 'ver':
                stop_lower_idx = idx
                for jdx in range(idx, len(pptx_results_pre)):
                    if pptx_results_pre[jdx][0] == 'E':
                        found_upper_idx = jdx
                        finally_sentenced =  pptx_results_pre[found_upper_idx] + pptx_results_pre[stop_lower_idx]

            # del text_list[found_upper_idx]
            if idx == stop_lower_idx:
                pptx_results.append(finally_sentenced)
                # print(finally_sentenced)
            elif idx == found_upper_idx:
                continue 
            elif len(pptx_results_pre[idx]) == 1 and pptx_results_pre[idx][0] in upper:
                continue
            else:
                pptx_results.append(pptx_results_pre[idx])
        
        pptx_results = list(filter(None, pptx_results))

        if i == 1:
            pptx_test_print_1 = pptx_file_list[50:-5]
        elif i == 2:
            pptx_test_print_2 = pptx_file_list[50:-5]
        else:
            print(i, end=" ")

        file_lists_pptx[pptx_file_list[50:-5]] = pptx_results
        

    #     completed_log.write(str(i) + ' \n' + str(pptx_results) + ' \n ')
    # completed_log.close()
    print(f'done, file_lists_pptx : is {len(file_lists_pptx)}')
    print(file_lists_pptx.get(pptx_test_print_1))
    print(file_lists_pptx.get(pptx_test_print_2))
    print(f'pptx는 {i}개 가져왔어요')
    # completed_log.close()
    
    
    # ------------------------------------------------------------------------------------
    # docx dict 만들기
    # 잠시보류
#     file_lists_docx = {}
    
    # ------------------------------------------------------------------------------------
    # docx와, pptx merging
    file_lists_all = {}
    file_lists_all.update(file_lists_pptx)
#     file_lists_all.update(file_lists_docx)
    print(f'total length is : {len(file_lists_all)}')
    # print(list(file_lists_all.keys()))
    
    
    

    # ------------------------------------------------------------------------------------
    # log 출력 (파일명 확인하기 위해서)
    completed_log = open(f'/Users/jihyeoh/Desktop/Farm/4_2019한국표준협회/log_stabdard_36' + '.txt', "w+")
    

    # ------------------------------------------------------------------------------------
    # 한글, 영어 구분해서 각각의 dict에 넣어주기
    ko_files = {}
    en_files = {}
    

    i = 0
    j = 1
    for key, value in file_lists_all.items():
        i += 1
        print(key) 
        language = key[-1]
        key_name = key[:-2]
        print(key_name)
        
        if language == '한':
            ko_files.update({key_name : value})
            print(f'{key[:-2]}, {key_name}, {language}')
            completed_log.write(str(i) + '_[한. DONE READING]' + key_name + ' \n')
        elif language == '영':
            en_files.update({key_name : value})
            print(f'{key[:-2]}, {key_name}, {language}')
            completed_log.write(str(i) + '_[영. DONE READING]' + key_name + ' \n')
        elif language == '병':
            completed_log.write(str(i) + '_[병. DONE READING]' + key_name + ' \n')
        else:
            print('지금 잘 안되고 있어요. 코드 수정필요')
            print(f'{key[:-2]}, {key_name}, {language}')
    
    
    print(list(ko_files.keys()))
    print(list(en_files.keys()))
    

    completed_log.write(f'[DONE READING Total] 한:{str(len(en_files))} 영:{str(len(ko_files))}')
    completed_log.close()

    
    # ------------------------------------------------------------------------------------
    # excel 밖으로 빼내기
    workbook = xlsxwriter.Workbook('/Users/jihyeoh/Desktop/Farm/4_2019한국표준협회/4_xlsx/standard36_.xlsx')
    print('excel 빼내기 파일생성 성공!')
    worksheet = workbook.add_worksheet()
    worksheet.write('B1', 'ko')
    worksheet.write('C1', 'en')
    
    row_idx = 2
    
    i = 0
    

    # ------------------------------------------------------------------------------------
    # excel 글쓰기

    for ko_key, ko_value in ko_files.items():
        for en_key, en_value in en_files.items():
            if ko_key == en_key:
                i += 1
                print(f'{i}-{ko_key}')
                print(f'{i}-{en_key}')
                worksheet.write('A' + str(row_idx), '>'*10 + ko_key)
                row_idx += 1
                for ko, en in zip_longest(ko_value, en_value, fillvalue=' '):
                    ko_index = get_excel_index('ko', row_idx)
                    en_index = get_excel_index('en', row_idx)
                    worksheet.write(ko_index, ko)
                    worksheet.write(en_index, en)
                    row_idx += 1
          
    workbook.close()
    stop = timeit.default_timer()
    
    print('Running Time: ', stop - start)