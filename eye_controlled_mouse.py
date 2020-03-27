import pyautogui 
import math
import cv2
scaling_factor = 0.7
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(~img, cv2.COLOR_BGR2GRAY)
    ret, thresh_gray = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        rect = cv2.boundingRect(contour)
        x, y, width, height = rect
        radius = 0.25 * (width + height)
#        print(radius)
        area_condition = (100 <= area <= 200)
        symmetry_condition = (abs(1 - float(width)/float(height)) <= 0.2)
        fill_condition = (abs(1 - (area / (math.pi * math.pow(radius, 2.0)))) <= 0.3)
        if area_condition and symmetry_condition and fill_condition:
#            cv2.circle(img, (int(x + radius), int(y + radius)), int(1.3*radius), (0,180,0), -1)
            cv2.circle(img, (int(x + radius), int(y + radius)), 2, (0,180,0), -1)
            #print(pyautogui.size())
            pyautogui.moveTo(int(x + radius), int(y + radius), duration = 1)
     
        
    cv2.imshow('Pupil Detector', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()