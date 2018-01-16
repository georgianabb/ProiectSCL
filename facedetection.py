from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np
 
def select_image():
	global panelA
	path = tkFileDialog.askopenfilename()
	if len(path) > 0:
                face_cascade = cv2.CascadeClassifier('/home/georgiana/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
                eye_cascade = cv2.CascadeClassifier('/home/georgiana/opencv/data/haarcascades/haarcascade_eye.xml')
		image = cv2.imread(path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                     image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                     roi_gray = gray[y:y+h, x:x+w]
                     roi_color = image[y:y+h, x:x+w]
                     eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		
		image = Image.fromarray(image)
		
 
		
		image = ImageTk.PhotoImage(image)
		
		if panelA is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)

 
		
		else:
			
			panelA.configure(image=image)
			panelA.image = image

root = Tk()
panelA = None

 
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 

root.mainloop()

