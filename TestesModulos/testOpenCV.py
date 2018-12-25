
import cv2
import numpy as np
from matplotlib import pyplot as plt

class TestOpenCV:

    def OpenCVPrinc(self):
        print("[0] Cam Test")
        print("[1] Open CV Test")
        print("[2] Translation")
        print("[3] ImageThresholding")
        print("[4] Gradiente")
        print("[5] Detector de borda")

        teste = input()
        if teste is "0":
            TestOpenCV.CamTeste(object)
        if teste is "1":
            TestOpenCV.ColorDetection(object)
        if teste is '2':
            TestOpenCV.TranslationCam(object)
        if teste is '3':
            TestOpenCV.ImageThresholding(object)
        if teste is '4':
            TestOpenCV.ImageGradiente(object)
        if teste is '5':
            TestOpenCV.EdgeDetector(object)
        if teste is '6':
            TestOpenCV.EdgeDetectorVideo(object)

    def CamTeste(self):
        print("Executando gray cam")
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def ColorDetection(self):
        print("Executando Color filter azul")
        cap = cv2.VideoCapture(0)

        while (1):

            # Take each frame
            _, frame = cap.read()

            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

    def TranslationCam(self):
        print("Executando tranlação de imagem")
        img = cv2.imread('translation.jpg', 0)
        rows, cols = img.shape

        M = np.float32([[1, 0, 100], [0, 1, 50]])
        dst = cv2.warpAffine(img, M, (cols, rows))

        cv2.imshow('img', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def ImageThresholding(self):
        print("Executando Image Thresholding")
        img = cv2.imread('translation.jpg', 0)
        img = cv2.medianBlur(img, 5)

        ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)

        titles = ['Original Image', 'Global Thresholding (v = 127)',
                  'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img, th1, th2, th3]

        for i in range(4):
            plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()

    def EdgeDetector(self):
        print("deteção de borda")
        img = cv2.imread('translation.jpg', 0)
        edges = cv2.Canny(img, 100, 200)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()

    def ImageGradiente(self):
        img = cv2.imread('translation.jpg', 0)

        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
        plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

        plt.show()


