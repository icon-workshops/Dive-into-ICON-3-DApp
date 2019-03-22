from django.shortcuts import render
from . import UseSDK
import os
from django.http.response import HttpResponse

DIR_PATH = os.path.abspath(os.path.dirname('__file__'))


#POST, GET 따로 받을 수 있습니다.
def make_game_room(request):
    if request.method == "GET":
        return render(request, "MakeGameRoom.html")
    elif request.method == "POST":
        return HttpResponse("it works  !!")
    else:
        return HttpResponse("go to main Page")


def mint_token(request):
    return render(request, "MintToken.html")


def sample(request):
    return render(request, "Sample.html")


def balance(request):
    return render(request, "balance.html")


def room_list(request):
    _data=UseSDK.JsonRPCCalls()
    _data=_data.show_game_room_list()
    _out_data={}
    _room_number = 0
    for _ in _data:
        print(_)
        _temp={}
        _splited = _.split(".")
        _temp["Name"] = _splited[0]
        _temp["Address"] = _splited[0].split(" ")[0]
        _temp["Explain"] = _splited[1]
        _temp["Prize"] = _splited[2]
        _temp["Time"] = _splited[3]
        _out_data["RoomNo"+str(_room_number)] = _temp
        _room_number += 1
    return render(request, "game_room_list.html", {"WaitRoom" : _out_data})



