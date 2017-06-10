import Leap
import requests
from time import sleep

controller=Leap.Controller()

IP='192.168.43.76:8080'
pi=3.14159
a1=15
a2=20

while True:
    #sleep(0.05)
    frame=controller.frame()
    hands=frame.hands
    if len(hands)==1:
        d=hands[0].direction
        #print hands[0].pinch_strength,hands[0].grab_strength,
        if hands[0].grab_strength > 0.5:
            if d.yaw*180/pi < -a1:
                requests.get('http://'+IP+'/a')
                print 'Turn Left'
            elif d.yaw*180/pi > a1:
                requests.get('http://'+IP+'/d')
                print 'Turn Right'
            else:
                print 'Stop'
        elif hands[0].pinch_strength < 0.5:
            if d.yaw*180/pi < -a2:
                requests.get('http://'+IP+'/q')
                print 'Go Left'
            elif d.yaw*180/pi > a2:
                requests.get('http://'+IP+'/e')
                print 'Go Right'
            else:
                requests.get('http://'+IP+'/w')
                print 'Go'
        else:
            if d.yaw*180/pi < 0:
                requests.get('http://'+IP+'/j')
                print 'Spin Left'
            elif d.yaw*180/pi > 0:
                requests.get('http://'+IP+'/k')
                print 'Spin Right'
 
    else:
        #print 'not one hand'
        pass
