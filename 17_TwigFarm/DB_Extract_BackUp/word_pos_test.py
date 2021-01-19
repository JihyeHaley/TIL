import MeCab
from konlpy.tag import Mecab
import re
import xlsxwriter
import timeit
from datetime import datetime

test_sent =  '▶경강  京江  Gyeonggang조선시대에  한성부에서  부르던,  문헌에서  사용하는  명칭의  하나이다.'

# 형태소 분석
def _start_mecab(raw_sent):
    m = Mecab()
    te = m.pos(raw_sent)
    return te
    



