import jwt
from flask import Flask, request

app = Flask(__name__)

JWT_SECRET = "demo-jwt-secret"

@app.get("/jwt/login")
def jwt_login():
    user = request.args.get("u", "alex")

    token = jwt.encode(
        {"user": user},
        JWT_SECRET,
        algorithm="HS256"
    )

    return {"token": token}

@app.get("/jwt/me")
def jwt_me():
    auth = request.headers.get("Authorization", "")

    if not auth.startswith("Bearer "):
        return "you are nobody"

    token = auth.removeprefix("Bearer ")

    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return f"you are {data['user']}"
    except jwt.InvalidTokenError:
        return "invalid token", 401
