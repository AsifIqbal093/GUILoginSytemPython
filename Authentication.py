#all the packages neccessary are imported here......

from tkinter import *
from tkinter import font
from PIL import ImageTk
from tkinter import messagebox

class Login:
    
    def __init__(self, root):
        self.root= root
        self.root.title("KHAZANA GREES")
        self.root.geometry("1199x600+100+50")
        # self.root.resizable(False, False)
        #Setting up background image........
        self.bg = ImageTk.PhotoImage(file="Images/canvas_bg.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login form for authentication
        
        login_frame = Frame(self.root, background="#EACCD3")
        login_frame.place(x=550, y=150,height=340, width=500)

        title = Label(login_frame, text="Login Here", font=("Impact",35,"bold"),fg="#C70039", bg="#EACCD3").place(x=140, y=30)
        Descp = Label(login_frame, text="User Login Form", font=("Goudy old style",15,"bold"),fg="#C70039", bg="#EACCD3").place(x=180, y=90)
        
        lbl_username = Label(login_frame, text="Username", font=("Goudy old style",15,"bold"),fg="grey", bg="#EACCD3").place(x=90, y=140)
        self.username_txt = Entry(login_frame,font=("Times new Roman", 15), bg="lightgrey")
        self.username_txt.place(x=90,y=170, width=350,height=30)
        
        lbl_password = Label(login_frame, text="Password", font=("Goudy old style",15,"bold"),fg="grey", bg="#EACCD3").place(x=90, y=205)
        self.password_txt = Entry(login_frame,font=("Times new Roman", 15), bg="lightgrey")
        self.password_txt.place(x=90,y=235, width=350,height=30)
        
        forget_btn = Button(login_frame, text="Forgot Password?", bd=0, fg="#C70039", bg="#EACCD3", font=("Times new Roman", 12)).place(x=90, y=275)
        Login_btn = Button(self.root,command=self.Login_function, text="Login",  fg="#EACCD3", bg="#C70039", font=("Times new Roman", 20)).place(x=710, y=470, width=180, height=40)

    #Function for authentication user into the system.....
    def Login_function(self):
        if self.password_txt.get() == "" or self.username_txt.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        elif self.password_txt.get() != "12345" or self.username_txt.get() != "Admin":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            messagebox.showinfo("Login Success", f"Wellcome! Mr.{self.user_name.txt.get()}", parent=self.root)

#defining TK instance and assigning it into variable 
root = Tk()
#instance object of Login Class
login_obj = Login(root)

root.mainloop()