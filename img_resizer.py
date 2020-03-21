import cv2
import time
from tkinter import *

class App:
    def __init__(self):
        def resize():
            file = e1_value.get()
            img = cv2.imread(file, 1)
            newImg = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
            def waitTime():
                times = [5,4,3,2,1]
                print("please wait for ")
                for i in times:
                    print("... " + str(i) + "s")
                time.sleep(1)
                cv2.imshow("Image", newImg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            waitTime()

        def preview():
            file = e1_value.get()
            img = cv2.imread(file, 1)
            cv2.imshow(file, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        window = Tk()
        window.config(background = "lightgreen")

        l0 = Label(window, text = "Image Resizer", fg = "white", bg = "lightgreen", font=('sans',30)).grid(row = 0, column = 1, columnspan = 4)
        l1 = Label(window, text="Image").grid(row = 1, column=0)
        e1_value = StringVar()
        e1 = Entry(window, textvariable = e1_value).grid(row=1, column=1)
        b1 = Button(window, text="resize", bg="green", border=10,command=resize).grid(row = 2, column=1)
        b2 = Button(window, text="preview",bg = "blue",border=10, command=preview).grid(row = 2, column=2)

        window.mainloop()

app = App()
app()
