import Leap
import requests

controller=Leap.Controller()

IP='192.168.43.17:8080'

order={'L':0,'R':0}
while True:
    order['L']=order['R']=0
    frame=controller.frame()
    if len(frame.hands)==2:
        for hand in frame.hands:
            pwm = 0 if hand.grab_strength == 1 else Leap.Vector.backward.dot(hand.palm_normal)
            if hand.is_left:
                order['L'] = pwm*100//1
            else:
                order['R'] = pwm*100//1
        print 'L:',order['L'],'R:',order['R']
        #requests order
        requests.get('http://'+IP+'/pwm/'+str(order['L'])+'/'+str(order['R']))
    else:
        #requests stop
        requests.get('http://'+IP+'/pwm/0/0')
