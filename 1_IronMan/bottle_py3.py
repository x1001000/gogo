from bottle import route, run#, template
import control

@route('/<x>')
def movement(x):
    control.move(x)

try:
	run(host='0.0.0.0', port=80)

finally:
  control.ena.stop()
  control.enb.stop()
  control.GPIO.cleanup()
