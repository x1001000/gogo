from bottle import route, run, template
import control

@route('/')
def index():
    return template('dictate')

@route('/gogo/<sentence>')
def gogo(sentence):
    print(sentence)
    for word in sentence:
        if word=='前':
            control.move('w',0.3)
        if word=='左':
            control.move('a',0.3)
        if word=='右':
            control.move('d',0.3)
        if word=='圈':
            control.move('d',1.5)

@route('/<x>')
def movement(x):
    control.move(x)

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()