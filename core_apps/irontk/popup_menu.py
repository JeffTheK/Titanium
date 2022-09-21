import tkinter as tk

class PopupMenu(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master, tearoff=0, cursor="hand2")
        master.bind("<Button-3>", lambda event: popup_right_click_menu(master, event)) # Button-2 on Aqua

def popup_right_click_menu(master, event):
        try:
            master.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            master.popup_menu.grab_release()