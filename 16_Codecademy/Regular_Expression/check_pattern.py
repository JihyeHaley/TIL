import MeCab
import re

# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    print(te)
    # return te
    # tagger = Mecab()
    # print(tagger.pos('혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'))

ex = '빠 른 생리식염수 투여를(rapid fluid administration) 하였 다.'
ex = '객담에서의 항산균 도말 검사(acid-fast bacillus smear test)와 결핵균 중합효소연쇄 반응 검사도 모두 음성이었다. '
ex = '흉수의 아데노신탈아미노효소(ade- nosinedeaminase, ADA)는 127 U/L이었다. '
ex = '패혈증 치료를 위하여 항생제(piperacillin/tazobactam)와 다량의 수액을 투여하였다. '
ex = '후두마스크(laryngeal mask airway, LMA)는 응급 상황에서의 기도유지는 물론 전신마취시에 기관내삽관을 대신하여 많이 사용되고 있다.'
start_mecab(ex)
