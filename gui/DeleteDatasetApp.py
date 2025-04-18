import tkinter as tk
from PIL import Image, ImageTk
#from TestApp import TestApp  # You'll need to implement this class

class DeleteDatasetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Data")
        self.root.geometry("700x400+500+100")
        self.root.resizable(False, False)

        # Charger l'image
        image = Image.open("app_images/background_main.jpg") 
        image = image.resize((700, 400))  
        self.bg = ImageTk.PhotoImage(image) 

        bg_label = tk.Label(root, image=self.bg)  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title = tk.Label(root, text=" Data Management ", font=("Arial", 20, "bold"))
        title.pack(pady=40)
