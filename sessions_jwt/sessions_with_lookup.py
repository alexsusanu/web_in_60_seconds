from flask import Flask, request, make_response
import uuid

app = Flask(__name__)

SESSION_STORE = {}

@app.get("/classic/login")
def classic_login():
    user = request.args.get("u", "alex")
    sid = str(uuid.uuid4())

    SESSION_STORE[sid] = {"user": user}

    resp = make_response(f"classic login as {user}")
    resp.set_cookie("sid", sid, httponly=True)
    return resp

@app.get("/classic/me")
def classic_me():
    sid = request.cookies.get("sid")
    data = SESSION_STORE.get(sid)

    if not data:
        return "you are nobody"

    return f"you are {data['user']}"

@app.get("/classic/logout")
def classic_logout():
    sid = request.cookies.get("sid")
    SESSION_STORE.pop(sid, None)
    return "session deleted"
