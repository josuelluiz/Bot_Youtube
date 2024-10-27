import pyautogui as pa
import time
import pyperclip

pa.press('win')
pa.write("chrome")
time.sleep(1)
pa.press('ENTER')
time.sleep(1)
pa.hotkey('alt','space')
pa.hotkey('x')
time.sleep(1)
pa.write("youtube.com")
time.sleep(1)
pa.press('ENTER')
time.sleep(3)
pa.click(x=625, y=167)
time.sleep(1)
