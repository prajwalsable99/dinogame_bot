import pyautogui
# import PIL   #pillow
from PIL import Image,ImageGrab,ImageOps
from numpy import asarray

import time
# x=1
# while x<10:
#     pyautogui.keyDown('p')
#     x=x+1ppppppppp




def press(button):
    pyautogui.keyDown(button)


def isdhadak(imgdata):
    for i in range(785,800):
                    for j in range(330,400):
                        if imgdata[i,j]<100:
                            return True
    return False    



if __name__=='__main__':

    time.sleep(3)
    press("up")
    # img.show()
    while True:
    #     print(pyautogui.position())
   
        img=ImageGrab.grab().convert('L')
      
            
        imgdata=img.load()

        if isdhadak(imgdata):
            press("up")
          
        
            # print(asarray(img))

            # for i in range(686,730):
            #     for j in range(350,400):
            #         imgdata[i,j]=0

            # img.show()