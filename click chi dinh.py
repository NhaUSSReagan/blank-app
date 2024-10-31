import pyautogui as pag
import time
#Find the prescription
# time.sleep(5)
# pos=pag.position()
# #Auto click
# for _ in range(3): 
# pag.click(pos)
# time.sleep(3)
#Search by object
time.sleep(3)
loc=pag.locateOnScreen(r'F:\software\python\thao tác chuột\click vào đối tượng chỉ định\1.png')
pag.leftClick(loc)
