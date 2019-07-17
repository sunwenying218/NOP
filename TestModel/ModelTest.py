import cv2
import time

def Video():
        facepath = "./Final_xml/HAAR_MyFace_cascade2.xml"
        glasspath = "./Final_xml/haarcascade_eye.xml"
        faceCascade = cv2.CascadeClassifier(facepath)
        glassCascade = cv2.CascadeClassifier(glasspath)
        camera1 = cv2.VideoCapture(0)
        while True:
            #time.sleep(0.1)
            ret1, frame1 = camera1.read() 
            img = frame1.copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            rect_f = faceCascade.detectMultiScale(gray, # 输入灰度图像
                                                scaleFactor = 1.15, # 每次图像尺寸减小比例
                                                minNeighbors = 7, # 每一个目标被检测到minneighbors次才算真的目标
                                                minSize = (150, 150), # 目标最小尺寸
                                                maxSize = (500, 500), # 目标最大尺寸
                                                flags = cv2.IMREAD_GRAYSCALE
                                                )

            
            for (x, y, w, h) in rect_f:
                cv2.putText(frame1, 'MyFace', (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)
                #break

            rect_e = glassCascade.detectMultiScale(gray, # 输入灰度图像
                                                scaleFactor = 1.15, # 每次图像尺寸减小比例
                                                minNeighbors = 5, # 每一个目标被检测到minneighbors次才算真的目标
                                                minSize = (50, 50), # 目标最小尺寸
                                                maxSize = (500, 500), # 目标最大尺寸
                                                flags = cv2.IMREAD_GRAYSCALE
                                                )
            for (x, y, w, h) in rect_e:
                cv2.putText(frame1, 'eye', (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 3)

                
            cv2.imshow('frame1',frame1)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        camera1.release()
        cv2.destroyAllWindows()
        return;

def Picture():
        PersonPath = "./xml/cascade.xml"
        #PersonPath = "E:\opencv\opencv\sources\data\lbpcascades\lbpcascade_frontalface.xml"
        PersonCascade = cv2.CascadeClassifier(PersonPath)

        #img = cv2.imread("D:\PythonFile\CurriculaDesign\Code\Picture\JPG\(8).jpg")

        img = cv2.imread("E:\desk_picture\jj2.jpg")
        #img = cv2.resize(img, (300, 400))
        imgc = img.copy()
        gray = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)
        rect = PersonCascade.detectMultiScale(  gray, # 输入灰度图像
                                                scaleFactor = 1.15, # 每次图像尺寸减小比例
                                                minNeighbors = 3, # 每一个目标被检测到minneighbors次才算真的目标
                                                minSize = (10, 10), # 目标最小尺寸
                                                maxSize = (500, 500), # 目标最大尺寸
                                                flags = cv2.IMREAD_GRAYSCALE
                                                )
        for (x, y, w, h) in rect:
                print(w,h)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

        cv2.imshow('img',img)
        return;

if __name__ == "__main__":
        Video()
        #Picture()
