import pyautogui
from pynput.keyboard import Key, Controller
import pytesseract
import time

time.sleep(3)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
screenshot = pyautogui.screenshot(region=(470, 700, 1670, 290))
screenshot.save('screenshot.png')
text = pytesseract.image_to_string('screenshot.png')
text = str(text.replace('[', ''))
text = str(text.replace('|', 'I'))
text = str(text.replace('\n', ' '))
text = str(text.replace('  ', ' '))
if(text.startswith('|') or text.startswith('I')):
    text = str(text[1:])

with open('prompt.txt', 'w') as f:
    f.write(text)

print(text)
for char in text:
    Controller().press(char)
    Controller().release(char)
    time.sleep(0.01)
    
Controller().press(Key.page_up)

