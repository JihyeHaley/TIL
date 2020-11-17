# nlp_ner
말뭉치 구축 프로젝트 
<br/>
python 3.6 anaconda 환경에서 개발되었습니다.

#### requirements

* requirements.txt 파일 참고
* ++ mecab설치는 `mecab_instruction_tip.md` 파일을 참고해주세요 :)

<br/><br/>

## 사용법

### 📄parser_start.py 

##### 용어사전 만들기

원문과 번역문을 파싱하여 문장단위로 단어를 추출해서 align 시켜줍니다.   

##### Usage: `python parser_start.py -r '[ROOT_PATH]' -s '[SUB_PATH]'`

**-r**:  root directory

**-s**: 분야별 폴더

<br/>

* #### **💼 Example**

1. **터미널 창에 `python parser_start.py -r '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/' -s '11.세메스' ` 입력**

   🚨주의사항 - `/Users/jihyeoh/Lexcode.... ` 형식의 PWD는 각 사용자마다 다르니 이점은 참고해서 각자에게 맞게 수정해서 입력해야한다.

2. 

   * ![image](https://user-images.githubusercontent.com/58539681/97831084-5f466d80-1d12-11eb-878c-705a9fcecdba.png)
     * **이런식으로 시작 된다면 파일을 잘 가져오는 중**
     * **각 파일 형식마다 몇 개의 파일을 가져오는지 알 수 있다.**

   

   

   * ![image](https://user-images.githubusercontent.com/58539681/97831657-08da2e80-1d14-11eb-9185-80192789c766.png)
     * **소요시간과, 문장의 개수를 확인할 수 있다.**
     * 파일 형식이 없으면 없는다고 알림이 뜨며, 이는 파일이 있는데 못가져왔거나 아예 없는 경우이기 때문에 확인해야한다.

   

   

   

   * ![image](https://user-images.githubusercontent.com/58539681/97831437-628e2900-1d13-11eb-802f-85be3a7f570d.png)
     *  `[Sub-path]_확장자명_날짜시분.xlsx ` **가 생성되면 완료된 것이다.**
     *  `[Sub-path]_log_확장자명_날짜시분.xlsx ` **는 생성된 파일들을 기록한다.**


<br/>

<br/>

### 📄pdf_parser_start.py

📍pdf 파싱은 소요시간이 굉장합니다. 따라서 사용을 권장하지는 않습니다.

##### 용어사전 만들기

원문과 번역문을 파싱하여 문장단위로 align 시켜줍니다.   

##### Usage: `python pdf_parser_start.py -r '[ROOT_PATH]' -s '[SUB_PATH]'`

**-r**:  root directory

**-s**: 분야별 폴더

* #### 💼 Example

  **터미널 창에`python pdf_parser_start.py -r '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/' -s '11.세메스' `**

  * 이후는 위의 parser_start.py와 동일하게 작동한다. (느리다)



<br/>

<br/>

## File Tree & 간단설명

<br/>

### 📂parsers

| 코드 이름               | 형식       |
| ----------------------- | ---------- |
| xlsx_parser.py          | 엑셀       |
| pptx_parser.py          | 파워포인트 |
| docx_single_parser.py   | 워드_한/영 |
| docx_mix_parser.py      | 워드_병    |
| docx_seperate_parser.py | 워드_한/영 |

<br/><br/>

### 📂utils

| 코드 이름            | 주된 목적                   |
| -------------------- | --------------------------- |
| common_functions.py  | Word 파싱위해 html로 만들기 |
| excel2word.py        | Word 파싱위해 html로 만들기 |
| read_pdf.py          | Pdf 파싱 helper             |
| regex_functions.py   | 한글/영어/특수문자 전처리   |
| sentence_splitter.py | 문장단위로 끊어주기         |
| write_file_info.py   | 어떤 파일들이 쓰였는지 정리 |

<br/><br/>

### 📄mecab.py

형태소 추출의 핵심

| VV+ETM   | MM       | XPN         | ETN           | ETM           | XSN          | XSV          | XSA            | NNB      |
| -------- | -------- | ----------- | ------------- | ------------- | ------------ | ------------ | -------------- | -------- |
|          | 관형사   | 체언 접두사 | 명사 전성어미 | 관형 전성어미 | 명사  접미사 | 동사  접미사 | 형용사  접미사 | 의존명사 |
| **NNP**  | **NNG**  | **JKO**     | **JX**        | **SSO**       | **SL**       | **SY**       | **SC**         | **SSC**  |
| 고유명사 | 일반명사 | 조사        | 보조사        | (             | 영어         | 특수문자     | 구분자         | )        |

를 활용해서 작업하기

<br/><br/>