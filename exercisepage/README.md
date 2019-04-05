# Welcome
ICON SCORE인 welcome 에 ICONex, JS SDK를 통하여 GUI를 구현하였습니다.  
Exercise 페이지의 빈 부분을 채워 넣는 실습을 할 수 있습니다. 


## 개발환경
-   Python3.6
-   Django 2.1.7
-   iconSDK(Python)
-   iconSDK(JavaScript)
-   OS X (Mojave)
  
## Page

```
a. Welcome
b. Exercise-welcome
c. Scrooge
d. Exercise-scrooge
e. iconex_connect_sample
```


#### a. Welcome

```/welcome```   

  1. ICONex로 지갑을 로드할 경우, SCORE에 정의된 메세지를 호출합니다.
  2. Read-only 인 ```Welcome``` 의 결과를 받아오고, 받아온 결과를 호출하도록 JS SDK, ICONex 로 구현되어있습니다.


#### b. Exercise-Welcome  

```/exercise-welcome```  

  1. ICONex로 지갑을 로드할 경우, SCORE에 정의된 메세지를 호출합니다.
  2. exercise-welcome 페이지는 ```/welcome``` 페이지와 같은 페이지 입니다. JS를 수정하여 완성해 주세요


#### c. Scrooge

``` /scrooge ```

  1. SCORE에 ```CallTransaction``` 을 통해 value와 파라미터를 전달합니다.
  2. 생성된 트랜잭션을 화면의 왼쪽에 있는 textarea, "score-data" 에서 확인할 수 있습니다.
  3. 트랜잭션의 결과는 화면의 우측에 있는 textarea, "score-response" 에서 확인할 수 있습니다.


#### d. Scrooge

``` /exercise-scrooge ```

  1.  exercise-scrooge 페이지는 ```/scrooge``` 페이지와 동일한 페이지 입니다.
  2.  scrooge 페이지에서 ```CallTransaction``` 부분이 지워져 있습니다. JS를 수정하여 완성해 주세요


#### e. iconex_connect_sample

``` /sample ```

  1.  iconex_connect_sample 페이지는 아이콘의 공식 지갑인 [ICONex, chrome extention](https://github.com/icon-project/iconex_chrome_extension) 의 [예제](https://github.com/icon-project/iconex_chrome_extension/blob/master/docs/iconex_connect/iconex_connect_sample.html) 페이지와 동일한 페이지 입니다.



## Start 

1. start Django server 
   
    ```
    $ cd ./exercisepage
    
    $ pip3 install -r requirements.txt
    
    $ python3 manage.py runserver 0.0.0.0:8000    
    ```

## Link

1. iconex_chrome_extension  
   https://github.com/icon-project/iconex_chrome_extension

2. icon-sdk-js  
   https://github.com/icon-project/icon-sdk-js

3. ICONex  
   https://github.com/icon-project/iconex_chrome_extension/tree/master/docs/iconex_connect
