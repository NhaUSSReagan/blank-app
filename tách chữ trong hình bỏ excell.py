from pytesseract import pytesseract # pip install pytesseract 
from PIL import Image # pip install Pillow
import xlwings as xw
# Defining paths to tesseract.exe 
# # and the image we would be using 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
image_path = r"F:\software\python\tự copy time vào mt5 mt4\Take Screenshot\1.png"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable 
# # location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function 
# # This function will extract the text from the image 
text = pytesseract.image_to_string(img,lang="eng")
Split_text = text.split("\n")
print(text)
# create wb
wb = xw.Book()
# set active sheet
sht = wb.sheets.active
# set data to sheet
sht.range("A1").value = Split_text

# save wb
wb.save(r"F:\software\python\tự copy time vào mt5 mt4\Take Screenshot\1.xlsx")

