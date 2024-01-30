import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle

class JSONCombinerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Combiner")
        self.master.geometry("500x200")

        self.style = ThemedStyle(self.master)
        self.style.set_theme("plastik")  # You can choose different themes

        self.folder_path = tk.StringVar()
        self.output_file = tk.StringVar()

        ttk.Label(master, text="Select Folder:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        ttk.Entry(master, textvariable=self.folder_path, width=30).grid(row=0, column=1, pady=10, padx=10, sticky="w")
        ttk.Button(master, text="Browse", command=self.browse_folder).grid(row=0, column=2, pady=10, padx=10, sticky="w")

        ttk.Label(master, text="Output File:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        ttk.Entry(master, textvariable=self.output_file, width=30).grid(row=1, column=1, pady=10, padx=10, sticky="w")
        ttk.Button(master, text="Save As", command=self.save_as).grid(row=1, column=2, pady=10, padx=10, sticky="w")

        ttk.Button(master, text="Combine JSON", command=self.combine_json).grid(row=2, column=1, pady=20, padx=10, sticky="ew")

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def save_as(self):
        file_selected = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        self.output_file.set(file_selected)

    def combine_json(self):
        folder_path = self.folder_path.get()

        if not os.path.exists(folder_path):
            tk.messagebox.showerror("Error", "Selected folder does not exist.")
            return

        files = os.listdir(folder_path)
        python_objects = []

        for file_name in files:
            if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith('.json'):
                with open(os.path.join(folder_path, file_name), 'r') as file:
                    python_objects.append(json.load(file))

        output_file = self.output_file.get() or f"combined_{datetime.now().strftime('%Y-%m-%d')}.json"

        with open(output_file, "w") as f:
            json.dump(python_objects, f, indent=4)

        tk.messagebox.showinfo("Success", "JSON files combined successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONCombinerGUI(root)
    root.mainloop()
