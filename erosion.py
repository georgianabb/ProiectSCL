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
                erosion = cv2.erode(image,kernel,iterations = 1)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                erosion = cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB) 
		
		image = Image.fromarray(image)
		erosion = Image.fromarray(erosion)
 
		
		image = ImageTk.PhotoImage(image)
		erosion = ImageTk.PhotoImage(erosion)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			
			panelB = Label(image=erosion)
			panelB.image = erosion
			panelB.pack(side="right", padx=10, pady=10)
 
		
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=erosion)
			panelA.image = image
			panelB.image = erosion

root = Tk()
panelA = None
panelB = None
 
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

