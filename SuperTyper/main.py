import pyautogui as pg
import pytesseract
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print('Staring in 5 second!')
sleep(5) 
while True:
    screen_image = pg.screenshot(region=(426,268, 1050, 60))
    text_process = pytesseract.image_to_string(screen_image)
    text = str(text_process).split(" ")

    if len(text) == 1:
        break  
    
    print(text)
    
    for word in text:
        
        print(word)
        
        pg.typewrite(word)
        pg.press('space')
        
        if word == text[-1]:
            break 
         
        
    
            
    
         
              