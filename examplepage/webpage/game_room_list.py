import json
import os
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService

DIR_PATH = os.path.abspath(os.path.dirname('__file__'))


class JsonRPCCalls():

    # SCORE address and EOA address for call
    def __init__(self, keywallet_address = "hxbbf22a5733d5afd3743d4fd39dc9448f481c8f15" , sample_game_score_address = "cx89245b4a663f2062a9fe52a219c44c281e1d6c36"):
        self._sample_game_score_address = sample_game_score_address
        self._keywallet_address = keywallet_address

    def show_game_room_list(self):

        _icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))
        _ = CallBuilder().from_(self._keywallet_address) \
            .to(self._sample_game_score_address) \
            .method("showGameRoomList") \
            .build()

        response = _icon_service.call(_)

        return response

