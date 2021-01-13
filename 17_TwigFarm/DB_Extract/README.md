# DB_한국하천지명 단어 추출

<br/>
python 3.6 anaconda 환경에서 개발되었습니다.

#### requirements

* requirements.txt 파일 참고

  ++ mecab설치는 `mecab_instruction_tip.md` 파일을 참고해주세요 :)

<br/><br/>

## 사용법

### 📄pdf_parser_start.py 


원문과 번역문을 파싱하여 문장단위로 단어를 추출해서 align 시켜줍니다.   

##### Usage: `python pdf_parser_start.py -s '[SUB_PATH]' -r '[ROOT_PATH]' `

**-r**:  절대경로(Root)

**-s**: 분야별 폴더

<br/>

* #### **Example**

1. ** `python pdf_parser_start.py -s "db_pdf" -r '/Users/haley/Desktop/Git/TIL/17_Twigfarm/DB_Extract/' ` **

   🚨 주의사항 - `/Users/haley/Desktop.... ` 형식의 path는 각 사용자마다 다르니 이점은 참고해서 각자에게 맞게 수정해서 입력해야한다.

   🚨 PDF파싱은 시간이 다소 소요됩니다.

2. 

   ![image](https://user-images.githubusercontent.com/58539681/104439401-68866d00-55d4-11eb-8193-3e3c8649c1e7.png)

   * PDF 작업 시작 유무, 개수가 보이면 파일을 가져와서 파싱작업하는 중입니다.

3. `./results/sub_path` 폴더 안에 완료된 파일을 확인할 수 있다.

   ![image](https://user-images.githubusercontent.com/58539681/104439504-848a0e80-55d4-11eb-962e-9f7d1a2fee86.png)

<br/>

<br/>

* #### 💼 Example

  **터미널 창에`python pdf_parser_start.py -r '/Users/haley/desktop/일본어_파싱/' -s '이노룰스 번역본 문서 (일본어)/' `**

  * 이후는 위의 parser_start.py와 동일하게 작동한다. (느리다)

<br/>

<br/>

## 📂File Tree & 간단설명

<br/>

| 코드 이름                 | 형식                                           |
| ------------------------- | ---------------------------------------------- |
| work_start.py             | **작업 시작** file open, parsing, word_extract |
| extract_check_to_excel.py | list -> 형태소 분석, 추출 -> excel             |
| parser_docx.py            | docx -> list                                   |
| parser_pdf.py             | pdf -> list                                    |
| parser_pptx.py            | pptx -> list                                   |
| parser_xlsx.py            | xlsx -> list                                   |

<br/>

**/utils**

| utils.common_functions.py | **여러 곳**에서 공통으로 쓰이는 공통 함수 |
| ------------------------- | ----------------------------------------- |
| utils.docx_utils.py       | **docx 파싱**을 위한 함수                 |
| utils.pdf_utils.py        | **pdf 파싱**을 위한 함수                  |
| utils.pptx_utils.py       | **pptx 파싱**을 위한 함수                 |
| utils.word_pos_utils.py   | **형태소 분석**에 필요한  함수            |

<br/>