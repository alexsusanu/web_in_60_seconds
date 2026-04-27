1. tested two identical fetch calls
fetch("https://httpbin.org/get")   // works
fetch("https://example.com")       // fails

Same code. Different result.

2. difference
httpbin → returned data → JS could read it
example.com → error → JS was blocked

3. why
The server response decides.

httpbin → sends Access-Control-Allow-Origin → allowed
example → no header → blocked

4. confirmed it in DevTools
Network → Headers
One has:
Access-Control-Allow-Origin: *
One doesn’t

5. key point
request still happens
response is blocked from JS
Final takeaway
CORS = browser rule
server opts in
controls who can READ responses (not who can call)

----------------------

Why use it:

Use CORS when:
you have a frontend (site A) calling an API (site B)

Example:

app.com → api.com

You must allow:

Access-Control-Allow-Origin: https://app.com

Otherwise your frontend breaks.

Don’t allow (or restrict) when:
you don’t want random websites using your API in the browser

If you do:

Access-Control-Allow-Origin: *

Then:

any site can use your API via JS
Critical truth
CORS does NOT stop people calling your API

This still works:

curl https://example.com
