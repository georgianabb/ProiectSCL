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
		sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
 
		image = Image.fromarray(image)
		sobelx = Image.fromarray(sobelx.astype('uint8'))
 
		image = ImageTk.PhotoImage(image)
		sobelx = ImageTk.PhotoImage(sobelx)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			panelB = Label(image=sobelx)
			panelB.image = sobelx
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=sobelx)
			panelA.image = image
			panelB.image = sobelx
root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

