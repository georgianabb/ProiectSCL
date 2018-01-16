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
		laplacian = cv2.Laplacian(image,cv2.CV_64F)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
             
		image = Image.fromarray(image)
		laplacian = Image.fromarray(laplacian.astype('uint8'))
 
		image = ImageTk.PhotoImage(image)
		laplacian = ImageTk.PhotoImage(laplacian)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			panelB = Label(image=laplacian)
			panelB.image = laplacian
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=laplacian)
			panelA.image = image
			panelB.image = laplacian

root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

