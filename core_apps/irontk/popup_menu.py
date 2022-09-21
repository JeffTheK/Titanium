import tkinter as tk

class PopupMenu(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=0, cursor="hand2")
        master.bind("<Button-3>", lambda event: self.popup_right_click_menu(event)) # Button-2 on Aqua

    def popup_right_click_menu(self, event):
            try:
                self.tk_popup(event.x_root, event.y_root, 0)
            finally:
                self.grab_release()