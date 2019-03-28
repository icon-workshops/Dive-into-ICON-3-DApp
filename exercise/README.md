# SCORE 를 완성해 보세요

easy, hard  모드를 선택하여, 각각의 메서드를 구현해 주세요

###  공통사항
  ``` ./tests``` 폴더에 있는 test code를 수행하여 OK가 출력되어야 합니다. 
  
  T-Bears test 수행방법

  ``` tbears test tests ``` 


  ### 1. easy mode
- method name 'welcome'
- 외부에서 호출 가능
- 읽기만 가능
- 입력값 없음
- str 출력
  - 출력값 :   
  ``` Hello, [your wallet address] !!! Welcome to ICON Workshop 2019!!!```
  


### 2. hard mode 
- method name 'scrooge'
- 외부에서 호출 가능
- 쓰기 가능
- ICX 전송가능
- 보낼주소, 스쿠루지가 갖을 수수료 비율 입력받음


``` 
2 == _ratio 일 경우,

스크루지 개발자가 갖는 ICX의 양 == 전체 보낸양 / 2
 ```

#### hard 를 선택했을 때 유의할 점
  - 보낸사람의 잔고와 보낼양을 비교한 후 보내는 사람이 지닌 ICX의 양이 적을 경우, revert(트랜잭션 취소)를 해야합니다.

    ```
    if (보내는사람의 잔고 < 보낼 ICX양) :
        revert ("트랜잭션 취소")
    ```

  - scrooge는, ``` 전체 ICX양 / _ratio ``` 대로 SCORE의 배포자에게 보낸다.
  - scrooge가 갖고 남은 양의 ICX는 보낼사람에게 보내진다.

    ```
    스크루지(SCORE의 소유주)가 갖을 수수료 = 보내는 사람이 보낸 ICX / _ratio
    실제 받을사람이 받을 ICX = 보내는사람이 보낸 ICX -  스크루지(SCORE의 소유주)가 갖을 수수료
    ```

  - 두 트랜잭션은 이벤트로그가 남는다.  
  [icondev.io / audit checklist 중, 'ICXTransfer Eventlog' 참조](https://www.icondev.io/docs/audit-checklist#section-eventlog-without-token-transfer)
  
    ```
    @이벤트로그(인덱스될 입력값개수)
    이벤트로그 저장함수

    (어노테이션 생략)
    토큰 혹은 ICX를 전송하는 함수
    ```

----------------------------------------------------------------------------------


## 실습방법

1. hard / easy 중 하나를 골라, 디렉토리에 들어간다.  
    ``` cd easy/welcome ``` or ``` cd hard/welcome ```

2. tbears 의 test 기능을 통해 확인한다.  
    ``` tbears test tests ```

3. 같이 첨부되어있는 ``` test_welcome.py ```를 참조하여 welcome.py SCORE를 수정한다.  

4. 수정한 SCORE가 올바르게 작동하는지는 아래의 명령어를 통해서확인한다.  
    ``` tbears test tests ```



## 파일구조

```
├── README.md
└── sampleSCORE
    ├── easy
    │   └── welcome
    │       ├── __init__.py
    │       ├── package.json
    │       ├── tests
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   └── test_welcome.cpython-36.pyc
    │       │   └── test_welcome.py
    │       └── welcome.py
    └── hard
        └── welcome
            ├── __init__.py
            ├── package.json
            ├── tests
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   └── test_welcome.cpython-36.pyc
            │   └── test_welcome.py
            └── welcome.py
```
