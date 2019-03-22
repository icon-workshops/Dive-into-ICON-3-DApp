# Transaction Fee

트랜잭션이 실행되며 소모되는 수수료는 `usedStep * stepPrice` 로 계산됩니다.

* 수수료 계산에 사용된 `stepPrice` 는 `step` 과 `ICX` 의 교환 비율이며, `usedStep` 은 해당 트랜잭션에서 실행된 각 행동에 따른 `stepCost` 의 합으로 계산됩니다.
* 실행된 트랜잭션이 완료되기 전 `usedStep` 이 `stepLimit` 을 초과하는 경우, 해당 트랜잭션을 `out of step` 에러를 반환하며 실패합니다. **트랜잭션은 실패하였지만 실행과정에서 소모된 `stepLimit` 만큼의 수수료는 지불됩니다.**
* 트랜잭션을 실행하기 전 사용자의 ICX 잔고가 `stepLimit * stepPrice` 보다 적은 경우, 트랜잭션은 실행되지 않고 바로 실패합니다.

사용자는 거버넌스 스코어를 통해 ***행동에 따른 `stepCost`*** 와 ***`stepLimit` 설정할 수 있는 최대값***, ***stepPrice*** 를 조회할 수 있습니다.

* SCORE address = cx0000000000000000000000000000000000000001 : 거버넌스 스코어

* getStepCost

```bash
$ cat stepcost.json 
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "icx_call",
    "params": {
        "to": "cx0000000000000000000000000000000000000001",
        "dataType": "call",
        "data": {
            "method": "getStepCosts"
        }
    }
}

$ curl -H "Content-Type: application/json" -d @stepcost.json https://bicon.net.solidwallet.io/api/v3 
{
    "jsonrpc": "2.0",
    "result": {
        "default": "0x186a0",
        "contractCall": "0x61a8",
        "contractCreate": "0x3b9aca00",
        "contractUpdate": "0x5f5e1000",
        "contractDestruct": "-0x11170",
        "contractSet": "0x7530",
        "get": "0x0",
        "set": "0x140",
        "replace": "0x50",
        "delete": "-0xf0",
        "input": "0xc8",
        "eventLog": "0x64",
        "apiCall": "0x0"
    },
    "id": 1
}
```

* getMaxStepLimit

```bash
$ cat maxsteplimit.json 
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "icx_call",
    "params": {
        "to": "cx0000000000000000000000000000000000000001",
        "dataType": "call",
        "data": {
            "method": "getMaxStepLimit",
            "params": {
                "contextType": "invoke"
            }
        }
    }
}

$ curl -H "Content-Type: application/json" -d @maxsteplimit.json https://bicon.net.solidwallet.io/api/v3 
{
    "jsonrpc": "2.0",
    "result": "0x9502f900",
    "id": 2
}
```

* getStepPrice

```bash
$ cat stepprice.json 
{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "icx_call",
    "params": {
        "to": "cx0000000000000000000000000000000000000001",
        "dataType": "call",
        "data": {
            "method": "getStepPrice"
            }
        }
    }
}

$ curl -H "Content-Type: application/json" -d @stepprice.json https://bicon.net.solidwallet.io/api/v3 
{
    "jsonrpc": "2.0",
    "result": "0x2540be400",
    "id": 3
}
```