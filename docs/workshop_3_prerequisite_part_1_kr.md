# Part 1. HelloWorld on local emulated environment

## **T-Bears 설치하기(도커)**

### **도커 이미지 다운로드 및 컨테이너 생성하기**

* Docker 설치하기 [[Get started with Docker]](https://www.docker.com/get-started)
* T-Bears 설치하기

```bash
$ docker run -it --name local-tbears -p 9000:9000 iconloop/tbears
* Starting RabbitMQ Messaging Server rabbitmq-server                    [ OK ]
Made tbears_cli_config.json, tbears_server_config.json, keystore_test1 successfully
Started tbears service successfully
root@c5b81f9874ee:/tbears# 
```

> 도커 설치 후 해당 명령어를 따라 입력하시면 T-Bears 도커 이미지를 받고, 컨테이너를 생성 및 실행할 수 있습니다.

### **컨테이너 환경에서 나오기**

```bash
root@07dfee84208e:/tbears# exit
```

> `exit` 또는 `Ctrl + P + Q` 를 입력하는 것으로 컨테이너 환경에서 빠져나올 수 있습니다.

### **컨테이너 목록보기**

```bash
$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS                    NAMES
c5b81f9874ee        iconloop/tbears     "entry.sh"          6 minutes ago       Up 6 minutes               0.0.0.0:9000->9000/tcp   local-tbears
```

> 해당 명령어를 따라 입력하시는 것으로 생성된 컨테이너의 목록 및 상태를 확인할 수 있습니다.

### **컨테이너 실행 및 환경 진입하기**

```bash
$ docker container start local-tbears
$ docker container attach local-tbears
root@07dfee84208e:/tbears#
```

> 해당 명령어를 따라 입력하시는 것으로 컨테이너를 실행하고, 환경으로 진입할 수 있습니다.

---

## **T-Bears 활용하기**

### **Test account**

사용자의 편의를 위해 로컬 테스트를 위한 키스토어 파일 `keystore_test1`을 제공합니다.
비밀번호가 공개되어 있으므로, 다른 네트워크에서 사용 시 불이익이 있을 수 있습니다.

* Address : hxe7af5fcfd8dfc67530a01a0e403882687528dfcb
* Passweord : test1_Account
* ICX balance : 0x2961fff8ca4a62327800000

---

### **ICX 잔고 확인하기**

`tbears balance` 를 통해 Account의 ICX 잔고를 확인할 수 있습니다.

```bash
root@07dfee84208e:/tbears# tbears balance hxe7af5fcfd8dfc67530a01a0e403882687528dfcb
balance in hex: 0x2961fff8ca4a62327800000
balance in decimal: 800460000000000000000000000
```

---

### **SCORE 프로젝트 생성하기**

`tbears init`을 통해 SCORE 새로운 프로젝트(hello_world)를 생성할 수 있습니다.

```bash
root@07dfee84208e:/tbears# tbears init hello_world HelloWorld
Initialized tbears successfully

root@07dfee84208e:/tbears# ls hello_world
hello_world.py  __init__.py  package.json
```

`hello_world.py` 는 기본적인 SCORE 구현 템플릿으로 구성되어 있습니다.

```python
from iconservice import *

class HelloWorld(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def hello(self) -> str:
        return "Hello"
```

---

### **SCORE 배포하기**

생성한 SCORE를 수정 없이 배포(deploy)하고 SCORE address를 확인해보겠습니다.

```bash
root@07dfee84208e:/tbears# tbears deploy hello_world
Send deploy request successfully.
If you want to check SCORE deployed successfully, execute txresult command
transaction hash: 0xc40cbbf2b89cd1e2890132145e6d86ad61835edaca0bcc3a4c34b5cb22b8be28

root@07dfee84208e:/tbears# tbears txresult 0xc40cbbf2b89cd1e2890132145e6d86ad61835edaca0bcc3a4c34b5cb22b8be28
Transaction result: {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0xc40cbbf2b89cd1e2890132145e6d86ad61835edaca0bcc3a4c34b5cb22b8be28",
        "blockHeight": "0x3158",
        "blockHash": "0x9e0c1385128bf0d425773f9f9130d683d327a058a9c8dc0a6c4df71bb98195e1",
        "txIndex": "0x0",
        "to": "cx3176b5d6cae66a1abbc3ca9070423a5c708834a9",
        "scoreAddress": "cx3176b5d6cae66a1abbc3ca9070423a5c708834a9", <-- SCORE address
        "stepUsed": "0x4d361d0",
        "stepPrice": "0x0",
        "cumulativeStepUsed": "0x4d361d0",
        "eventLogs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1"
    },
    "id": 1
}
```

> 모든 트랜잭션의 실행 결과는 `tbears txresult` 와 `txhash`값으로 확인할 수 있습니다. 해당 트랜잭션의 결과가 성공적인 경우 SCORE address를 확인할 수 있습니다.

---

### **SCORE 메소드 호출하기**

T-Bears CLI를 통해 배포한 SCORE의 `hello` 메소드를 호출하고, 결과를 확인해 보겠습니다.<br />
새롭게 생성할 `call.json` 파일은 request 메시지를 가지고 있어야합니다. `to`은 request를 받을 SCORE address를 의미하며 `from`은 request를 보내는 사용자의 address를 의미합니다.<br />
**예제의 scoreAddress가 아닌 실제 실행한 결과로 도출된 SCORE의 address를 입력해야합니다.**<br />
이와 다른 request에 대한 json 양식들은 [ICON JSON-RPC API v3 specification](https://www.icondev.io/docs/json-rpc-specification) 를 통해 확인할 수 있습니다.

```bash
root@07dfee84208e:/tbears# tbears call call.json
response : {
    "jsonrpc": "2.0",
    "result": "Hello",
    "id": 1
}
root@07dfee84208e:/tbears# cat call.json 
{
    "jsonrpc": "2.0",
    "method": "icx_call",
    "id": 1,
    "params": {
        "from": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "to": "cx3176b5d6cae66a1abbc3ca9070423a5c708834a9",
        "dataType": "call", 
        "data": {
            "method": "hello" 
        }
    }
}
```

---

### **hello_world SCORE 수정 및 업데이트하기**

`hello_world` SCORE의 `name`메소드를 새롭게 작성하고, `hello` 메소드를 수정하여, `hello` 메소드를 호출하는 request를 보낸 사용자의 address와 SCORE의 이름을 반환하도록 수정해 보겠습니다.


```python
    @external(readonly=True)
    def name(self) -> str:
        return "HelloWorld"

    @external(readonly=True)
    def hello(self) -> str:
        return f'Hello, {self.msg.sender}. My name is {self.name()}'
```

기존의 SCORE에 업데이트를 통해 수정한 내용을 적용해보겠습니다. 이전에 배포를 위한 명령어 `deploy`에 두가지 옵션을 더하는 것으로 SCORE를 업데이트할 수 있습니다.<br />
`-m update` 옵션과 `-o [socre_address]` 옵션을 통해 해당 request는 새로운 SCORE의 배포가 아닌 기존 SCORE에 대한 업데이트를 요청할 수 있습니다.

> **업데이트는 아이콘의 유니크한 특징으로, 업데이트 후 SCORE의 주소가 바뀌지 않습니다.**

```bash
root@07dfee84208e:/tbears# tbears deploy -m update -o cx3176b5d6cae66a1abbc3ca9070423a5c708834a9 hello_world
Send deploy request successfully.
If you want to check SCORE deployed successfully, execute txresult command
transaction hash: 0xc412dc9c6685701c8837eddea091283244303d322aa1fba36bc0782e1b483763
...
```

---

## **Part 1 마무리**

업데이트한 SCORE의 수정된 `hello` 메소드를 호출하고 결과를 확인하는 것으로 Part 1 을 마무리하도록 하겠습니다.

```bash
root@07dfee84208e:/tbears# tbears call call.json
response : {
    "jsonrpc": "2.0",
    "result": "Hello, hxe7af5fcfd8dfc67530a01a0e403882687528dfcb. My name is HelloWorld",
    "id": 1
}
```


