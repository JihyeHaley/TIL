# corpus_friends.py

데이터 샘플을 편하게 모으기 위해서 함수도 많고, print도 많이 있습니다.

corpus와 친해지기 위해 첫 시작 파일을 `corpus_friends.py` 로 naming 했습니다 😸 



### Haley's 개발 일기 2020/10/23 (Update)

* MeCab()으로 분석 시도

  * | VV+ETM   | MM       | XPN         | ETN           | ETM           | XSN          | XSV          | XSA            |         |
    | -------- | -------- | ----------- | ------------- | ------------- | ------------ | ------------ | -------------- | ------- |
    |          | 관형사   | 체언 접두사 | 명사 전성어미 | 관형 전성어미 | 명사  접미사 | 동사  접미사 | 형용사  접미사 |         |
    | **NNP**  | **NNG**  | **JKO**     | **JX**        | **SSO**       | **SL**       | **SY**       | **SC**         | **SSC** |
    | 고유명사 | 일반명사 | 조사        | 보조사        | (             | 영어         | 특수문자     | 구분자         | )       |

    **적용 패턴** ***(최신)***

    * ```python
      mor_pattern = '(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(JX)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSO)?(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?'# open 괄호의 유무는 있어도 되고 없어도 되고
      ```

      * 괄호가 있어야 하는 경우가 더 정확도가 높다.
      * 의약학_wecab_raw_ko_report.xslx
      * 공학_wecab_raw_ko_report.xslx

    

    

  * *<u>실패한 패턴</u>*

    * 대부분 잘 뽑히지만, **only if  괄 호 있을 때 ** 입니다.
    * 품사의 처리 중 눈에 띄던 것  (처리완료)

      * 다음으로  소비자의  행동을  고관여(high  involvement),  저관여(low  involvement)로구분하여  소비자의  행동특성에  관한  연구를  제시하고  있다.

        * 예상대로라면 `고관여`, `저관여` 는 `NNG` 명사로 잡힐 줄 알았다.
        * 혹은 `고` `저` (`MM`)- `관여`(`NNG`) 로 filtering 될 줄 알았지만... 안그랬습니다.

    

    * 이유: 명사형으로 끊어서 접근을 시도했지만 아닌 경우도 꽤 됐다. 40개 중 10개

      * | 부   | 종양 | 신   | 경학 | 적   | 증후군 |
        | ---- | ---- | ---- | ---- | ---- | ------ |
        | XPN  | NNG  | XPN  | NNG  | XSN  | NNG    |

        | 저   | 관여 | 고관 | 여   |
        | ---- | ---- | ---- | ---- |
        | MM   | NNG  | NNG  | XSN  |

        | 분절 | 하   | 기   | 관지 |
        | ---- | ---- | ---- | ---- |
        | NNG  | XSV  | ETN  | NNG  |

        | 비   | 교통 | 성   |
        | ---- | ---- | ---- |
        | XPN  | NNG  | XSN  |

        | 저린   | 감   |
        | ------ | ---- |
        | VV+ETM | NNG  |

        | 항상 | 균   | 도말검사 |
        | ---- | ---- | -------- |
        | NNG  | JX   | NNG      |

        | 아데노신 | 탈   | 아미노효소 |
        | -------- | ---- | ---------- |
        | NNG      | XPN  | NNG        |

        | 대   | 조군 |
        | ---- | ---- |
        | XPN  | NNG  |

    * ```python
      mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
      ```

    * ```python
      mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' 
      #괄호 포함 해야만함
      ```

    


### :woman_student: 알고리즘 로직



### 🔓 해결하고 싶은 큰 덩어리

* 쉼표 뒤에 있는 대문자 요약어 

  * | 유엔 연합 | United Nations | ,    | UN   |
    | --------- | -------------- | ---- | ---- |
    | NNG NNG   | SL SL          | SC   | SL   |

    형태소 패턴이 `한글 (영어,영어[오로지 대문자])`

    일 경우.......

    * 앞의 **한글**을 끌어와서 쉼표 뒤에 있는 **대문자로만 된 영어**와 한 세트로 만들어 주기

  