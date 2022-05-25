
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from cgitb import text
from pathlib import Path
import requests

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk
from datetime import datetime


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_tambahdata")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TambahData)
        self.title('Pendataan Kasus Covid-19 Indonesia')
        self.geometry("1000x600")
        self.configure(bg = "#FFFFFF")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

class TambahData(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master) 
        #window = Toplevel
        master.geometry("1000x600")
        master.title('Pendataan Kasus Covid-19 Indonesia')
        master.configure(bg = "#FFFFFF")
        #declaring variable for Login

        #declaring variable for Login
        global  meninggal
        global positif
        global sembuh

        meninggal = StringVar ()
        positif = StringVar ()
        sembuh= StringVar ()


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
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            750.0,
            357.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=positif
        )
        entry_1.place(
            x=616.0,
            y=337.0,
            width=268.0,
            height=38.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            750.0,
            431.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=sembuh
        )
        entry_2.place(
            x=616.0,
            y=411.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            609.0,
            313.0,
            anchor="nw",
            text="Sembuh",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            751.0,
            283.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            textvariable=meninggal
        )
        entry_3.place(
            x=617.0,
            y=263.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            610.0,
            239.0,
            anchor="nw",
            text="Kasus Positif",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        #entry_4 = tanggal
        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            750.0,
            209.0,
            image=entry_image_4
        )


        canvas.create_text(
            616.0,
            195.0,
            anchor="nw",
            text= datetime.today().strftime('%Y-%m-%d'),
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            609.0,
            165.0,
            anchor="nw",
            text="Tanggal",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            609.0,
            387.0,
            anchor="nw",
            text="Meninggal",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            459.0,
            600.0,
            fill="#00D1FF",
            outline="")

        canvas.create_text(
            37.0,
            145.0,
            anchor="nw",
            text="Pendataan Kasus COVID-19\nIndonesia",
            fill="#FFFFFF",
            font=("Inter SemiBold", 30 * -1)
        )

        canvas.create_text(
            37.0,
            77.0,
            anchor="nw",
            text="Tambah Data",
            fill="#FFFFFF",
            font=("Inter SemiBold", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: tambahkanData(),
            relief="flat"
        )
        button_1.place(
            x=703.0,
            y=469.0,
            width=93.0,
            height=32.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            229.0,
            414.0,
            image=image_image_1
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame("dataKum"),
            relief="flat"
        )
        button_2.place(
            x=37.0,
            y=8.0,
            width=102.0,
            height=37.0
        )

        self.notif = canvas.create_text(
                        623.0,
                        110.9999999999999,
                        anchor="nw",
                        text="",
                        fill="#ff0000",
                        font=("Inter", 17 * -1)
        )

        def tambahkanData():
            meninggal2 = meninggal.get()
            sembuh2 = sembuh.get()
            positif2 = positif.get()
            date = requests.get("http://localhost:5000/kasus/date")
            print(date.text)
            import login
            id = login.id_user

            try:
                if meninggal2=='' or sembuh2=='' or positif2=='':
                    canvas.itemconfig(self.notif, text= "tidak boleh ada data yang kosong")
                else:
                    url = 'http://localhost:5000/kasus'
                    myjson = {
                        'positif':positif2,
                        'sembuh': sembuh2,
                        'meninggal':meninggal2,
                        'tanggal': date.text,
                        'user_id': id
                        }
                    x = requests.post(url, json = myjson)
                    print(x.status_code)
                    canvas.itemconfig(self.notif, text= "Data berhasil ditambahkan!")
            except:
                self.entry_1.delete(0, 'end')
                self.entry_2.delete(0, 'end')
                canvas.itemconfig(self.notif, text= "Gagal Menghubungkan ke Server")

        master.resizable(False, False)
        master.mainloop()



if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()
