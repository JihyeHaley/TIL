## nltk.LineTokenizer(), nltk.SpaceTokenizer(), nltk.TweetTokenizer()

## word_tokenize()

`from nltk.tokenize import LineTokenizer, Spacetokenizer, TweetTokenizer`

`from nltk import word_tokenize`

##### LineTokenizer()

* 클래스

- 입력 문자열을 *<u>**줄**</u>* 로 나눈 것

- ```python
  rawText = 'My name is Haley. I have two younser sisters.'
  lTokenizer = LineTokenizer()
  print(lTokenizer.tokenize(rawText))
  ```

  ['My name is Haley.', 'I have two younser sisters.']



##### TweetTokenizer

* 클래스

* 특수문자를 다룰 때

* ```python
  rawText = 'This is a cooool #dummysmiley: :-) :-P <3'
  tTokenizer = TweetTokenizer()
  print(tTokenizer.tokenize(rawText))
  ```

  ['This', 'is', 'a', 'cooool', '#dummysmiley', ':', ':-)', ':-P', '<3']

*  이모티콘도 원형을 잃지 않고 유지되고 있다. 





#### SpaceTokenizer() vs word_tokenize

| SpaceTokenizer()                              | word_tokenize                             |
| --------------------------------------------- | ----------------------------------------- |
| Class                                         | nltk의 method                             |
| 단어, 구두점(문장부호) **구분없이** 되어 출력 | 단어, 구두점(문장부호) **구분** 되어 출력 |
|                                               |                                           |

##### SpaceTokenizer()

* 클래스

- 공백 문자로 나눠 분활

- ```python
  rawText = 'By 11 o\'clock on Sunday, the doctor shall open the dispensary.'
  sTokenizer = SpaceTokenizer()
  print(sTokenizer.tokenize(rawText))
  ```

  ['By', '11', 'o\'clock', 'on', 'Sunday,', 'the', 'doctor', 'shall', 'open', 'the', 'dispensary.']



##### word_tokenize

* nltk의 method

* ```python
  rawText = 'By 11 o\'clock on Sunday, the doctor shall open the dispensary.'
  print(word_tokenize(rawText))
  ```

  ['By', '11', 'o\'clock', 'on', 'Sunday', ',' ,'the', 'doctor', 'shall', 'open', 'the', 'dispensary', '.']



## Stemmer

##### 어간의 개념과 스테밍 과정.

##### nltk의 내장 스테밍 클래스를 이용

##### *어간 = 접미사(suffix)가 없는 단어의 기본형

*  의미있는 알맹이

  ex. writing, written에서 `writ`

##### *스테머 = 접미사를 제거하고 단어의 어간을 반환

