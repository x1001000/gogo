from bottle import route, run, template

@route('/')
def index():
    return template('dictate')

@route('/gogo/<cmd>')
def gogo(cmd):
    print(cmd)

run(host='0.0.0.0', port=8080)