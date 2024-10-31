import pyautogui as pg
import time
pg.doubleClick(1919,1047)
pg.doubleClick(141,521)

pos=pg.position(1919,1045)
time.sleep(5)
pg.doubleClick(69,76)
pg.typewrite(' bitcoin')
pg.press ('enter')
pg.doubleClick(65,39)
pg.doubleClick(121,71)
#rest of world
pg.doubleClick(1179,394)
pg.doubleClick(1203,692)
# tab tithi
pg.doubleClick(518,112)
pg.doubleClick(609,472)
pg.typewrite('d')
pg.doubleClick(556,583)
for _ in range(2):
    pg.press ('backspace')

pg.typewrite('0')
#2  find tithi pravesha
pg.doubleClick(572,411)
time.sleep(3)
pg.doubleClick(785,320)















