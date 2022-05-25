# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import requests

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk
from gui_DataKum import DataKum
from gui_TambahData import TambahData
from gui_TampilDataPilihan import TampilDataPilihan
from gui_UbahData import UbahData
from gui_UbahPassword import UbahPass
from gui_UbahProfil import UbahProfil
from gui_tampilDataKum import tampilDataKum
from login import Login
from Homepage import Homepage
from register import Register
# from MainGUI import Homepage, Login, Register


OUTPUT_PATH = Path(__file__).parent
    

new_register = 0
pages = {
    "dataKum": DataKum,
    "tambahData": TambahData,
    "register": Register,
    "login": Login,
    "homepage": Homepage,
    "tampilDataKum": tampilDataKum,
    "tampilDataPilihan": TampilDataPilihan,
    "ubahData": UbahData,
    "ubahProfil": UbahProfil,
    "ubahPass": UbahPass
}

class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("login")
        self.title('Pendataan Kasus Covid-19 Indonesia')
        self.geometry("1000x600")
        self.configure(bg = "#FFFFFF")
    
    # Fungsi Ganti Page
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[frame_class]
        print(cls)
        new_frame = cls(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()