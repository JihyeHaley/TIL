### Function

~~~javascript
numbering = function (){
  i=0;
  while(i<10){
    document.write(i);
    i+=1;
  }
}

function numbering(){
  i=0;
  while(i<10){
    document.write(i);
    i+=1;
  }
}

(function(){
  i=0;
  while(i<10){
    document.write(i);
    i+=1;
  }
})(); //익명함수

~~~



### Object

~~~javascript
var grades = {'jihye':97, 'jisun':01, 'jiwoo':03}

var grades ={};
grades ['jihye']=97;
grades ['jisun']=01;
grades ['jiwoo']=03;

grades ['jihye']
>>> 97
grades.'jihye'
>>>>97
~~~

 

```javascript
var arr = ['a','b','c'];
var array = {'a':97, 'b':01, 'c':03};

// 배열
for ( var i=0;i<arr.length;i++){
  console.log(arr[i]);
}
//객체 
// key value 
for (key in object 이름){
  document.write("key: "+key+ "value"
                 +object 이름[key]+"<br/>");
}
for ( key in object 이름 ){
  console.log(key);
}
>>> key값 다 내보내!

for( key in object 이름){
  console.log([key]);
}
>>> value 값 다 내보내!
  
var grades = {};
grades['love']=10;
grades['hate']=11;
grades['jealous']= 12;

/*객체의 반복문*/
for(key in grades){
  document.write("key: "+key+", value:"+grades[key]);
}

for(key in grades){
  console.log(key);
}
```

