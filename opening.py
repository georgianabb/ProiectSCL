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
                opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                opening = cv2.cvtColor(opening, cv2.COLOR_BGR2RGB) 
		
		image = Image.fromarray(image)
		opening = Image.fromarray(opening)
 
		image = ImageTk.PhotoImage(image)
		opening = ImageTk.PhotoImage(opening)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			panelB = Label(image=opening)
			panelB.image = opening
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=opening)
			panelA.image = image
			panelB.image = opening

root = Tk()
panelA = None
panelB = None
 
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

