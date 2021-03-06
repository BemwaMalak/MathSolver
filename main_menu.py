#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 25, 2021 10:23:37 PM CAT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk

from sympy.functions.elementary.complexes import im
py3 = True
import main_menu_support
import os.path

from Eigen import eigen
from vector_operations import vector_operations
from Determinant import determinant
from Laplace import laplace
from inverse_Laplace import inverse_laplace
import interface

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    main_menu_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_menu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def load_eigen(self, top=None):
        top.destroy()
        eigen.vp_start_gui()
    def load_vector(self, top=None):
        top.destroy()
        vector_operations.vp_start_gui()
    def load_determinant(self, top=None):
        top.destroy()
        determinant.vp_start_gui()
    def load_laplace_transform(self, top=None):
        top.destroy()
        laplace.vp_start_gui()
    def load_laplace_inverse(self, top=None):
        top.destroy()
        inverse_laplace.vp_start_gui()
    def load_interface(self, top=None):
        top.destroy()
        interface.vp_start_gui()
        

        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1080x720+255+83")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(0,  0)
        top.title("main menu")
        top.configure(background="#ffffff")

        

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.056, rely=0.931, height=31, width=956)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 17.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.194, rely=0.264, height=281, width=74)
        self.Label2.configure(activebackground="#f0f0f0f0f0f0")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(borderwidth="0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 16.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img1)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.278, rely=0.278, height=64, width=597)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=lambda: self.load_eigen(top))
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 11.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img2)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.278, rely=0.375, height=64, width=597)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(command=lambda: self.load_vector(top))
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 12.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img3)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.292, rely=0.458, height=74, width=567)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(command=lambda: self.load_determinant(top))
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 13.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button3.configure(image=_img4)
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Button''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.294, rely=0.569, height=44, width=317)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(borderwidth="0")
        self.Button4.configure(command=lambda: self.load_laplace_transform(top))
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 15.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Button4.configure(image=_img5)
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Button''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.917, rely=0.056, height=44, width=37)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(borderwidth="0")
        self.Button5.configure(command=lambda: self.load_interface(top))
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 10.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Button5.configure(image=_img6)
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Button''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.6, rely=0.561, height=54, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#ffffff")
        self.Button6.configure(borderwidth="0")
        self.Button6.configure(command=lambda: self.load_laplace_inverse(top))
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,r"Assessts/menu_assists/Asset 14.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.Button6.configure(image=_img7)
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Button''')

if __name__ == '__main__':
    vp_start_gui()





