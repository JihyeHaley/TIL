from konlpy.tag import Mecab

mecab = Mecab()
sent = '안녕하세요, 지혜입니다.'
sent = mecab.pos(sent)
