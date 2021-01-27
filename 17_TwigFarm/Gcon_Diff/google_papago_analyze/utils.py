import nltk

from tensorflow.keras.preprocessing.text import text_to_word_sequence

def _work_mor_analyze(sent):
    # 단어만 남기기
    words_list = text_to_word_sequence(sent) # [Hi, My, name, is, jihye] (문장의 첫 단어도 )
    
    # 단어와 형태소 List
    words_mor_list = nltk.tag.pos_tag(words_list) # [(Hi, NNG), ...] 

    # # 형태소만 
    # mors_list = list()
    # for each_mor in words_mor_list:
    #     mors_list.append(each_mor[1]) # [NNG, NNP, VB ...]

    return words_list, words_mor_list


def _show_mor(idx, en_google_list, en_papago_list):
    google_words, google_words_mors = _work_mor_analyze(en_google_list[idx])
    papago_words, papag_words_mors = _work_mor_analyze(en_papago_list[idx])
    return google_words, google_words_mors, papago_words, papag_words_mors



    


