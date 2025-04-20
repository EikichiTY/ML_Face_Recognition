import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
from core.FaceTrainer import FaceTrainer

class MainMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("700x400+500+100")
        self.root.resizable(False, False)

        # Charger l'image
        image = Image.open("app_images/background_main.jpg") 
        image = image.resize((700, 400))  
        self.bg = ImageTk.PhotoImage(image) 

        bg_label = tk.Label(root, image=self.bg)  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title = tk.Label(root, text=" Facial Recognition Menu ", font=("Arial", 20, "bold"))
        title.pack(pady=40)

        # Test Recognition button
        test_btn = tk.Button(root, text="Test Recognition", font=("Arial", 14), width=20, command=self.open_test)
        test_btn.place(x= 100, y = 320 )

        # Manage Data button
        manage_btn = tk.Button(root, text="Manage Data", font=("Arial", 14), width=20, command=self.open_manage_data)
        manage_btn.place(x= 400, y= 320)


    def open_manage_data(self):
        self.root.destroy()
        from gui.ManageDataApp import ManageDataApp
        new_root = tk.Tk()
        ManageDataApp(new_root)
        new_root.mainloop()

    def open_test(self):
        # Créer la fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.geometry("300x100+700+300")
        popup.title("Please wait")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        label = tk.Label(popup, text="Training data, please wait...", font=("Arial", 12))
        label.pack(pady=20)

        # Lancer l'entraînement dans un thread, mais garder le contrôle UI dans le thread principal
        def background_task():
            data = FaceTrainer()
            data.train_all()
            self.root.after(100, lambda: self.finish_training(popup))  # revenir dans le thread principal

        Thread(target=background_task).start()


    def finish_training(self, popup):
        popup.destroy()
        self.root.destroy()

        from gui.FaceRecognizerApp import FaceRecognizerApp
        new_root = tk.Tk()
        app = FaceRecognizerApp(new_root)
        Thread(target=app.start_recognition).start()
        new_root.mainloop()

