`git init` : 처음 Git 시작할때

`git remote add origin [paste]` : 내 레퍼지토리 주소를 넣기

`git config --global user.name [username]`

`git config --global user.email [useremail]`

`git config --global user.name ` : name 잘 넣었는지 확인

`git config --global user.email ` : email 잘 넣었는지확인

`git status` :

1) 폴더에 어떤 변화가 있는지? 
2) 파일들이 무대에 잘 올라갔는지

`git add .` : 모든 파일 추가하기 (무대에 올릴 친구들 고르기)

`git commit  -m "sdfsdf"` (무대에 올릴때 이름 정해주기 )

orign - 주소

master - 브랜치 이름

`git push origin master` : origin  은 주소였고, master은 브랜치명



##### <브랜치 만들고 바꾸기>

`git branch [브랜치명]` : 브랜치 만들기

`git checkout [브랜치명]`: 브랜치 바꾸기, 브랜치가 바뀌면 로컬에서도 상태 바뀜



`git push/pull origin --allow-unrelated-histories ` : 안올라갈때... 빡칠때 쓰기..ㅎㅎ 어지간하면 안쓰는게 죻아요.