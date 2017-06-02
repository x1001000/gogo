from bottle import route, run, template
import control

@route('/')
def index():
    return template('dictate')

@route('/gogo/<cmd>')
def gogo(cmd):
    print(cmd)

@route('/<x>')
def movement(x):
    control.move(x)

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()