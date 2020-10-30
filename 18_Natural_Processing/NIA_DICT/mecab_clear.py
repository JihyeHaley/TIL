from mecab import *
experience = []

e = '첫 번째 단계는 측정 모형(measurement model) 검증을 통해 각 측정 변인 들이 각 잠재 변인을 제대로 측정하는지를 살핀다.' 
e = '첫 번째 단계는 측정 모형(measurement model) 검증을 통해 각 측정 변인 들이 각 잠재 변인을 제대로 측정하는지를 살핀다.' 
e = '서버로 전송된 데이터는 웹(web) 상에 그래프 형태로 게시하여 측정치의 변화를 직관적으로 확인할수 있다.'
e = '수집된 데이터는 전처리 과정(Data Pre-pressing)을 거치면서 유효한 값을 가지게 되며, 이상치 제거를 위해서 각 변수 분포의 양측 1%를 제거하고 결측치를 각 비율의 평균값으로 보정하여 유효한 데이터 셋을 구성한다.'
e = '이때는 언어적 변수(linguistic variable)로 표현되는 비계량 평가가 하나의 현실적인 방법으로 간주된다.'
e = '재생보상정리는 재생과정(renewal process)이 무한히 반복되는 상황을 가정하고 있다.'
# experience = '서버로 전송된 데이터는 웹(web) 상에 그래프 형태로 게시하여 측정치의 변화를 직관적으로 확인할수 있다.'

     
te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(e)
print(ko_words, en_words, mor_match_list_str)