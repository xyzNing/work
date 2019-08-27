import pytesseract
from PIL import Image


image=Image.open(r'C:\Users\ning\Desktop\1.gif')
text=pytesseract.image_to_string(image)
print(text)