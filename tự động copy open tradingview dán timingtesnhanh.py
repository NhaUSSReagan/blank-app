import pyautogui as pg
import time


#pg.leftClick(1919,1049)

time.sleep(2)
#copy 
pg.leftClick(396,305)
pg.hotkey('ctrl', 'c')
pg.leftClick(1346,908)
#mở trading view

pg.leftClick(634,1047)
time.sleep(2)
pg.hotkey('alt', 'g')
pg.leftClick(1036,396)
time.sleep(1)
pg.hotkey('ctrl', 'v')
pg.leftClick(1081,895)








