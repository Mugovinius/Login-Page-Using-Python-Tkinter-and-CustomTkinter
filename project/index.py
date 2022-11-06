from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image

#set default customtkinter theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
spacer=" "#empty space to position title at the center
root.title(200*spacer+"SAMARIA MILK GROUP")
root.geometry("1360x800")
#set page logo
root.iconbitmap("images/logo1.ico")
root.state('zoomed')
class Login:
    def __init__(self, master) -> None:
        #create label widget containing logo
        self.title_frame=Frame(master)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1=" LOGIN"
        self.img=ImageTk.PhotoImage(Image.open('images/Samaria Mega Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,fg_color="maroon",text_color="white", text_font=("Consollas 10", -30, "italic"),width=200,height=35)
        self.my_sub_text.grid(row=1, column=1,padx=10,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1, fg_color="orange",text_color="white", text_font=("Consollas 10", -35, "bold","underline"),width=300,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4, padx=10)
        #signup frame
        self.signup_frame=customtkinter.CTkFrame(master,corner_radius=8)
        self.signup_frame.pack(anchor="e",pady=5)
        self.signup_button=customtkinter.CTkButton(self.signup_frame, text="Sign Up",fg_color="purple",text_color="white",text_font=("Consollas 10", -20,"bold"),width=200, height=30,command="")
        self.signup_button.pack(padx=30)
        #right frame
        self.right_frame=customtkinter.CTkFrame(master,border_color="green",border_width=5,corner_radius=8,width=800,height=600)
        self.right_frame.pack(fill=BOTH, expand=YES)
        
        #leftframe
        self.left_frame=customtkinter.CTkFrame(self.right_frame,corner_radius=10,width=400,height=450)
        self.left_frame.pack(anchor="center",pady=10)
        #login
        #variable
        self.c_v1=IntVar(value=0)
        self.login_label=customtkinter.CTkLabel(self.left_frame, text=" USER LOGIN", fg_color="darkblue",text_color="white", text_font=("Consollas 10", -40, "underline", "bold"),width=300,height=50)
        self.login_label.grid(row=0, column=0, columnspan=15, rowspan=2, pady=10,padx=30,sticky=EW)
        self.img1= ImageTk.PhotoImage(Image.open('images/user.png'))
        self.image_label1=customtkinter.CTkLabel(self.left_frame, image=self.img1)
        self.image_label1.grid(row=2, column=0, columnspan=15,padx=30)
        self.username_label=customtkinter.CTkLabel(self.left_frame, text="UserName:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -25, "bold"),width=200,height=35)
        self.username_label.grid(row=3, column=0,columnspan=8, rowspan=2,pady=20, padx=30)
        self.username_entry=customtkinter.CTkEntry(self.left_frame, width=300,height=40,corner_radius=8,placeholder_text="Enter Username",placeholder_text_color="purple",border_color="blue")
        self.username_entry.grid(row=3, column=8,rowspan=2,pady=20,padx=20,columnspan=7)
        self.password_label=customtkinter.CTkLabel(self.left_frame, text="Password:",fg_color="maroon",text_color="white",text_font=("Consollas 10", -25 ,"bold"),width=200,height=35)
        self.password_label.grid(row=5, column=0,columnspan=8,padx=30)
        self.password_entry=customtkinter.CTkEntry(self.left_frame,show="*", width=300,height=40,corner_radius=8,placeholder_text="Enter Password",placeholder_text_color="purple",border_color="blue")
        self.password_entry.grid(row=5, column=8,columnspan=7)
        self.showpassword_ck=customtkinter.CTkCheckBox(self.left_frame,text="Show Password",text_font=("Consollas 10", -20, "bold"),text_color="green",variable=self.c_v1,command=self.my_show)
        self.showpassword_ck.grid(row=6,column=0,padx=20,pady=10,columnspan=10)
        self.forgot_password_button=customtkinter.CTkButton(self.left_frame,text="Forgot Password ?",fg_color="purple",text_color="white",text_font=("Consollas 10", -15,"bold"),width=200,height=30,command="")
        self.forgot_password_button.grid(row=6,column=10,columnspan=5,padx=10)
        self.login_button=customtkinter.CTkButton(self.left_frame, text="LOGIN", fg_color="maroon",text_color="white",text_font=("Consollas 10", -25,"bold"),width=250, height=50, command="")
        self.login_button.grid(row=7, column=0, columnspan=15,pady=10,padx=30,sticky=EW)
        
    #show password
    def my_show(self):
        if(self.c_v1.get()==0):
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
#load page
app=Login(root)
root.mainloop()
