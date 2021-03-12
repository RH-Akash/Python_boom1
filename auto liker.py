import pyautogui as rh
import time
class coordinate:
    emptyMessage = (173, 700)
def click():
        rh.click(coordinate.emptyMessage)
def typechat():
    rh.typewrite("Hello, How are you?")
    rh.typewrite('\n')
    time.sleep(0.5)
    rh.typewrite("This is Syed Rimon")
    rh.typewrite('\n')
def send():
    print('text send')
while True:
     coordinate()
     click()
     typechat()
     send()
     time.sleep(1)

