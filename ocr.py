import pytesseract
import cv2
from pytesseract import Output

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_text_boxes(image):
    d = pytesseract.image_to_data(image, lang= 'rus+eng', output_type=Output.DICT)
    n_boxes = len(d['level'])
    boxes = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        boxes = cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return boxes

def image_to_string(image, lang='rus+eng'):

    extracted_text = pytesseract.image_to_string(image, lang=lang)
    return extracted_text