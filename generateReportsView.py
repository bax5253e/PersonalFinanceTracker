import tkinter as tk

class GenerateReportsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, text="Generate Reports", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Go Back", font=("Arial", 16), command=lambda: controller.show_frame("MainView")).pack(pady=10)
        