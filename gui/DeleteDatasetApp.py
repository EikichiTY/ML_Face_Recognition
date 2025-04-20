import os
import shutil
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from PIL import Image, ImageTk

class DeleteDatasetApp:
    def __init__(self, root, dataset_path="faces_dataset"):
        self.root = root
        self.root.title("Delete Datasets")
        self.root.geometry("700x600+500+100")
        self.root.resizable(False, False)
        
        # Add background
        image = Image.open("app_images/background.png")
        image = image.resize((700, 600))  
        self.bg = ImageTk.PhotoImage(image)

        bg_label = tk.Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        #Add datasets for actions
        self.dataset_path = dataset_path
        self.protected_folders = {"Lionel Messi", "Tony Stark"}

        tk.Label(root, text="Select a dataset to delete:", font=("Arial", 14)).pack(pady=10)
        tk.Label(root, text="! Lionel Messi and Tony Stark are default test datasets they cannot be deleted !", font=("Arial", 11,"italic")).pack(pady=10)

        # Scrollbar + Listbox
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = Listbox(root, width=40, height=15, font=("Arial", 12))
        self.listbox.pack(padx=20, pady=10)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.bind("<<ListboxSelect>>", self.check_protection)

        self.delete_button = tk.Button(
            root,
            text="Delete Selected Dataset",
            command=self.delete_selected,
            bg="red",
            fg="white",
            highlightbackground="black",
            font=("Arial", 12, "bold"),
            state=tk.DISABLED
        )
        self.delete_button.pack(pady=20)

        #Back Button
        self.back_button = tk.Button(
            root,
            text="Back", 
            font=("Arial", 12), 
            width=15, 
            highlightbackground="black",
            command=self.open_manage_data)
        
        self.back_button.pack(pady=20)

        self.load_datasets()

    def load_datasets(self):
        self.listbox.delete(0, tk.END)
        if os.path.exists(self.dataset_path):
            for folder in os.listdir(self.dataset_path):
                folder_path = os.path.join(self.dataset_path, folder)
                if os.path.isdir(folder_path):
                    self.listbox.insert(tk.END, folder)

    def check_protection(self, event):
        selected = self.listbox.get(tk.ACTIVE)
        if selected in self.protected_folders:
            self.delete_button.config(state=tk.DISABLED)
        else:
            self.delete_button.config(state=tk.NORMAL)

    def delete_selected(self):
        selected = self.listbox.get(tk.ACTIVE)
        if not selected or selected in self.protected_folders:
            return

        full_path = os.path.join(self.dataset_path, selected)
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete the dataset: '{selected}'?"
        )
        if confirm:
            try:
                shutil.rmtree(full_path)
                messagebox.showinfo("Success", f"'{selected}' has been deleted.")
                self.load_datasets()
                self.delete_button.config(state=tk.DISABLED)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete folder: {e}")


    def open_manage_data(self):
        self.root.destroy()
        from gui.ManageDataApp import ManageDataApp
        new_root = tk.Tk()
        ManageDataApp(new_root)
        new_root.mainloop()


# Test
if __name__ == "__main__":
    root = tk.Tk()
    app = DeleteDatasetApp(root)
    root.mainloop()
