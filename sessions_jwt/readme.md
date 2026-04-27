pip install flask pyjwt

flask --app app.py run --host localhost --port 8000

--------------------------
sessions with lookup

curl -v -c jar.txt "http://localhost:5000/classic/login?u=alex"
curl -v -b jar.txt "http://localhost:5000/classic/me"
curl -v -b jar.txt "http://localhost:5000/classic/logout"
curl -v -b jar.txt "http://localhost:5000/classic/me"

Cookie: sid=abc123
server does lookup → SESSION_STORE[abc123] → alex

--------------------

jwt

TOKEN=$(curl -s "http://localhost:5000/jwt/login?u=alex" | jq -r .token)

curl -v -H "Authorization: Bearer $TOKEN" \
  "http://localhost:5000/jwt/me"

Authorization: Bearer <jwt>
server verifies signature → reads token → alex
