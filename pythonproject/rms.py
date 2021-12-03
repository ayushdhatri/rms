from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("Restaurant Management System ")
root.geometry("1000x667")
root.resizable(False, False)
#================ Function for program===================
def checklogin():
    pass

#==========Backgroud Image==============
bgi = ImageTk.PhotoImage(file="/Users/ayushsolanki/Desktop/img/loginpage1.jpeg")
bg_image = Label(root, image=bgi)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)
# =====================Main frame====================
main_frame = Frame(root, bg="#5D6D7E", bd=4, relief="sunken")
main_frame.place(x=32, y=120, height=340, width=500)
# =======set username password========================
login = Label(main_frame, text="Login Here ", font=("Helvetica", 42), fg="black", bd=5, relief="raised")
login.grid(row=0, column=0)
user = Label(main_frame, text="USERNAME ", fg="black", font=("Helvetica", 15), bg="green")
user.place(x=40, y=100)
user_name = Entry(main_frame, bd=3)
user_name.place(x=150, y=100)
password = Label(main_frame, text="PASSWORD ", fg="black", font=("Helvetica", 15), bg="green")
password.place(x=40, y=200)
user_password = Entry(main_frame, bd=3, show="*")
user_password.place(x=150, y=200)
#=============Login button to Restaurant Management System======================
login_button = Button(main_frame, text="LOGIN", font=("Helvetica", 15), bg="red", fg="black", )
login_button.place(x=190, y=270)

















root.mainloop()



