#### BOM - window, document, location, history, navigator, screen

* window
* document

* location

  * ```javascript
    location.href : // 페이지 이동을구현하고자 하는
    location.reload()  // 현재 페이지를 재요청
    ```

* history :   브라우저의 기록

* navigator

  * ~~~javascript
    navigator.userAgent // 이 페이지를 렌더링하고 있는 클라이언트 머신과 브라우저 정보를 하나의 문자열로 추출
    ~~~

* screen

#### DOM - Document Object Model)

- 브라우저의 HTML 파서가 서버로부터 전달받은 HTML 문서의 내용을 파싱하고 랜더링할때 인식된 HTML 태그, 속성 그리고 텍스틀 구성된 컨텐츠를 하나하나 JavaScript 객체로 생성한다.

- 이 때 만들어지는 DOM 객체들(Element 객체, Text 객체) 부모 자식 관계를 유지해서 트리 구조를 형성한다.

  - ==> JavaScript 코드로 HTML 태그나 속성 그리고 컨텐츠를 읽거나 변경할 수 있게 지원해서 동적인 웹페이지를 생성

  1. 필요한 태그를 찾는 방법

     ```javascript
     document.getElementsByTagName("태그명") // 복수의 값 , NodeList
     document.getElementByID("태그의ID 속성의 값") //Node
     document.getElementByClassName("태그의 class 속성값") // 복수의 값, NodeList
     ```

     ```javascript
     document.querySelector("CSS선택자") //Node
     document.querySelectorAll("CSS선택자") // 복수의 값, NodeList
     ```

  2. 태그의 내용이나 속성을 읽고 변경하는 방법, 삭제하는 방법

     ~~~javascript
     찾은Element객체.innerHTML
     찾은Element객체.textContent
     찾은Element객체.getAttribute("속성명")
     찾은Element객체.setAttribute("속성명", 속성값)
     찾은Element객체.removeAttribute("속성명")
     찾은Element객체.속성명
     찾은Element객체.속성명=속성값+
     ~~~

     

  3. 태그에서 발생하는 이벤트 또는 브라우저 객체서 발생하는 이벤트(WINDOW)에 대한 이벤 핸들러 구현 방법

     1. 인라인 이벤트 모델

        ```javascript
        <button onclick="코드">1</button>
        ```

     2. 전역적 이벤트 모델(고전 이벤트 모델)

        ```javascript
        <button>2</button>
        ```

        var dom = document.write.getElementsTagName("button")[0];

        

     3. 표준 이벤트 모델

        ```javascript
        <button>3</button>
        ```

        ```javascript
        var dom = document.getElementTagName("button")[0];
        dom.addEventListener("click", function(){코드});
        dom.removeEventListener("click", function(){코드});
        ```
   ```
      
  
  이벤트: 웹페이지상에서 마우스, 키보드 등을 통해 발생하는 액션
  
  ​				웹 브라우저에서 자동으로 발생하는 액션
  
  이벤트 핸들러(리스너):  이벤트가 발생했을 때 수행되는 기능을 구현한 함수
  
  이벤트 타켓: 이벤트가 발생한 대상 DOM 객체
  
  ​						((1). this,  (2)핸들러에 매개변수(e)를 하나 정의한 후: e.target
  
  ​						this.가 만들어지면 새로생긴 객체를 참조한다! 
   ```



data-xxx :  사용자가 필요에 의해 태그에 정의하는 속성

***** [디폴트 이벤트 핸들러]

HTML 태그에 디폴트로 등록되어 있는 이벤트 핸들러를 의미한다.
태그에 따라서는 눈에 띄는 디폴트 이벤트 핸들러를 가지고 있다.

<a> : click 이벤트에 대한  핸들러를 내장하고 있다.

<form> : submit 이벤트에 대한 핸들러를 내장하고 있다.
</form>

```javascript
<a herf="http://java.sun.com/">...</a>
<a herf="test.html">...</a>
<a herf="#memo">...</a> //#memo는 앵커명 !, 메모라는 이름이 붙어있는 태그 위치로 가라!  
<a herf="test.html#subject">...</a>

<a name = "memo"></a>
```



***** [이벤트 버블링]

특정 DOM 객체에서 이벤트가 발생하면 그 돔 객체에 등록된 이벤트 핸들러만  수행되는 것이 아니라 조상 DOM 객체에 등록된 핸들러도 수행된다.
(이벤트 전파)