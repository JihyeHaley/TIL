import os
import timeit
import xlsxwriter
import pandas as pd
# from io import StringIO
# from konlpy.tag import Mecab
from datetime import datetime 


class First:
    def _excel_index_creator(self, column, row_idx):
        cell_idx  = column + str(row_idx)
        return cell_idx 


    def analyze(self, sheet_names):
        file_name = '퀄리과제과제과제.xlsx' # str
        start = timeit.default_timer()
        for sheetname in sheet_names:
            df = pd.read_excel(file_name, sheet_name = sheetname)
            
            timestamp = datetime.now().strftime('%m%d%H%M')
            workbook = xlsxwriter.Workbook('./results/' +  sheetname  + '_'  + timestamp +'.xlsx') 
            yellow_cell = workbook.add_format()
            yellow_cell.set_pattern(1)
            yellow_cell.set_bg_color('yellow')

            ########################################################################################
            # <!-- simple analysis START-->
            worksheet_simple = workbook.add_worksheet('simple_analysis')
            worksheet_simple.write('A1', 'No', yellow_cell)
            worksheet_simple.write('B1', 'Script', yellow_cell)
            scripts = df['script'].tolist()

            # Script 작성
            for idx, script in enumerate(scripts):
                a_idx = self._excel_index_creator('A', idx+2)
                b_idx = self._excel_index_creator('B', idx+2)
                worksheet_simple.write(a_idx, str(idx + 1))
                worksheet_simple.write(b_idx, script)


            worksheet_simple.write('C1', 'Topic_1', yellow_cell)
            worksheet_simple.write('D1', 'Topic_2', yellow_cell)
            worksheet_simple.write('E1', 'Topic_3', yellow_cell)
            
            first_topic = df['first'].tolist()
            first_topic = [i.lower() for i in first_topic]
            
            # Topic 1
            company_name = sheetname.split('_')[-1]
            esg_in_second_dict = {}
            chat_in_second_dict = {}
            company_in_second_dict = {}

            esg_in_second_idx = {}
            chat_in_second_idx = {}
            company_in_second_idx = {}

            first_dict = {'ESG':[0, esg_in_second_dict, esg_in_second_idx], company_name:[0, company_in_second_dict, company_in_second_idx], 'Chatting':[0, chat_in_second_dict, chat_in_second_idx]}
            org_first_dict = {'ESG':0, company_name:0, 'Chatting':0}
            first_topic_cell = ''
            for idx, each in enumerate(first_topic):
                if 'esg' in each:
                    first_dict['ESG'][0] += 1
                    org_first_dict['ESG'] += 1
                    first_topic_cell = 'ESG'
                    if each not in first_dict['ESG'][1]:
                        first_dict['ESG'][1][each] = 1
                        first_dict['ESG'][2][each] = []
                        first_dict['ESG'][2][each].append(idx)
                    elif each in first_dict['ESG'][1]:
                        first_dict['ESG'][1][each] += 1
                        first_dict['ESG'][2][each].append(idx)

                elif 'chatting' in each or 'thank' in each:
                    first_dict['Chatting'][0] += 1
                    org_first_dict['Chatting'] += 1
                    first_topic_cell = 'Chatting'
                    if each not in first_dict['Chatting'][1]:
                        first_dict['Chatting'][1][each] = 1
                        first_dict['Chatting'][2][each] = []
                        first_dict['Chatting'][2][each].append(idx)
                    elif each in first_dict['Chatting'][1]:
                        first_dict['Chatting'][1][each] += 1
                        first_dict['Chatting'][2][each].append(idx)
                else:
                    first_dict[company_name][0] += 1
                    org_first_dict[company_name] += 1
                    first_topic_cell = company_name
                    if each not in first_dict[company_name][1]:
                        first_dict[company_name][1][each] = 1
                        first_dict[company_name][2][each] = []
                        first_dict[company_name][2][each].append(idx)
                    elif each in first_dict[company_name][1]:
                        first_dict[company_name][1][each] += 1
                        first_dict[company_name][2][each].append(idx)
                # EXCEL WRITE
                c_idx = self._excel_index_creator('C', idx+2)
                worksheet_simple.write(c_idx, first_topic_cell)
            
            # topic 별로 나누기
            worksheet_1_2 = workbook.add_worksheet('topic_1_2')
            worksheet_1_2.write('A1', 'No', yellow_cell)
            worksheet_1_2.write('B1', 'Topic_1', yellow_cell)
            worksheet_1_2.write('C1', 'Topic_2', yellow_cell)
            worksheet_1_2.write('D1', 'Script', yellow_cell)
            row_idx =2

            for key, value in first_dict.items():
                dict_script_idx = 0
                for key_2, value_2 in first_dict[key][2].items():
                    for idx in range(len(first_dict[key][2][key_2])):
                        # no.
                        a_idx = self._excel_index_creator('A', row_idx)
                        worksheet_1_2.write(a_idx, str(row_idx-1))
                        
                        # topic 1
                        b_idx = self._excel_index_creator('B', row_idx)
                        worksheet_1_2.write(b_idx, key)

                        # topic 2
                        c_idx = self._excel_index_creator('C', row_idx)
                        worksheet_1_2.write(c_idx, key_2)

                        script_idx = first_dict[key][2][key_2][idx]
                        d_idx = self._excel_index_creator('D', row_idx)
                        worksheet_1_2.write(d_idx, scripts[script_idx])
                        row_idx += 1

            print(sheetname)
            for key, value in org_first_dict.items():
                print(f'\t{key}: {value}')



            # Topic 2
            second_dict = {}
            second_dict_idx = {}
            
            for jdx, second_topic in enumerate(first_topic):
                if second_topic not in second_dict:
                    second_dict[second_topic] = 1
                    # script idx 기억해서 script 넣어주기
                    second_dict_idx[second_topic] = []
                    second_dict_idx[second_topic].append(jdx) 
                elif second_topic in second_dict:
                    second_dict[second_topic] += 1
                    # script idx 기억해서 script 넣어주기
                    second_dict_idx[second_topic].append(jdx)

                # EXCEL WRITE
                d_idx = self._excel_index_creator('D', jdx+2)
                worksheet_simple.write(d_idx, second_topic)

            #####################
            # 소중한 통계 txt로 빼내기
            print(f'\t\t->topic_cnt - {len(second_dict)}')
            print('#'*40)
            second_topic_log = open(f'./results/' + sheetname+ '_second_topic_log_' + timestamp + '.txt', "w+")
            for key, value in second_dict.items():
                second_topic_log.write(key + '\t' + str(value) + '\n')
            second_topic_log.write('\n' + 'Total_Topic_cnt' + '\t' + str(len(second_dict)) + '\n')
            second_topic_log.close()

            #####################
            # 소중한 통계 Excel로 빼내기
            # print(f'{sheetname}: topic_cnt - {len(second_dict)}')
            # second_topic_log = open(f'./results/' + sheetname+ '_second_topic_log_' + timestamp + '.txt', "w+")
            # for key, value in second_dict.items():
            #     second_topic_log.write(key + '\t' + str(value) + '\n')
            # second_topic_log.write('\n' + 'Total_Topic_cnt' + '\t' + str(len(second_dict)) + '\n')
            # second_topic_log.close()


            # <!-- simple analysis END-->
            ########################################################################################

            # Topic 3
            # key - second_topic
            # value - total_cnt
            for second_topic, total_cnt in second_dict.items():
                worksheet_sepecific = workbook.add_worksheet(second_topic)
                worksheet_sepecific.write('A1', 'No', yellow_cell)
                worksheet_sepecific.write('B1', 'Script', yellow_cell)
                worksheet_sepecific.write('C1', 'Topic_3', yellow_cell)
                for enumerate_idx, script_idx in enumerate(second_dict_idx[second_topic]):
                    a_idx = self._excel_index_creator('A', enumerate_idx + 2)
                    b_idx = self._excel_index_creator('B', enumerate_idx + 2)
                    worksheet_sepecific.write(a_idx, str(enumerate_idx + 1))
                    worksheet_sepecific.write(b_idx, scripts[script_idx])
            workbook.close()
        stop = timeit.default_timer()

        print(f'RUNNING TIME : {stop - start}')


first_class = First()
sheet_names = ['ESG1_한화', 'ESG2_현대자동차', 'ESG3_Deloitte']
first_class.analyze(sheet_names) 


