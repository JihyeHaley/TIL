import re
# from nltk.tokenize import LineTokenizer, Spacetokenizer, TweetTokenizer
# from nltk import word_tokenize

def find_English(sent):
    sp_english_sp = '(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)'
    match = re.findall(sp_english_sp, sent)
    
    return match

# def find_Korean(sent):
#     match, terminated = find_English(sent)
#     return_times = len(match)
#     print(return_times)
#     eng_at_least = '3,'
#     korean_sp_english_sp = f'((([ㄱ-ㅣ가-힣]+)\s?)\s?){return_times}(\s?\(?(([a-zA-Z]){eng_at_least}\s*){return_times}+\)?)'
#     match = re.findall(korean_sp_english_sp, sent)
#     return match

def find_pattern(sent):
    # rabbit = '((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'
    match = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)', sent)
    return match


rabbit = r'((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'