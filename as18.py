import cv2
import imutils
cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
cam_north=cv2.VideoCapture(0)

while True:
    detected1 = 0
    _,img1=cam_north.read() #reading frame from camera
    img1=imutils.resize(img1,width=300) #resize to 300
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #color to Grayscale
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) #coordinates of vehicle in a frame
    for (x,y,w,h) in cars:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Frame", img1)
    b=str(len(cars))
    a= int(b)
    detected1=a
    n=detected1
    print("------------------------------------------------")
    print ("North: %d "%(n))
    if n>=2:
        print ("North More Traffic")
    else:
        print ("no traffic")
    if cv2.waitKey(33) == 27:
        break
    detected = 0
   
    if cv2.waitKey(33) == 27:
        break
cam.release()
cv2.destroyAllWindows()


