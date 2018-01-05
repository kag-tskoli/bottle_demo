import os
from bottle import run, route

@route('/')

def index():
  return "Hello bottle"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

