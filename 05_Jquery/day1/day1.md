### day1 

##### : Jquery

jQuery

[jQueryHome](http://jquery.com)

[jQueryUi](https://jqueryui.com/)

[jQuery플러그인](https://plugins.jquery.com/)



* jQuery.ajax()     ==     
  * **$.ajax()**, **$.get()** ←default, **$.post()**   ←  **xml**
  * $.getJSON()   ←  json
  * $.(...).load()    ←  get방식만 지원하고 응답이 text 형식일때만 의미가 있다.



#### Package

* **effect**
  * exam1 - hide, show
  * exam2 - toggle
  * exam3 - fade in , fade out
  * exam4 - slide up, slide down
  * exam5 - animate (if/else)
  * exam6 - animate method 를 두번 호출하면서 효과를 변, back은 없음
  * exam7- toggle (opacity 0,1)
  * exam8 - toggle (width, height, toggle, swing like easing - 점빨, 점느) [swing or lean]
  * exam9 - toggle( width만) ←→
  * exam10 -  jquery plug in 사용



* **domedit**

  * exam4 - attr (argument1개, 속성1개만 있음), 이미지 size 바꿈 width만 변경

  * exam5 - attr 변수에 function이 와서 수행하도록 *****?index는 0부터*

  * exam6 - attr 변수에 function이 와서 수행하도록 width는 또 function을 활용해서 받아오고, height는 고정

  * exam7 - 있었던 속성 삭제 , removeAttr

  * exam8 - **Attr, Css는 Argument 사양이 똑같아**

    ### Attr('HTML속성명'), Css() 는 똑같은 사양

    > *** Attr('HTML속성명') ⇒ *getter* (첫번째 것만 처리한다.)**

    > *** Attr('HTML속성명', 'HTML속성값')

    - Attr('HTML속성명', '함수')

    - Attr({HTML속성명: 'HTML속성값', HTML속성명: 'HTML속성값',...} ) ⇒ setter**

      $(document).ready(function () { $('h1').each(function(index,data) { var color = $(data).css('color'); alert(color); });

  * exam9 -색상처리

  * exam10 - 글자의 background 컬러도 검정색으로

  * exam11

    - html() -  innerHTML(htlm 태그로서 rendering)

      argument 有O ('태그문자열'),  ('함수')—> setter

      argument 無X—> getter

    - text() —> textContent

  * exam12- alert가 하나로 묶어서 나온다.

  * exam13 - div 태그에 아무것도 없지만... // h1 태그 추가해서 html 로, // h1 태그 추가해서 text 로

  * exam14 - div 태그에 아무것도 없지만... // h1 태그 추가해서 html  header + index로

  

* **ajaxjqexam** - jQuery를 가지고 ajax를 구현

  * exam1 - ??

    ```
      $(document).ready( function() {
         $.ajax('content/sample.xml', {
            success :  function(data) {                    
              $(data).find('testxml').each(function() { 
                $('body').append("<h1>"+$(this).find('name').text() + '</h1>');
                $('body').append("<h1>"+$(this).find('age').text() + '</h1>');
                $('body').append("<h1>"+$(this).find('kind').text() + '</h1>');
              });
            }
          });
      });
    ```

    body 태그에 h1 태그를 찾아서 붙여라

  * exam2 -

    - $(....).each(함수)
    - $.each(배열객체 또는 자바스크립트 객체, 함수) ← 반복처리를 대신 해준다.

  * exam3 -

  * exam5 - load();

  * exam7

  * exam7_1

  * exam7_2 ← 파일 업로드 post 방식