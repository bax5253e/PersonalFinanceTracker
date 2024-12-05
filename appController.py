import tkinter as tk

from appModel import AppModel

from mainView import MainView
from addEditTransactionView import AddEditTransactionView
from viewTransactionsView import ViewTransactionsView
from generateReportsView import GenerateReportsView

class AppController:
    def __init__(self):
        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")

        #Create the model
        self.model = AppModel()

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        
        # Populate the frames dictionary with the views
        for view_name in [ MainView, 
                          AddEditTransactionView, 
                          ViewTransactionsView, 
                          GenerateReportsView ]:
            frame = view_name(self.container, self)
            self.frames[view_name.__name__] = frame

        # Show the main view
        self.show_frame("MainView")

    def show_frame(self, view_name):
        frame = self.frames[view_name]
        frame.tkraise()

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.quit()