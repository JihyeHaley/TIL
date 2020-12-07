# Tag Extractor 사용법
<br>

#### simple data
1. `python tm_friend_simple.py` 입력

2. `ko`, `en`, `ja` 중 추출하고 싶은 언어 입력

3. 결과물 시간, 에러 확인 
   take: N
   error_cnt: N
   error_chunk: N

   normal_cnt: N
   normal_chunk: N

<br>

#### total data

1. `python tm_friend_total.py` 입력

2. `ko`, `en`, `ja` 중 추출하고 싶은 언어 입력

3. 결과물 시간, 에러 확인 
   take: N
   error_cnt: N
   error_chunk: N

   normal_cnt: N
   normal_chunk: N

<br><br>

## 파일 설명

##### common_function.py

* excel_index_creator(column, row_idx)
  * excel index 생성
* html_tag_creator()
  * text를 포함하는 대표 tag를 포함하는 리스트 생성

##### tag_extrctor.py

* stack_extractor(sent)
  * 자료구조 STACK(LIFO)를 활용한 태그 추출 함수

##### tm_friend_simple.py

* simple 데이터 추출하는 main
  * ko, en, ja를 입력하고 원하는 언어 추출 가능

##### tm_friend_total.py

* total 데이터 추출하는 main
  * ko, en, ja를 입력하고 원하는 언어 추출 가능

##### tm_to_list.py

* excel(raw tm) to list



## 결과

| simple                                                       | total                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **simple_ko**<br />take: 4.079736744 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 4001 <br />normal_chunk: 12609 | **total_ko**<br />take: 13.674640512 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 9964 <br />normal_chunk: 20367 |
| **simple_en**<br />take: 4.492487446 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 4001 <br />normal_chunk: 14473 | **total_en**<br />take: 12.665452307 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 9964 <br />normal_chunk: 22419 |
| **simple_ja**<br />take: 4.361901007 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 4001 <br />normal_chunk: 12693 | **total_ja**<br />take: 12.088039841 <br />error_cnt: 0 <br />error_chunk: 0<br />normal_cnt: 9964 <br />normal_chunk: 20539 |

