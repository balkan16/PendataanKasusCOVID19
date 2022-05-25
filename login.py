
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import requests

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_login")


def relative_to_assets_login(path: str) -> Path:
    return ASSETS_PATH / Path(path)
id_user = None

new_register = 0
class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.title('Pendataan Kasus Covid-19 Indonesia')
        self.geometry("1000x600")
        self.configure(bg = "#FFFFFF")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame    


# Page Login
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        #window = Toplevel
        
        #declaring variable for Login
        global  message
        global username
        global password
        username = StringVar ()
        password = StringVar ()
        message= StringVar ()

        master.geometry("1000x600")
        master.title('Pendataan Kasus Covid-19 Indonesia')
        #window.configure(bg = "#FFFFFF")

        canvas = Canvas(
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        entry_image_1 = PhotoImage(
            file=relative_to_assets_login("entry_1.png"))
            
        entry_bg_1 = canvas.create_image(
            736.0,
            171.9999999999999,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable= username
        )
        entry_1.place(
            x=602.0,
            y=151.9999999999999,
            width=268.0,
            height=38.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets_login("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            736.0,
            245.9999999999999,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable= password
        )
        entry_2.place(
            x=602.0,
            y=225.9999999999999,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            595.0,
            127.99999999999989,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets_login("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=756.0,
            y=288.9999999999999,
            width=123.0,
            height=21.0
        )

        canvas.create_text(
            595.0,
            201.9999999999999,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_rectangle(
            0.0,
            1.1368683772161603e-13,
            459.0,
            600.0000000000001,
            fill="#00D1FF",
            outline="")

        canvas.create_text(
            28.0,
            127.99999999999989,
            anchor="nw",
            text="Pendataan Kasus COVID-19\nIndonesia",
            fill="#FFFFFF",
            font=("Inter SemiBold", 30 * -1)
        )

        canvas.create_text(
            595.0,
            349.9999999999999,
            anchor="nw",
            text="Belum punya akun? ",
            fill="#000000",
            font=("Inter", 14 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets_login("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame("register"),
            relief="flat"
        )
        button_2.place(
            x=765.0,
            y=349.9999999999999,
            width=79.0,
            height=21.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets_login("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command= lambda:login(),
            relief="flat"
        )
        button_3.place(
            x=595.0,
            y=281.9999999999999,
            width=93.0,
            height=32.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets_login("image_1.png"))
        image_1 = canvas.create_image(
            229.0,
            413.9999999999999,
            image=image_image_1
        )

        self.notif = canvas.create_text(
                        595.0,
                        329.9999999999999,
                        anchor="nw",
                        text="",
                        fill="#ff0000",
                        font=("Inter", 17 * -1)
        )

        def login():
        #getting form data
            global id_user
            uname=username.get()
            pwd=password.get()
            #applying empty validation
            if uname=='' or pwd=='':
                canvas.itemconfig(self.notif, text= "username dan password tidak boleh kosong")
            else:
                print(uname,pwd)
                url = 'http://localhost:5000/users/login'
                myjson = {
                    'email': uname,
                    'password':pwd
                    }
                x = requests.post(url, json = myjson)
                #print the response text (the content of the requested file):
                if x.status_code == 200:
                    print(x.json())
                    response = x.json()
                    id_user = response['userId']
                    print(id_user)
                    print("here")
                    #navigate to menu page
                    master.switch_frame("homepage")
                    
                else:
                    entry_1.delete(0, 'end')
                    entry_2.delete(0, 'end')
                    jsonResponse = x.json()
                    canvas.itemconfig(self.notif, text= jsonResponse["msg"])
          
        # Muncul setelah Register akun baru
        if(new_register == 1):
            canvas.create_text(
                650.0,
                100.0,
                anchor="nw",
                text="Akun Baru Terdaftar!",
                fill="#000000",
                font=("Inter", 20 * -1)
            )
        master.resizable(False, False)
        master.mainloop()

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()
