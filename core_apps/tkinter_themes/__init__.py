import tkinter.ttk as ttk

def setup_global_tkinter_theme(root):
    root.tk.call('source', 'core_apps/Forest-ttk-theme/forest-light.tcl')
    ttk.Style().theme_use('forest-light')