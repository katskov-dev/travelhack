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
from akinator import Akinator

sid_visitor_id = {

}


async def send_message(text, user_id, sid=0):
    message = Messages.create(
        chat=0,
        text=text,
        visitor_token=user_id,
        type="BOT_MESSAGE",
        datetime=datetime.datetime.now()
    )
    message.save()
    await sio.emit('getMes', {
        "messages": [
            {
                "type": 'BOT_MESSAGE',
                'content': text
            },
        ],
    }, room=sid)


@sio.on("sendMes")
async def my_event(sid, message_data):
    data = message_data
    sid_visitor_id[sid] = data["uuid"]
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
    await sio.emit('getMes', msgs, room=sid)
    id = data["uuid"]
    if Akinator.check_yes(data["message"]):
        state = Akinator().states[id]
        state = Akinator().query(id,state, "+")
        Akinator().states[id] = state

        text = Akinator().messages[state]
        await send_message(text, message_data["uuid"], sid)
    elif Akinator.check_no(data["message"]):
        state = Akinator().states[id]
        state = Akinator().query(id, state, "-")
        Akinator().states[id] = state

        text = Akinator().messages[state]
        await send_message(text, message_data["uuid"], sid)
    else:
        await send_message("Я вас не понимаю :( Нужно отвечать 'да' или 'нет'", message_data["uuid"], sid)



@sio.on("getMes")
async def my_event(sid, uuid):
    messages = Messages.select().where(Messages.visitor_token == uuid).order_by(Messages.datetime.asc())
    msgs = []
    for message in messages:
        msgs.append({
            "type": message.type,
            "content": message.text,
        })
    msgs = {
        "messages": msgs,
    }

    await sio.emit('getMes', msgs, room=sid)


@sio.on("sendUiid")
async def my_event(sid, uuid):
    messages = Messages.select().where(Messages.visitor_token == uuid).order_by(Messages.datetime.asc())
    msgs = []
    for message in messages:
        msgs.append({
            "type": message.type,
            "content": message.text,
        })
    msgs = {
        "messages": msgs,
    }
    await sio.emit('getMes', msgs, room=sid)

    state = Akinator().query(uuid)
    print(state)
    if state == 0:
        Akinator().states[uuid] = 1
        await send_message(
            "Если вы согласитесь ответить на несколько вопросов, то я готов подобрать для вас страну, согласны? :)",
            uuid, sid)
    else:
        text = Akinator().messages[state]
        await send_message(text, uuid, sid)


@app.route('/api/sendall', methods=["POST"])
async def send_message_to_all(request):
    data = request.json
    msgs = {
        "messages": [
            {
                "type": "BOT_MESSAGE",
                "content": data["messsage"]
            }
        ]
    }
    await sio.emit('getMes', msgs)


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


@app.route("/api/packages/<package>", methods=['GET'])
async def a6(request, package):
    return await get_package(request, package)


@app.route("/api/tours/<tour_id>", methods=['GET'])
async def a7(request, tour_id):
    return await get_tour_by_id(request, tour_id)


@app.route("/api/packages/<package>/tours/<tour>", methods=['GET'])
async def a8(request, package, tour):
    return await get_package_tour(request, package, tour)

@app.route("/api/get_recomended_tours", methods=['GET'])
async def a9(request):
    return await get_recomended_tours(request)



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
