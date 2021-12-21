import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('sample.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
print(d)
text = pytesseract.image_to_string(img)
print(text)
