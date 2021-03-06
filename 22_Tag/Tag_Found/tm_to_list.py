import pandas as pd

############################################################
############### language 전체 to list ###############
def call_tagMT_simple():
    tm_simple_raw_data = pd.read_excel('./data/tagMT_ko_simpl.xlsx')
    path_simple_list = tm_simple_raw_data['path'].tolist()
    ko_simple_list = tm_simple_raw_data['ko'].tolist()
    en_simple_list = tm_simple_raw_data['en'].tolist()
    ja_simple_list = tm_simple_raw_data['ja'].tolist()
    
    return path_simple_list, ko_simple_list, en_simple_list, ja_simple_list

def call_tagMT_total():
    tm_total_raw_data = pd.read_excel('./data/tagMT_ko_total.xlsx')
    path_total_list = tm_total_raw_data['path'].tolist()
    ko_total_list = tm_total_raw_data['ko'].tolist()
    en_total_list = tm_total_raw_data['en'].tolist()
    ja_total_list = tm_total_raw_data['ja'].tolist()

    return path_total_list, ko_total_list, en_total_list, ja_total_list


############################################################
############### language 선택 to list ###############
def call_tagMT_simple_lan(lan):
    tm_simple_raw_data = pd.read_excel('./data/tagMT_ko_simpl.xlsx')
    path_simple_list = tm_simple_raw_data['path'].tolist()
    ko_simple_list = tm_simple_raw_data['ko'].tolist()
    en_simple_list = tm_simple_raw_data['en'].tolist()
    ja_simple_list = tm_simple_raw_data['ja'].tolist()
    
    if lan == 'ko':
        return path_simple_list, ko_simple_list
    elif lan == 'en':
        return path_simple_list, en_simple_list
    elif lan == 'ja':
        return path_simple_list, ja_simple_list

def call_tagMT_total_lan(lan):
    tm_total_raw_data = pd.read_excel('./data/tagMT_ko_total.xlsx')
    path_total_list = tm_total_raw_data['path'].tolist()
    ko_total_list = tm_total_raw_data['ko'].tolist()
    en_total_list = tm_total_raw_data['en'].tolist()
    ja_total_list = tm_total_raw_data['ja'].tolist()

    if lan == 'ko':
        return path_total_list, ko_total_list
    elif lan == 'en':
        return path_total_list, en_total_list
    elif lan == 'ja':
        return path_total_list, ja_total_list