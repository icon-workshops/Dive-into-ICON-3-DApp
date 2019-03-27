from iconservice import *

TAG = 'Welcome'


class Welcome(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @eventlog(indexed=3)
    def ScroogeSend(self, _to: Address, _amount: int, _will_sent: int):
        pass

    @eventlog(indexed=3)
    def ScroogeGet(self, _owner: Address, _amount: int, _scrooge_get: int):
        pass

    @external(readonly=True)
    def welcome(self) -> str:
        return f"Hello, {self.msg.sender} !!! Welcome to ICON Workshop 2019!!!"

    @payable
    @external
    def scrooge(self, _to: Address, _ratio: int) -> str:

        # check sender's balance is bigger than send value
        if (self.icx.get_balance(self.msg.sender) < self.msg.value):
            self.revert(f"Hey, {self.msg.sender} !!! you have only {self.icx.get_balance(self.msg.sender)} !!!")

        # calculate scrooge's fee
        _scrooge_get = int(self.msg.value/_ratio)
        _will_sent = self.msg.value - _scrooge_get

        # send Tx
        self.icx.send(addr_to=_to, amount=_will_sent)
        self.icx.send(addr_to=self.owner, amount=_scrooge_get)

        # write to eventlog
        self.ScroogeSend(_to , self.msg.value, _will_sent)
        self.ScroogeGet(self.owner,self.msg.value, _scrooge_get)

        return "Done."

