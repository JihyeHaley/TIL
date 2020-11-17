# nlp_corpus
말뭉치 구축 프로젝트 
<br />
<br />
python 3.6 anaconda 환경에서 개발되었습니다.
<br />

## Running sample script
### TM parsers
원문과 번역문을 파싱하여 문장단위로 align 시켜줍니다.   

##### Usage: parser_start.py -s SUB_PATH [-r DIR_TYPE]
**-s**: 분야별 폴더    
**-r**: 용도별 root directory **[TM | AD(원문) | manual root_dir]** - <font color='blue'> optional </font>
   1. for TM: `$HOME/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)`   
   2. for AD: `$HOME/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/3.학술정보/`
  
##### Example
1. One drive 연결하여 사용시: `python parser_start.py -r "TM" -s "1. 2018한국관광공사"`
2. Local에서 사용시: `python parser_start.py -r "/Users/twigfarm/mydoc/" -s "1. 2018한국관광공사"`
<br />
<br />

### pdf parsers
기술문서 pdf 원문을 파싱하여 엑셀파일로 만들어 줍니다.   

##### Usage: pdf_parser_start.py [-r ROOT_PATH] -s SUB_PATH
**-s**: 분야별 폴더   
**-r**: root directory (default: `$HOME/주식회사 트위그팜/NIA - 01_원문/`) - <font color='blue'>optional</font>
<br />

##### Example
1. One drive 연결하여 사용시: `python pdf_parser_start.py -s "사회과학"`
2. Local에서 사용시: `python pdf_parser_start.py -r "/Users/twigfarm/mydoc/" -s "사회과학"`

