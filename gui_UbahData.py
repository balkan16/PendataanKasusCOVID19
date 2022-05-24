
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_UbahData")


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
    750.0,
    357.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
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
    highlightthickness=0
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
    highlightthickness=0
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

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    750.0,
    209.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_4.place(
    x=616.0,
    y=189.0,
    width=268.0,
    height=38.0
)

canvas.create_text(
    609.0,
    165.0,
    anchor="nw",
    text="Tanggal",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    750.0,
    136.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_5.place(
    x=616.0,
    y=116.0,
    width=268.0,
    height=38.0
)

canvas.create_text(
    609.0,
    92.0,
    anchor="nw",
    text="Kota",
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
    text="Ubah Data",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=37.0,
    y=8.0,
    width=102.0,
    height=37.0
)

canvas.create_text(
    625.0,
    124.0,
    anchor="nw",
    text="Autofill per User",
    fill="#ABABAB",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
