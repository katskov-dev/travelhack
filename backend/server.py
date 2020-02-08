from sanic import Sanic
from sanic.response import json
from views import *
from models import *
from sanic.websocket import WebSocketProtocol
import asyncio
import socketio
import json
import time
import os
sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins='*')
app = Sanic(__name__)
sio.attach(app)
from sanic_cors import CORS, cross_origin


@sio.on("sendMes")
async def my_event(sid, message_data):
    print('SID', sid)

    data = message_data
    print('Get message: ', message_data)
    message = Messages.create(
        chat=0,
        text=data["message"],
        visitor_token=data["uuid"],
        type="USER_MESSAGE",
        datetime=datetime.datetime.now()
    )
    message.save()
    msg = {
        'type': message.type,
        'content': message.text,
    }
    msgs = {
        "messages": [msg],
    }
    print(msgs)
    await sio.emit('getMes', msgs, room=sid)



@sio.on("getMes")
async def my_event(sid, uuid):
    print('SID', sid)

    print('getmes', uuid)
    messages = Messages.select()
    # messages = Messages.select().where(Messages.visitor_token == uuid).order_by(Messages.datetime.asc())
    msgs = []
    for message in messages:
        msgs.append({
            "type": message.type,
            "content": message.text,
        })
    msgs = {
        "messages": msgs,
    }
    print(msgs)
    await sio.emit('getMes', msgs, room=sid)

@sio.on("sendUiid")
async def my_event(sid, message):
    print('SID', sid)

    # messages = Messages.select().where(Messages.visitor_token == uuid).order_by(Messages.datetime.asc())
    messages = Messages.select()
    msgs = []
    for message in messages:
        msgs.append({
            "type": message.type,
            "content": message.text,
        })
    msgs = {
        "messages": msgs,
    }
    print(msgs)
    await sio.emit('getMes', msgs, room=sid)



@app.route("/api/test", methods=['GET', 'POST'])
async def a1(request):
    return test2(request)


@app.route("/api/sign_in", methods=['POST'])
async def a2(request):
    return sign_in(request)


@app.route("/api/sign_up", methods=['POST'])
async def a3(request):
    return sign_up(request)


@app.route("/api/sign_out", methods=['POST'])
async def a4(request):
    return sign_out(request)


@app.route("/api/get_tours", methods=['POST'])
async def a5(request):
    return await get_tours(request)


# @app.route("api/get_tours_by_api", methods=['POST'])
# def a6(request):
#     return await get_tours_by_api(request)


# @app.route("/")
# async def test(request):
#     test3()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Person, Session])
    app.run(host="0.0.0.0", port=8000, protocol=WebSocketProtocol)
