
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_register")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
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
    736.0,
    172.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_1.place(
    x=602.0,
    y=152.0,
    width=268.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    736.0,
    246.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_2.place(
    x=602.0,
    y=226.0,
    width=268.0,
    height=38.0
)

canvas.create_text(
    595.0,
    128.0,
    anchor="nw",
    text="Username",
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

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    736.0,
    318.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_3.place(
    x=602.0,
    y=298.0,
    width=268.0,
    height=38.0
)

canvas.create_text(
    595.0,
    274.0,
    anchor="nw",
    text="Kota",
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
    28.0,
    128.0,
    anchor="nw",
    text="Pendataan Kasus COVID-19\nIndonesia",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    595.0,
    430.0,
    anchor="nw",
    text="Sudah punya akun? ",
    fill="#000000",
    font=("Inter", 17 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=768.0,
    y=430.0,
    width=52.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=631.0,
    y=369.0,
    width=209.0,
    height=38.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    238.0,
    407.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
