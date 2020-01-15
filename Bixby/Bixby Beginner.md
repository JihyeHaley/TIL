# Bixby

### 모델링

* action(*.model.bxb)
  * 캡슐이 사용자가 원하는 작업을 이해하도록 수행할 동작 정의
  * 가장 잘 판단할 것 같은 빅스비 캡슐에게 발화 전달 (이 때 발화함수가 action이다. 함수이므로 input, output 존재)
* concepts(*.model.bxb)
  * 발화 인식 및 발화 ***결과를 리턴할 때*** 필요한 값
  * ex) '햄버거 두개 주문해줘'
    * 햄버거 : FoodName
    * 2 : NumberOfFood

### 비지니스 로직

* Javascript code(*.js)
  * 모델링 단계에서 정의한 actions, concepts를 바탕으로 실제 서비스 코드 구현
  * 이 단계에서 서비스 API 연동 가능 
  * 개발자는 메뉴와 주문 정보를 저장하는 서버 구축하여 API를 통해 캡슐과 연동

### UX/UI

* layout(*.layout.bxb)
  * Layout-macro-def 함수를 작성하여,view에서 필요한 부분에 원하는 layout-macro 호출 가능
* view(*.view.bxb)
  * 최종 결과를 사용자에게 보여주는 UX/UI레이아웃 작업 진행

### 모델링 작성시 권장사항

유사한 Goal은 통합해서 최소화할 것!

* 기존)
  1. TurnUpVolume 소리 높여줘
  2. TurnDownVolume 소리 낮춰줘
  3. IncreaseBrightness  밝기 높여줘
  4. DecreaseBrightness 밝기 낮춰줘
  
* 개선)

  1. IncreaseSettingsValue 높여줘

  2. DecreaseSettingsValue 낮춰줘

  3. .

  4. vocab (SttingsValue){

     ​		SoundVolume

     ​		SoundBrightness

  5. }

### vocab 작성시 권장사항

1. 다른 vocab 들과 중복 지양



2. 한 entry에 다른 표현 방법이 있따면, 이들 역시 포함할 것
   1. vocab(PlaceName){
   2. ​           인천공항,
   3. ​           인천 공항,
   4. ​           인천국제공항,
   5. ​           인천 국제 공항,
   6. ​           인천 국제공항,
   7. }

   

3. enum vocab에 'key'값이 단어 set에서도 필요하다면, 단어set에도 한번 더 명시할 것
   1. Vocab (cuisineStyle){
   2. ​             "한식"{
   3. ​                     "한식",
   4. ​                     "한식당",
   5. ​              }
   6. }



4. 태깅 시 조사는 제외

* 명사 tagging 시, 조사 제외하고 tagging 진행 ("행", "발", 등 제외)



5. 명사동사 vocab 

* 기본적으로 명사를 tagging하는 것이 권장되나, 명사 외 tagging 이 필요하다면, flag나 role로 문장 전체에  tagging가능
*  필요하다면 동사 tagging 가능하나, 주의할 점은 vocab 생성 시 다양한 표현을 입력



### Bixby Studio

##### New Capsule 생성

* capsule.bxb 파일 생성: 해당 capsule의 id('.'  기준으로 앞이 팀명, 뒤가 샙술명) 및 기탙 정보 입력
  * playground.***(상용화 불가능 캡슐)
    * 상용화 하기 위해서는 캡슐 id 등록 필욧
    * Bixby developers site접속
    * 좌측 'Teams & Capsules' 클릭
    * '+ Create Team '클릭 및 팀명 입력
    * '+ Register Capsule' 캡슐명 입력 
    * '000팀명.000캡슐명' 캡슐 생성 완료
  * targets: 어떤 device에서 사용할 것인지
    * resourece의 training옵션에 영향을 미침
* code(비지니스 로직) 폴더, models(모델링) 폴더, resources(UX/UI)폴더 생성



##### 모델링 폴더 세분화

