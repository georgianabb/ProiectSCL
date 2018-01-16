from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
 
def select_image():
	
	global panelA, panelB
 
	path = tkFileDialog.askopenfilename()
	
	if len(path) > 0:
		
		image = cv2.imread(path)
		median = cv2.medianBlur(image,5)
 
		
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                median = cv2.cvtColor(median, cv2.COLOR_BGR2RGB) 
 
		image = Image.fromarray(image)
		median = Image.fromarray(median)
 
		image = ImageTk.PhotoImage(image)
		median = ImageTk.PhotoImage(median)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			panelB = Label(image=median)
			panelB.image = median
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=median)
			panelA.image = image
			panelB.image = median

root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

