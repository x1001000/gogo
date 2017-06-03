from bottle import route, run, template
from time import sleep
import control

@route('/')
def index():
    return template('dictate')

@route('/gogo/<sentence>')
def gogo(sentence):
    print(sentence)
    for word in sentence:
        if word=='跑':
            control.move('w',1)
        elif word=='前':
            control.move('w',0.3)
        elif word=='進':
            control.move('w',0.3)
        elif word=='左':
            control.move('a',0.3)
        elif word=='右':
            control.move('d',0.3)
        elif word=='圈':
            control.move('a',1)
            sleep(1)
            control.move('d',1)

@route('/<x>')
def movement(x):
    control.move(x)

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()