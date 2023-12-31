import cv2
import numpy as np

camera = cv2.VideoCapture(0)


camera.set(3 , 640)
camera.set(4 , 480)

mountain = cv2.imread('mount everest.jpg')
mountain = cv2.resize(mountain , (640 , 480))

while True:
    status , frame = camera.read()

    if status:
        frame = cv2.flip(frame , 1)
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])

        
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)
        mask = cv2.bitwise_not(mask)

        person = cv2.bitwise_and(frame, frame , mask = mask)

        final_image = np.where(person  ==  0 , mountain , person)

        cv2.imshow('frame' , final_image)
        code = cv2.waitKey(1)
        if code  ==  32:
            break

camera.release()
cv2.destroyAllWindows()