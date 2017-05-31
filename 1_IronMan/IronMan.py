import Leap
import requests
from time import sleep

controller=Leap.Controller()

IP='172.19.16.186'
pi=3.14159
a=20

while True:
    #sleep(0.05)
    frame=controller.frame()
    hands=frame.hands
    if len(hands)==1:
        d=hands[0].direction
        #print hands[0].pinch_strength,
        if hands[0].pinch_strength > 0.65:
            if d.yaw*180/pi < -a:
                requests.get('http://'+IP+'/a')
                print 'Turn Left'
            elif d.yaw*180/pi > a:
                requests.get('http://'+IP+'/d')
                print 'Turn Right'
            else:
                print 'Stop'
        else:
            if d.yaw*180/pi < -a:
                requests.get('http://'+IP+'/q')
                print 'Go Left'
            elif d.yaw*180/pi > a:
                requests.get('http://'+IP+'/e')
                print 'Go Right'
            else:
                requests.get('http://'+IP+'/w')
                print 'Go Straight'
    else:
        #print 'not one hand'
        pass