* models 폴더 하위로 actions, concepts 폴더 생성

  * actions: input과 output으로 이루어진 함수 (특정 js 파일이 실행될 때 input으로 받아야 할 변수명, type, min, max 값의 정의 및 output으로 전달해야 할 객체 저의)

  * Concepts: primitives + structures로 이루어진 각 변수들의 형type 정의 (primitive, structures 폴더 생성)

    * Primitives: name, integer, enume, text, boolean과 같은 형 type 정의

      * Enum: 가능한 모든 value 나열 가능 (ex. 한국 프로야구 구단)

        -> vocab에 관련 단어들 정의 필수

      * Name: 가능한 모든 value나열 불가능하나, 이름으로 알 수 있는 형태(ex . 신촌맛집 이름)

        -> 가능하면 vocab만들어서 늘어나는 training 개수 조절 하는 것도 필요

      * Text: 가능한 모든 value 나열 불가능하며, 이름으로도 알 수 없음(ex. 핸드폰 알림 설정 내용)

    * Structures: 여러 변수들을 갖고 있는 객체에 대한 property 정의

    * Roll-of 와 extends의 차이

      * Roll-of : 그 모델의 특성을 그대로 사용
      * Extends: 그 모델의 특성에 무언가 추가하여 사용

* 캡슐 폴더 하위로 assets 폴더  > images  폴더 > 로고 이미지 파일 추가

* 모델링 파일은 맨 앞글자를 대문자로 사용(그 이후는 came|case 형태)

  * 비즈니스 로직 관련된 것은 맨 앞글자를 소문자로 사용

* 모델링 파일의 description -> 해당 모델링에 대한 설명



##### 비지니스 로직 파일 생성

* code > *.js 파일 생성

  * 어떤 input 데이터를 받아와서 어떤 output의 데이터를 전달할지 비즈니스 로직 작성

  

##### UX/UI 폴더 세분화

* resources 폴더 > base 폴더 > endpoints.bxb 파일 구성
  * actions <--> code 연결시켜주는 역할
  * 모델링해서 바로 외부서버와 연동해도 되는 경우, remote-endpoint에 바로 설정
* Resources 폴더 > ko-KR 폴더 > training 파일 생성 (훈련 및 학습 역할)
  * training은 Goal당 30개 이상 권장
  * training 발화는 모두 'Learned'상태여야 함 ('Not Learned'는 대부분 vocab 오류)
* resources 폴더 > ko-KR폴더 > dialog 폴더 생성 (상황별 화면에 조화도리 메시지 절달 목적)
* resources 폴더 > ko-KR폴더 > layout 폴더 생성 (사용자에게 제공할 UX/UI 레이아웃)
* resources 폴더 > ko-KR폴더 > view 폴더 생성 (사용자에게 제공할 UX/UI뷰)
* resources 폴더 > ko-KR폴더>vocab 폴더 생성(models>concepts>primitives에서 정의한 enum 변수에 대해 연관있는 모든 단어들을 정의)
* resources 폴더 > ko-KR폴더>capsule-info.bxb 파일 생성(캡슐에 대한 기본 정보 입력)
* resources 폴더 > ko-KR폴더 >000.hints.bxb 파일 생성(빅스비 캡슐의 원활한 학습을 위해 사용자로부터 예상되는 발화에 대한 문구 입력)
  * hints는 10개 이상 작성 권장



### Bixby 테스트

##### 빅스비 캡슐의 학습 및 훈련 실시

- resources > ko-KR > training 클릭
- ‘Adding New Training’ 부분에 ‘햄버거 1개랑 콜라1개 주문해’ 발화 입력
- ‘Goal’부분에 발화가 실행되길 원하는 actions 이름 입력
- ‘NL’에서 input으로 받아올 데이터와 일치하는 부분의 발화 드래그 > concepts에서 해당 데이터 이름 입력
  - ex) ‘햄버거 1개 주문해줘’
    –> 햄버거 : FoodName
    –> 1개 : NumberOfFood
- 우측 상단의 ‘Compile NL Model’ 버튼 클릭
- 등록한 발화들의 상태가 Not Learned -> Learned 로 변환
- 특정 발화의 ‘Open In Simulator’ 클릭하여 예상 시뮬레이션 진행



##### Training 시 권장사항

1. 표현이나 띄어쓰기는 최소한 ASR 기준으로 지원

   - 예를 들어, ‘삼성 뮤직’은 ASR에서 ‘Samsung Music’으로 변환되듯이 형태 달라질 수 있음

2. Goal 당 10개 미만의 학습은 지양

3. 다양한 형태의 parameter 학습

   - 단어수와 형태가 다양한 entry(숫자, 한글, 영어)들이 존재한다면 이들에 대한 학습 필수

   

##### 모바일 빅스비에서 실제 발화 테스트

- 모바일 빅스비 > 설정 > 빅스비 보이스 정보 > 버전 부분을 톡톡 터치 > 개발자 옵션 on
- 모바일 빅스비 > 설정 > 개발자 옵션 > 디바이스로 테스트하기 > 사용중 > Revision ID > bixby studio에서 submission history의 ID 입력



