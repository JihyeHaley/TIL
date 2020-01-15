[Query String (쿼리 문자열)]

웹 클라이언트에서 웹 서버에 정보를 요청할 때 추가로 전달하는 문자열

이 문자열을 정해진 규칙으로 구성되어 전달되어야 하는데 

이 규칙을 url encoding 또는 query string encoding 규칙이라고 한다.

1. 모든 데이터는 name = value  형식이어야 한다.
2. 여러개의 name = value쌍을 전달할 때는 반드시!!! ***&*** 기호로 구분한다.
3. 공백은 ***+***문자로 변환되어 전달한다.
4. 영문과 숫자 그리고 일부 특수문자를 제외하고 ***%*** 기호와 함께 ***16***진수 코드값으로 전달되어야 한다.



[https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=ABCabc+123%EA%B0%80%EB%82%98%EB%8B%A4&oquery=ABCabc+123%EA%B0%80%EB%82%98%EB%8B%A4&tqi=UmITUwprvOssseaZT3Vssssstto-308348](https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=ABCabc+123가나다&oquery=ABCabc+123가나다&tqi=UmITUwprvOssseaZT3Vssssstto-308348)

id=%EA%B0%80%EB%82%98%EB%8B%A4&passwd=dsdfsdfsdf





