import cv2
import numpy as np
import control

# Creating track bar
def nothing():
    pass
cv2.namedWindow('result')
cv2.createTrackbar('hl', 'result', 46,  359, nothing)
cv2.createTrackbar('hu', 'result', 67,  359, nothing)
cv2.createTrackbar('sl', 'result', 59,  100, nothing)
cv2.createTrackbar('su', 'result', 100, 100, nothing)
cv2.createTrackbar('vl', 'result', 0,   100, nothing)
cv2.createTrackbar('vu', 'result', 100, 100, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

while True:
    try:
        (_, frame) = cap.read()
        frame = cv2.flip(frame,-1)
        
        #print len(frame)

        # get info from track bar and appy to result
        hl = cv2.getTrackbarPos('hl', 'result')
        hu = cv2.getTrackbarPos('hu', 'result')
        sl = cv2.getTrackbarPos('sl', 'result')
        su = cv2.getTrackbarPos('su', 'result')
        vl = cv2.getTrackbarPos('vl', 'result')
        vu = cv2.getTrackbarPos('vu', 'result')

        '''
        # sports wear
        hl,hu=46,67 
        sl,su=59,100
        vl,vu=0,100
        # tiffany blue(green) umbrella
        hl,hu=177,182 
        sl,su=27,100
        vl,vu=0,100'''
        
        # h in range(180), s in range(256), v in range(256)
        hl = hl/2
        hu = hu/2
        sl = sl*255/100
        su = su*255/100
        vl = vl*255/100
        vu = vu*255/100

        # Converting to HSV, and flip the frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Normal masking algorithm
        lower = np.array([hl, sl, vl])
        upper = np.array([hu, su, vu])
        mask = cv2.inRange(hsv, lower, upper)

        (contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #print len(contours)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))  #has a chance to raise ZeroDivisionError
            cv2.circle(frame, center, 5, (255, 0, 0), -1)
            area = cv2.contourArea(c)
            print area,
            if area > 200:
                if center[0]<320*43/100:
                    control.move('a', 0.02)
                    print 'Left'
                elif center[0]>320*57/100:
                    control.move('d', 0.02)
                    print 'Right'
                else:
                    control.move('w', 0.05)
                    print 'Straight'
            else:
                print 'stop'

        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("result", result)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    except ZeroDivisionError:
        print 'ZeroDivisionError'
    except KeyboardInterrupt:
        print 'KeyboardInterrupt'
        break

cv2.destroyAllWindows()
control.ena.stop()
control.enb.stop()
control.GPIO.cleanup()