# corpus_friends.py

데이터 샘플을 편하게 모으기 위해서 함수도 많고, print도 많이 있습니다.

corpus와 친해지기 위해 첫 시작 파일을 `corpus_friends.py` 로 naming 했습니다 😸 



### Haley's 개발 일기 2020/10/21

* MeCab()으로 분석 시도

  * | NNG  | SL   | YS       | SSO  | SSC  |
    | ---- | ---- | -------- | ---- | ---- |
    | 명사 | 영어 | 특수문자 | (    | )    |

  * ```python
    mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    ```

  * ```python
    mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' #괄호 포함 해야만함
    ```

    ​    둘 중 하나로 시도

* 대부분 잘 뽑히지만, ***only if  괄 호 있을 때 *** 입니다.

* 품사의 처리 중 눈에 띄던 것 

  * 다음으로  소비자의  행동을  고관여(high  involvement),  저관여(low  involvement)로구분하여  소비자의  행동특성에  관한  연구를  제시하고  있다.

    * 예상대로라면 `고관여`, `저관여` 는 `NNG` 명사로 잡힐 줄 알았다.

    * 혹은 `고` `저` (`MM`)- `관여`(`NNG`) 로 filtering 될 줄 알았지만... 안그랬습니다.

      | 저   | 관여 | 고관 | 여   |
      | ---- | ---- | ---- | ---- |
      | MM   | NNG  | NNG  | XSN  |

      