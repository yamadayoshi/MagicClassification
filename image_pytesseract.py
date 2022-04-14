from pytesseract import pytesseract
from PIL import Image
import cv2
import requests
import imutils
import numpy as np

def show_img(win_name, image):
    cv2.imshow(win_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_tesseract(image):
    tesseract_path = '/usr/bin/tesseract'
    conf = '--oem 3 --psm 6'
    pytesseract.tesseract_cmd = tesseract_path

    text = pytesseract.image_to_string(image, config=conf)

    return text[:-1].replace('(', '').strip()

def box_text(img_name, image, is_gray):
    if is_gray:
        image = get_grayscale(image)
        h, w = image.shape
    else:
        h, w, c = image.shape

    box = pytesseract.image_to_boxes(image)

    for x in box.splitlines():
        x = x.split(' ')
        image = cv2.rectangle(image, (int(x[1]), h - int(x[2])), (int(x[3]), h - int(x[4])), (0, 255, 0), 2)

    cv2.imshow(img_name, image)
    cv2.waitKey(0)

    print('Box ', box)

def record():
    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    width = 1920
    height = 1080
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # phone_url = 'http://192.168.15.8:8080/shot.jpg'
  
    while(True):
        ret, frame = vid.read()
        img_resp = requests.get(frame)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=1000, height=1800)
              
        cv2.imshow('img', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_AREA)
            
            box_text('img_2', img, False)            

            break
    
        # # After the loop release the cap object
        # vid.release()
        # # Destroy all the windows
        # cv2.destroyAllWindows()


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def get_threshold(image):
    return cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

def run(image_path):
    image = cv2.imread(image_path)

    image_proc = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_AREA)
    image_proc = image
    
    return process_tesseract(remove_noise(image_proc))