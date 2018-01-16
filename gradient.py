from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np
 
def select_image():
	
	global panelA, panelB
 
	path = tkFileDialog.askopenfilename()
	
	if len(path) > 0:
		
		image = cv2.imread(path)
                kernel = np.ones((5,5),np.uint8)
                gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                gradient = cv2.cvtColor(gradient, cv2.COLOR_BGR2RGB) 

		image = Image.fromarray(image)
		gradient = Image.fromarray(gradient)
 
		image = ImageTk.PhotoImage(image)
		gradient = ImageTk.PhotoImage(gradient)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			panelB = Label(image=gradient)
			panelB.image = gradient
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=gradient)
			panelA.image = image
			panelB.image = gradient

root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

