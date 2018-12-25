
import cv2
import numpy as np
from matplotlib import pyplot as plt

class OpenCV:
    def EdgeDetectorVideo(self):
        print("deteção de borda de video")
        print("gradiente: ")
        gradiente = input()

        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #lower_red = np.array([30, 150, 50])
            #upper_red = np.array([255, 255, 180])

            #mask = cv2.inRange(frame, lower_red, upper_red)
            #frame = cv2.bitwise_and(frame,frame, mask= mask)

            frame = cv2.Canny(frame, 100, 150)

            # Display the resulting frame
            cv2.imshow('OpenCV', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def GradienteFilter(self, frame, gradiente):

        if gradiente is '1':
            frame = cv2.Laplacian(frame, cv2.CV_64F)
            print(frame)

        if gradiente is '2':
            frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
            frame = np.Sobel.absolute(frame)
            frame = np.uint8(frame)

        return frame
