from PIL import Image       #для распознования текста
import pytesseract          #для распознования текста\

from PIL import ImageGrab   #создание скриншотов
import pyautogui            #управление мышью и кликами

pyautogui.moveTo(440, 617)

my_image = ImageGrab.grab(bbox=(15, 15, 850, 1000))
my_image.save("test.jpg")


imagefile = Image.open('test.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
x = (pytesseract.image_to_string(imagefile, lang='eng')).split('\n')
print(x)
# print(pytesseract.image_to_string(imagefile, lang='eng', config='--psm 3 --oem 3'))
qwe