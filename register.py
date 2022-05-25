
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


#import requests
from cgitb import text
from pathlib import Path
import requests

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_register")

nama_reg=""
surel_reg=""
password_reg=""
password_konf_reg=""

def relative_to_assets_register(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Register)
        self.title('Pendataan Kasus Covid-19 Indonesia')
        self.geometry("1000x600")
        self.configure(bg = "#FFFFFF")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

# Page Register
class Register(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.geometry("1000x600")
        master.title('Pendataan Kasus Covid-19 Indonesia')
        #window.configure(bg = "#FFFFFF")

        global nama_reg
        global surel_reg
        global password_reg
        global password_konf_reg

        nama_reg = StringVar()
        surel_reg = StringVar()
        password_reg = StringVar()
        password_konf_reg = StringVar()

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
            file=relative_to_assets_register("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            736.0,
            172.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=nama_reg
        )
        entry_1.place(
            x=602.0,
            y=152.0,
            width=268.0,
            height=38.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets_register("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            737.0,
            98.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=surel_reg
        )
        entry_2.place(
            x=603.0,
            y=78.0,
            width=268.0,
            height=38.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets_register("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            736.0,
            246.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=password_reg
        )
        entry_3.place(
            x=602.0,
            y=226.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            595.0,
            128.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            594.0,
            54.0,
            anchor="nw",
            text="Nama",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            595.0,
            202.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets_register("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            736.0,
            319.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=password_konf_reg
        )
        entry_4.place(
            x=602.0,
            y=299.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            595.0,
            275.0,
            anchor="nw",
            text="Konfirmasi Password",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            595.0,
            347.0,
            anchor="nw",
            text="Kota",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        n = StringVar()
        self.kotaTerpilih = ttk.Combobox(master, width = 27,state="readonly", 
                                    textvariable = n,font=("Inter", 12 * -1))

        # Adding combobox drop down list
        self.kotaTerpilih['values'] = (' Jakarta', 
                                ' Tangerang',
                                ' Depok',
                                ' Bekasi',
                                ' Bogor',
                                ' Palembang', 
                                )

        self.kotaTerpilih.bind("<<ComboboxSelected>>",lambda e: master.focus())

        self.kotaTerpilih.place(
            x=602.0,
            y=374.0,
            width=268.0,
            height=38.0
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            459.0,
            600.0,
            fill="#00D1FF",
            outline="")

        canvas.create_text(
            28.0,
            128.0,
            anchor="nw",
            text="Pendataan Kasus COVID-19\nIndonesia",
            fill="#FFFFFF",
            font=("Inter SemiBold", 30 * -1)
        )

        canvas.create_text(
            595.0,
            500.0,
            anchor="nw",
            text="Sudah punya akun? ",
            fill="#000000",
            font=("Inter", 17 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets_register("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame("login"),
            relief="flat"
        )
        button_1.place(
            x=759.0,
            y=500.0,
            width=45.0,
            height=21.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets_register("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:register(),
            relief="flat"
        )
        button_2.place(
            x=631.0,
            y=439.0,
            width=209.0,
            height=38.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets_register("image_1.png"))
        image_1 = canvas.create_image(
            229.0,
            413.0,
            image=image_image_1
        )


        self.notif = canvas.create_text(
                        594.0,
                        520.9999999999999,
                        anchor="nw",
                        text="",
                        fill="#ff0000",
                        font=("Inter", 17 * -1)
        )

        

        def register():
            import login
            global new_register
            new_register = 1
            email=surel_reg.get()
            name=nama_reg.get()
            pwd=password_reg.get()
            confPwd=password_konf_reg.get()
            kota= str(self.kotaTerpilih.get())
            print(kota)
            # self.master.switch_frame(Login)
            #applying empty validation
            try:
                if email=='' or pwd=='' or confPwd=='' or name=='':
                    canvas.itemconfig(self.notif, text= "tidak boleh ada data yang kosong")
                else:
                    print(email,pwd)
                    url = 'http://localhost:5000/users'
                    myjson = {
                        'name':name,
                        'email': email,
                        'password':pwd,
                        'confPassword':confPwd,
                        'kota': kota
                        }
                    x = requests.post(url, json = myjson)
                    print(x.status_code)
                    canvas.itemconfig(self.notif, text= "Akun berhasil didaftarkan")
                    # #print the response text (the content of the requested file):
                    # if x.status_code == 200:
                    #     self.master.switch_frame(Login)
                    # else:
                    #     self.entry_1.delete(0, 'end')
                    #     self.entry_2.delete(0, 'end')
                    #     jsonResponse = x.json()
                    #     self.canvas.itemconfig(self.errorregis, text=jsonResponse["msg"])
                    #     print(x.text)
            except:
                entry_1.delete(0, 'end')
                entry_2.delete(0, 'end')
                canvas.itemconfig(self.notif, text= "Gagal Menghubungkan ke Server")


        master.resizable(False, False)
        master.mainloop()

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()