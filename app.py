import os
from bottle import run, route

@route('/')
def index():
  return "<a href='/about'>About</a>"

@route('/about')
def about():
  return "<h2>About</h2>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


