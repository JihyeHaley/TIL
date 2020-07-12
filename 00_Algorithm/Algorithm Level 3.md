# Algorithm Level 3

##### 역으로 출력하기

~~~~c++
#include <stdio.h>
int main() {
  int n;
  int arr[1010] = {0};
  scanf("%d", &n);
  
  for(int i = 1; i <= n; i++){
    scanf("%d", &arr[i]);
  }
  for(int i = n; i >= 1; i--){
    printf("%d ", arr[i]);
  }
  return 0;
}
~~~~

##### 최댓값

~~~c++
#include <stdio.h>

int main (){
  int arr[100]={0};
  int order =0;
  for(int i=1; i<=9 ; i++){
    scanf("%d\n", &arr[i]);
  }
  
  int max = -987987987987;
  for(int i=1; i<=9;i++){
    if(max<arr[i]){
      max=arr[i];
      order=i;
    }
  }
  printf("%d\n", max);
  printf("%d", order);
  
  return 0;
}
~~~



##### Binary

~~~c++
#include <stdio.h>

int main(){
  int n;
  int arr[20]={0};
  int inx=1;
  scanf("%d", &n);
  
  while(1){
    if(n==1)
     break;
     arr[inx++]=n%2;
     n=n/2;
  }
  printf("1");
  for(int i=inx-1;i>=1;i--){
    printf("%d", arr[i]);
  }
  printf("\n");
  return 0;
}
~~~



#### 소수판별 1

~~~c++
#include <stdio.h>

int main() {
  int n;
  int cnt = 0;
  scanf("%d", &n);
  
  for(int i = 1; i <= n; i++){
    if(n % i == 0){
      cnt++;
    }
  }
  if(cnt == 2){
    printf("YES\n");
  }
  else{
    printf("NO\n");
  }

  return 0;
}
~~~



#####  소수판별 2

~~~c++
#include <stdio.h>

int main() {

  int n, m;
  int cnt;
  scanf("%d %d", &n, &m);
  for(int i = n ; i <= m ; i++){
    cnt=0;
    for(int j = 1 ; j <= i ; j++){
      if(i % j == 0){
        cnt++;
      }
      if(cnt > 2){
        break;
      }
    }
    if(cnt == 2){
      printf("%d ", i);
    }
  }

  return 0;
}
~~~

