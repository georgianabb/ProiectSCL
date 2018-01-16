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
		sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		image = Image.fromarray(image)
		sobely = Image.fromarray(sobely.astype('uint8'))
 
		image = ImageTk.PhotoImage(image)
		sobely = ImageTk.PhotoImage(sobely)
		
		if panelA is None or panelB is None:
			
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)

			panelB = Label(image=sobely)
			panelB.image = sobely
			panelB.pack(side="right", padx=10, pady=10)
 
		else:
			
			panelA.configure(image=image)
			panelB.configure(image=sobely)
			panelA.image = image
			panelB.image = sobely

root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
root.mainloop()

