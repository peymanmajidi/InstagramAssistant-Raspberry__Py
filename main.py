import instagram
from tkinter import *
from tkinter import messagebox
 

a,b,c = instagram.fetch_data("peyman_majidi_moein")
#setup window
window = Tk()
window.title("Instagram Follower Counter")
window.geometry('600x400')
window.resizable(False, False)

#setup GUI elements
Label(window, text="Welcome to", font=("Arial", 19)).grid(column=0, row=0, sticky = 'w', columnspan = 3)
Label(window, text="Instagram Checker", font=("Arial Bold", 25)).grid(column=2, row=0, sticky = 'w', columnspan = 3)
lbl = Label(window, text="Instagram.com/", font=("Arial", 15))
lbl.grid(column=0, row=1, sticky = 'w', columnspan = 1)
txtUsername = Entry(window,width=20 , font = ('tahoma', 15) )
txtUsername.grid(column=2, row=1 , sticky = 'w', columnspan = 1)

def load_data(): # load data from json and display them
    username = txtUsername.get()
    if len(username) == 0:
        messagebox.showerror('Entry Error','Username is empty!')
        return False
    output = ''
    lblResult.configure(text="loading ...")
    followers, following, posts = instagram.fetch_data(username)
    if followers > -1:
        output = f"""{username}'s Account Detail:
        Followers: {followers} 
        Following: {following}
        Posts: {posts}"""
        lblResult.configure(text=output , bg = 'lightgray')
    else:
        output ='Internet Connection Error'
        lblResult.configure(text=output , bg = 'red')
    
def set_text(entry , text): # set custom text to Entry textbox
    entry.delete(0,END)
    entry.insert(0,text)
    return
    
Button(window, text=" Search ",width = 20, bg ='violet', command=load_data, font=("Arial", 15)).grid(column=2, row=5, sticky = 'w', columnspan = 4)
lblResult = Label(window, text="[ result ]", font=("Arial Bold", 15),  justify=LEFT)
lblResult.grid(column=0, row=6, sticky = 'w', columnspan = 4)

set_text(txtUsername,"peyman_majidi_moein") # default username
txtUsername.focus()

window.mainloop()