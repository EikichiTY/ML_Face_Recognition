import cv2
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class NewDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Capture App")
        self.root.geometry("700x600+500+100")
        self.root.resizable(False, False)

        # Charger l'image
        image = Image.open("app_images/background.png") 
        image = image.resize((700, 600))  
        self.bg = ImageTk.PhotoImage(image) 

        bg_label = tk.Label(root, image=self.bg)  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
 

        #Page Title
        label = tk.Label(root, text="New Data", font=("Arial", 24, "bold"), bd = 2, relief="solid", bg= "white")
        label.pack(pady=10)

        # Label input
        tk.Label(root, text=" Enter Label: ", font=("Arial", 14, "bold"), bd = 1, relief="solid", bg= "white").pack()
        self.label_entry = tk.Entry(root, width=30)
        self.label_entry.pack(pady=10, padx=5)

        # Start button
        self.start_button = tk.Button(root, text=" Start Camera ", width= 20, height= 1, command=self.start_camera)
        self.start_button.pack(padx= 10, pady= 5)

        # Image counter
        self.counter_label = tk.Label(root, text=" Images Captured: 0 ", font=("Arial", 11, "italic"), bd = 1, relief="solid", bg= "white")
        self.counter_label.pack(padx= 10, pady= 5)

        # Video frame
        self.video_label = tk.Label(root)
        self.video_label.pack(padx= 10, pady= 5)

        # Capture button
        self.capture_button = tk.Button(root, text="Capture", command=self.capture_image, state=tk.DISABLED)
        self.capture_button.pack(padx= 10, pady= 5)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.quit_app)
        self.exit_button.pack()

        self.cap = None
        self.frame = None
        self.img_counter = 0
        self.save_dir = ""

    def start_camera(self):
        label = self.label_entry.get().strip()
        if not label:
            messagebox.showwarning("Input Error", "Please enter a label name")
            return

        base_dir = "faces_dataset"
        self.save_dir = os.path.join(base_dir, label)
        os.makedirs(self.save_dir, exist_ok=True)
        self.cap = cv2.VideoCapture(0)
        self.capture_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.update_frame()

    def update_frame(self): 
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image).resize((400, 300))
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def capture_image(self):
        if self.frame is not None:
            img_name = f"{os.path.basename(self.save_dir)}_{self.img_counter}.png"
            img_path = os.path.join(self.save_dir, img_name)
            cv2.imwrite(img_path, self.frame)
            self.img_counter += 1
            self.counter_label.config(text=f" Images Captured: {self.img_counter}")
            print(" Image saved:", img_path)

    def quit_app(self):
        if self.cap:
            self.cap.release()
        self.root.destroy()
        from gui.MainMenuApp import MainMenuApp
        new_root = tk.Tk()
        MainMenuApp(new_root)
        new_root.mainloop()


