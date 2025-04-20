import tkinter as tk
from PIL import Image, ImageTk

class ManageDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Data")
        self.root.geometry("700x400+500+100")
        self.root.resizable(False, False)

        # Add Background
        image = Image.open("app_images/background_main.jpg") 
        image = image.resize((700, 400))  
        self.bg = ImageTk.PhotoImage(image) 

        bg_label = tk.Label(root, image=self.bg)  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title = tk.Label(root, text=" Data Management ", font=("Arial", 20, "bold"))
        title.pack(pady=40)

        # Test Recognition button
        test_btn = tk.Button(root, text="Create New Dataset", font=("Arial", 14), width=20, command=self.open_create_dataset)
        test_btn.place(x= 100, y = 300 )

        # Manage Data button
        manage_btn = tk.Button(root, text="Delete Dataset", font=("Arial", 14), width=20, command=self.open_delete_dataset)
        manage_btn.place(x= 400, y= 300)

        # Manage Data button
        back_btn = tk.Button(root, text="Back", font=("Arial", 12), width=15, command=self.open_main_menu)
        back_btn.place(x= 280, y= 360)


    def open_delete_dataset(self):
        self.root.destroy()
        from gui.DeleteDatasetApp import DeleteDatasetApp
        new_root = tk.Tk()
        DeleteDatasetApp(new_root)
        new_root.mainloop()

    def open_create_dataset(self):
        self.root.destroy()
        from gui.NewDataApp import NewDataApp
        new_root = tk.Tk()
        NewDataApp(new_root)
        new_root.mainloop()

    def open_main_menu(self):
        self.root.destroy()
        from gui.MainMenuApp import MainMenuApp
        new_root = tk.Tk()
        MainMenuApp(new_root)
        new_root.mainloop()