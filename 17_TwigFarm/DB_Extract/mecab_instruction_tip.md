## 본격 mecab설치 (환경: MacOS, python 3.7.7)

```
Patience will make you happy......
```

<br/>

<br/>

###### 주요 참고 사이트

[MeCab 및 mecab-python 설치하기 공식사이트 위주의 설명](https://buttercoconut.xyz/251/)

###### *도저히 해결이 안될때는...* 

[이 사이트를 참고해보시면 어떨까요? (적절한 에러에 대응하는 팁들 참고 가능)](https://medium.com/@ProgrammingPearls/elasticsearch에서-한글-형태소-분석기-은전-한-닢-를-os-x-에서-적용해보자-5f879962339)

<br/>

### 1. mecab-ko

https://bitbucket.org/eunjeon/mecab-ko/downloads/

우선 위의 링크의 최신 버전의 mecab-ko 을 다운로드 하여 설치합니다. (혹은 mecab-0.996-ko-0.9.2.tar.gz)

```python
tar xzvf mecab-0.996-ko-0.9.2.tar.gz
cd mecab-0.996-ko-0.9.2
./configure
make
sudo make install
```

<br/>

### 2. mecab-ko-dic

https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/

우선 위의 링크의 최신 버전의 mecab-ko 을 다운로드 하여 설치합니다. (혹은 mecab-ko-dic-2.1.1-20180720.tar.gz)

```python
tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
cd mecab-ko-dic-2.1.1-20180720
./configure
make
sudo make install
```

***여기까지 하면 우선 mecab이 MacOS에 설치가 된 것입니다. Error가 없다면, Warning은 또 다른 문제....\***

<br/>

### 3. mecab-python

아래의 코드대로 git를 통해 소스코드를 내려받아 파이썬 환경에서 혹은 virtualenv같은 가상 환경에서 설치를 해주면 됩니다.

```python
git clone <https://bitbucket.org/eunjeon/mecab-python-0.996.git>
cd mecab-python-0.996
python setup.py build
python setup.py install
```

- 그런데 python [setup.py](http://setup.py) 을 통해 설치가 안될 때가 있습니다.
- c++라이브러리 관련해서 문제가 있을 때 입니다. 이 경우에는

```python
MACOSX_DEPLOYMENT_TARGET=10.9 python3 setup.py build
MACOSX_DEPLOYMENT_TARGET=10.9 python3 setup.py install
```

<br/>

### 4. pip insatll mecab-python

```python
pip insatll mecab-python
```

- Test 할 수 있는 Example

  - MeCab_test_1.py MeCab ***대소문자\*** 주의

    ```python
    import MeCab
    
    m = MeCab.Tagger()
    te = m.parse('안녕하세요 헤일리입니다.')
    print(te)
    ```

    ![image](https://user-images.githubusercontent.com/58539681/97953286-5a9dba00-1de3-11eb-929c-b7a3930f883c.png)

  - MeCab_test_2.py'

    ```python
    import MeCab
    
    m = MeCab.Tagger()
    te = m.parse('안녕하세요 haley입니다.')
    print(te)
    ```

    ![image](https://user-images.githubusercontent.com/58539681/97953326-7903b580-1de3-11eb-9953-42ad537ed055.png)

<br/>

<br/>

<br/>

<br/>

## 여기까지 잘 실행이된다면..... 성공하신겁니다.....

MeCab설치 하루종일 걸릴 수 도 있는 작업이니 오래걸렸다고 속상해 안하셔도 됩니다..
 이제 마음껏 분석하실 수 있습니다. 축하축하축하:)**