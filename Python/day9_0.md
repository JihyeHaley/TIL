# day9_model more and more

`

model 2개를 연결,  refernece 있을 예정!!!!!



```PYTHON
article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



Relationship - > **reciprocal relationship**!!!!!!

for example but gon' be changeds

| ID   | TITLE  |
| ---- | ------ |
| 1    | hi     |
| 2    | hello  |
| 3    | ohayou |
| 4    |        |

| ID   | CONTENT | FK(참조키)                  |
| ---- | ------- | --------------------------- |
| 1    | HI      | if 100 <- 100번 게시물의 글 |
| 2    | HELLO   |                             |
| 3    | HELLO   |                             |

