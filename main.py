import pyautogui
from PIL import ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    #this is the lower rectangle to detect the cactus.
    for i in range(685, 800):
        for j in range(370, 400):
            if data[i, j] < 100:
                hit('up')
                return
    return
    #this is the upper rectangle to detect the birds.
    for i in range(680, 710):
        for j in range(290, 360):
            if data[i, j] < 100:
                hit('down')
                return
    return

if __name__ == '__main__':
    print("Dino game is going to start..")
    time.sleep(1)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
     
