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
            control.move('w',0.4)
        elif word=='進':
            control.move('w',0.4)
        elif word=='左':
            control.move('a',0.4)
        elif word=='右':
            control.move('d',0.4)
        elif word=='後':
            control.move('s',0.4)
        elif word=='圈':
            control.move('a',1)
            sleep(0.1)
            control.move('d',1)

@route('/<x>')
def movement(x):
    control.move(x)

@route('/pwm/<ena>/<enb>')
def movement_by_pwm(ena,enb):
    ena, enb = float(ena), float(enb)
    if ena > 0:
        control.GPIO.output(control.in1,1)
        control.GPIO.output(control.in2,0)
    else :
        control.GPIO.output(control.in1,0)
        control.GPIO.output(control.in2,1)
    
    if enb > 0:
        control.GPIO.output(control.in3,1)
        control.GPIO.output(control.in4,0)
    else :
        control.GPIO.output(control.in3,0)
        control.GPIO.output(control.in4,1)
    
    control.ena.ChangeDutyCycle(abs(ena))
    control.enb.ChangeDutyCycle(abs(enb))

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()
