# BLACK JACK 
ICON SCORE인 Black Jack 에 GUI를 추가하여 사용자가 접근하기 쉽게 한다.  
ICON SCORE의 Sample로 활용한다.

## 개발환경
-   Python3.6
-   django 2.1.7
-   iconSDK(Python)
-   iconSDK(Java Script)
-   OS X (mojave)
  
## Page

```
a. Room List
b. Sample
c. Make Game Room
d. Check Token Balance
e. Mint Token
```


#### a. Room List

```/roomlist```   

  1. 현재 존재하는 게임룸 오래된 순서대로 출력
  2. Testnet에 배포되어있는 Sample Game SCORE
  
      ``` SCORE address : cx89245b4a663f2062a9fe52a219c44c281e1d6c36 ``` 
  
  3. 2의 SCORE에서 show_game_room_list 의 icx_call 결과 
  4. Click 으로 세부내용 확인
  5. 세부내용 페이지에서 진행 가능한 게임일 경우, Join 기능
  6. Python SDK 를 활용하여 Django 에서 list 를 전달

#### b. Sample  

```/Sample```  

  1. ICONex Wallet에서 제공한 Sample 을 구현

#### c. Make Game Room

``` /room ```

1. Game Room 을 만든다.
2. 입력한 개수의 토큰만큼을 게임 참가비로 하는 게임을 만듭니다.
3. **LOAD WALLET** 버튼을 통해 지갑을 로드한 후, **MAKE IT** 버튼을 통해 방을 만드는 트랜잭션을 만들 수 있습니다.
4. 좌측 TextBox는 바라보고있는 노드에게 보내질 JSON Request 를 보여줍니다.
5. 우측 TextBox는 바라보고있는 노드에게 보낸 request에 대한 Response를 보여줍니다.


#### d. Check Token Balance

``` /balance ```

1. ICONex 를 통해, BlackJack Game에 있는 BalanceOf(msg.sender) 메서드를 호출하여, 현재 사용자의 Balance를 조회한다. 
2. **LOAD WALLET** 버튼을 통해 지갑을 로드합니다.
3. 지갑을 로드한 후, 즉시 선택한 지갑주소의 토큰 잔액이 화면에 보입니다. (Loop 단위입니다.)


#### e. Mint Token

``` /token ```

1. 사용자가 원하는 만큼의 Token을 mint 한다.
2. BlackJack Game에 있는 mintToken() 메서드를 통해 Token을 Mint 합니다.
3. Sign에는 ICONex를 활용한다.




## Start Sample 

1. Clone this repo 

2. start django server 
   
    ```$ cd samplepage/ ```
    ```$ python manage runserver 0.0.0.0:8000```

