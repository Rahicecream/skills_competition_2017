import requests
import cv2
import numpy as np
#from icecream import rahi
import time
def recognize():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Classifiers/face.xml"
    ecascade="Classifiers/haarcascade_eye.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    eyecascade=cv2.CascadeClassifier(ecascade);
    Id = 0

    cam = cv2.VideoCapture(1)
    src=1
    #cam = cv2.VideoCapture(src)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        timer=int(time.time())
        current_time=time.localtime()
        second=time.strftime("%S",current_time)
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.putText(img,"Mission status : active",(10,20),font,0.5,(0,0,255) ,1)
        cv2.putText(img,"localtime :  ",(10,40),font,0.5,(255,255,255) ,1)
        
        localtime=time.asctime(time.localtime(time.time()))
        cv2.putText(img,localtime,(100,40),font,0.5,(255,255,255) ,1)
        faces=faceCascade.detectMultiScale(gray,1.3,5)
     
      
            
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gray=img[y:y+h, x:x+w]
            roi_color=img[y:y+h,x:x+w]
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            occupation, conf = recognizer.predict(gray[y:y+h,x:x+w])
            cr_record, conf = recognizer.predict(gray[y:y+h,x:x+w])

            if(conf<50):
                 if(Id==1):
                    Id="Rahi"
                    occupation="Student"
                    cr_record="none"
                 elif(Id==2):
                    Id="Mazhar"
                    occupation="student"
                    cr_record="yes"
                   # rahi("criminal has detected")
                 elif(Id==3):
                    Id="Nurul Islam Nahid"
                    occupation="Education Minister"
                    cr_record="No"
                 elif(Id==4):
                    Id="Sheik Hasina"
                    occupation="Prime Minister"
                    cr_record="No"
                     

            else:
                    Id="unknown"

                    occupation="unknown"
                    cr_record="unknown"
                    
                    
            eyes=eyecascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                     cv2.rectangle(  roi_color,(ex,ey+20),(ex+ew,ey+eh), 255, 2)
                    

            #cv2.putText(img,str(Id), (x,y+h+20),font,2,(0,255,0), 2)

            cv2.putText(img,"Name : "+str(Id),(x,y+h+20),font,0.5,(0,255,0),2)

            cv2.putText(img,"Occupation : "+str(occupation),(x,y+h+45),font,0.5,(0,255,0),2)
            cv2.putText(img,"Criminal Records : "+str(cr_record),(x,y+h+70),font,0.5,(0,0,255),2)       #cv2.putText
        cv2.imshow('im',img)
     
     
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

 
