
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_tampilDataKum")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(tampilDataKum)
        self.title('Pendataan Kasus Covid-19 Indonesia')
        self.geometry("1000x600")
        self.configure(bg = "#FFFFFF")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

class tampilDataKum(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master) 
        #window = Toplevel
        master.geometry("1000x600")
        master.title('Pendataan Kasus Covid-19 Indonesia')
        master.configure(bg = "#FFFFFF")
        #declaring variable for Login    

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
            385.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        entry_1.place(
            x=616.0,
            y=365.0,
            width=268.0,
            height=38.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            750.0,
            459.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        entry_2.place(
            x=616.0,
            y=439.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            609.0,
            341.0,
            anchor="nw",
            text="Sembuh",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            751.0,
            311.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        entry_3.place(
            x=617.0,
            y=291.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            610.0,
            267.0,
            anchor="nw",
            text="Kasus Positif",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            750.0,
            237.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        entry_4.place(
            x=616.0,
            y=217.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            609.0,
            193.0,
            anchor="nw",
            text="Tanggal",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            750.0,
            164.0,
            image=entry_image_5
        )
        entry_5 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        entry_5.place(
            x=616.0,
            y=144.0,
            width=268.0,
            height=38.0
        )

        canvas.create_text(
            609.0,
            120.0,
            anchor="nw",
            text="Kota",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            625.0,
            152.0,
            anchor="nw",
            text="Autofill per User",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            625.0,
            226.0,
            anchor="nw",
            text="Ambil dari Input",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            625.0,
            300.0,
            anchor="nw",
            text="Ambil dari Database",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            625.0,
            373.0,
            anchor="nw",
            text="Ambil dari Database",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            625.0,
            447.0,
            anchor="nw",
            text="Ambil dari Database",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            609.0,
            415.0,
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
            text="Data Kumulatif",
            fill="#FFFFFF",
            font=("Inter SemiBold", 30 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            229.0,
            414.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(DataKum),
            relief="flat"
        )
        button_1.place(
            x=37.0,
            y=8.0,
            width=102.0,
            height=37.0
        )
        master.resizable(False, False)
        master.mainloop()

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()
