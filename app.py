import os
from bottle import run, route

@route('/')

def index():
  return "Hello bottle <br> New Line"

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)

