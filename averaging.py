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
		blur = cv2.blur(image,(5,5))
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB) 
 
		image = Image.fromarray(image)
		blur = Image.fromarray(blur)
 
		image = ImageTk.PhotoImage(image)
		blur = ImageTk.PhotoImage(blur)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			
			panelB = Label(image=blur)
			panelB.image = blur
			panelB.pack(side="right", padx=10, pady=10)
 
		
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=blur)
			panelA.image = image
			panelB.image = blur

root = Tk()
panelA = None
panelB = None
 
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

