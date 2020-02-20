#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import instagram
import tkinter as tk
import threading as thread
#print("Enter The UserName: ")
#username = input('Instagram.com/')
username = "peyman_majidi_moein"

window = tk.Tk()


fl = -1

def fetch_instagram(username, lblFollowings, lblFollowers):
    followers, following, posts = instagram.fetch_data(username)
    lblFollowings["text"] = following
    lblFollowers["text"] = followers
    print("update done")
    thread.Timer(5, fetch_instagram, [username, lblFollowings, lblFollowers] ).start()


def draw_ui(window):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Serif} -size 30 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family FreeSans -size 72 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        window.geometry("502x259+447+316")
        window.minsize(1, 1)
        window.maxsize(1905, 1050)
        window.resizable(1, 1)
        window.title("PyInstagram")

        lblFollowings = tk.Label(window)
        lblFollowings.place(relx=0.02, rely=0.425, height=131, width=217)
        lblFollowings.configure(background="#a3a3a3")
        lblFollowings.configure(font=font12)
        lblFollowings.configure(text='''0''')

        lblFollowers = tk.Label(window)
        lblFollowers.place(relx=0.538, rely=0.425, height=131, width=217)
        lblFollowers.configure(activebackground="#f9f9f9")
        lblFollowers.configure(background="#a3a3a3")
        lblFollowers.configure(font="-family {FreeSans} -size 72")
        lblFollowers.configure(text='''0''')

        Label3 = tk.Label(window)
        Label3.place(relx=0.02, rely=0.347, height=21, width=217)
        Label3.configure(activebackground="#ed2fae")
        Label3.configure(activeforeground="white")
        Label3.configure(background="#d81c1c")
        Label3.configure(foreground="#ffffff")
        Label3.configure(text='''Following''')

        Label3_4 = tk.Label(window)
        Label3_4.place(relx=0.538, rely=0.347, height=21, width=217)
        Label3_4.configure(activebackground="#ed2fae")
        Label3_4.configure(activeforeground="white")
        Label3_4.configure(background="#3a5fd8")
        Label3_4.configure(foreground="#ffffff")
        Label3_4.configure(text='''Followers''')

        lblTitle = tk.Label(window)
        lblTitle.place(relx=0.022, rely=0.012, height=80, width=417)
        lblTitle.configure(font=font10)
        lblTitle.configure(foreground="#742f96")
        lblTitle.configure(text=username)
        lblTitle.bind("<Button-1>",lambda x: fetch_instagram(username, lblFollowings, lblFollowers)) # when click on username
        
        fetch_instagram(username, lblFollowings, lblFollowers) # first time


draw_ui(window)
window.mainloop()


