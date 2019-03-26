import os

from iconsdk.builder.transaction_builder import DeployTransactionBuilder, CallTransactionBuilder
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.icon_service import IconService
from iconsdk.libs.in_memory_zip import gen_deploy_data_content

from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.signed_transaction import SignedTransaction

from iconservice import Address, json_loads


from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS
from tbears.libs.icon_jsonrpc import IconJsonrpc

DIR_PATH = os.path.abspath(os.path.dirname(__file__))


class TestWelcome(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT = os.path.abspath(os.path.join(DIR_PATH, '..'))

    def setUp(self):
        print("---------------------setup-------------------------")
        print(self.SCORE_PROJECT)
        super().setUp()

        # self.icon_service = None
        # if you want to send request to network, uncomment next line and set self.TEST_HTTP_ENDPOINT_URI_V3
        self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        print("---------------------[setups]wallet load-------------------------")
        self.test_wallet_two = self._wallet_array[0]


        # install SCORE
        print("---------------------[setups]SCORE Deploy-------------------------")
        # self._score_address = self._deploy_score(to = "cx0000000000000000000000000000000000000000")['scoreAddress']
        self._score_address = self._deploy_score()['scoreAddress']

    def _deploy_score(self, to: str = SCORE_INSTALL_ADDRESS) -> dict:
        # Generates an instance of transaction for deploying SCORE.
        transaction = DeployTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(to) \
            .step_limit(100_000_000_000) \
            .nid(3) \
            .content_type("application/zip") \
            .content(gen_deploy_data_content(self.SCORE_PROJECT)) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)

        # process the transaction in local
        tx_result = self.process_transaction(signed_transaction, self.icon_service)

        self.assertTrue('status' in tx_result)
        self.assertEqual(1, tx_result['status'])
        self.assertTrue('scoreAddress' in tx_result)

        return tx_result


    def test_call_welcome(self):
        print("----------------[test call]------------------------")
        # Generates a call instance using the CallBuilder
        call = CallBuilder().from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("welcome") \
            .build()

        # Sends the call request
        response = self.process_call(call, self.icon_service)
        self.assertEqual(response, f"{self._test1.get_address()} hello")
        print(response)

    def _use_scrooge_(self, _to: Address, _amount: int):
        transaction_use_scrooge = CallTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(self._score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("scrooge") \
            .params({
            "_to":_to,
            "_amount":_amount
        }) \
            .build()

        signed_transaction = SignedTransaction(transaction_use_scrooge, self._test1)
        tx_result = self.process_transaction(signed_transaction, self.icon_service)
        return tx_result


    def test_send_test(self):
        print("----------------[test sendTx]------------------------")
        print("----------------[sendTx] Balance ------------------------")


        _balance_test1 = self.icon_service.get_balance(self._test1.address)
        _balance_test2 = self.icon_service.get_balance(self.test_wallet_two.address)

        print(f"before send icx from test1, test1's balance : {_balance_test1}")
        print(f"before send icx from test2, test2's balance : {_balance_test2}")

        print("----------------[sendTx] Balance check before sendtx ------------------------")

        tx_result = self._use_scrooge_(_to=self.test_wallet_two.address, _amount=100_000)
        print(tx_result)

        self.assertTrue('status' in tx_result)
        self.assertEqual(1, tx_result['status'])



