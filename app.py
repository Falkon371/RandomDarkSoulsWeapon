import tkinter as tk
from tkinter import PhotoImage
from ds1l import ds1lista
from ds3l import ds3lista
from ds2l import ds2lista
from bb import bblista
import random
from PIL import Image, ImageTk
import os
import sys

filtered_lista = ds1lista.copy()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def SwitchGames(ds, bronie):
    global filtered_lista
    global frame

    if(ds == "Dark Souls 1"):
        filtered_lista = ds1lista.copy()
    elif ds == "Dark Souls 2":
        filtered_lista = ds2lista.copy()
    elif ds == "Dark Souls 3":
        filtered_lista = ds3lista.copy()
    elif ds == "Bloodborne":
        filtered_lista = bblista.copy()

    if frame is not None:
        frame.destroy()

    frame = bronie(mainFrame, filtered_lista)
    frame.grid(row=0, column=0, sticky="nsew", padx=(0,10))


class ds1BronieFrame(tk.Frame):
    def __init__(self, container, lista):
        super().__init__(container,
    bg="#252526",
    bd=2,
    relief=tk.RIDGE)

        titleLabel.config(text="Dark Souls 1", bg= "#0f0f0f", fg="white")

        folder = resource_path('weapons_pngs/ds1Weapons')

        bronie = []
        for images in os.listdir(folder):
            bronie.append(images)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()
        var4 = tk.BooleanVar()
        var5 = tk.BooleanVar()
        var6 = tk.BooleanVar()
        var7 = tk.BooleanVar()
        var8 = tk.BooleanVar()
        var9 = tk.BooleanVar()
        var10 = tk.BooleanVar()
        var11 = tk.BooleanVar()
        var12 = tk.BooleanVar()
        var13 = tk.BooleanVar()
        var14 = tk.BooleanVar()
        var15 = tk.BooleanVar()
        var16 = tk.BooleanVar()
        var17 = tk.BooleanVar()
        var18 = tk.BooleanVar()
        var19 = tk.BooleanVar()
        var20 = tk.BooleanVar()
        var21 = tk.BooleanVar()
        var22 = tk.BooleanVar()

        def ChooseWeapon():
            global filtered_lista

            filtered_lista = []

            for item in lista:
                key = list(item.keys())[0]

                if key == bronie[0] and var1.get(): continue
                if key == bronie[1] and var2.get(): continue
                if key == bronie[2] and var3.get(): continue
                if key == bronie[3] and var4.get(): continue
                if key == bronie[4] and var5.get(): continue
                if key == bronie[5] and var6.get(): continue
                if key == bronie[6] and var7.get(): continue
                if key == bronie[7] and var8.get(): continue
                if key == bronie[8] and var9.get(): continue
                if key == bronie[9] and var10.get(): continue
                if key == bronie[10] and var11.get(): continue
                if key == bronie[11] and var12.get(): continue
                if key == bronie[12] and var13.get(): continue
                if key == bronie[13] and var14.get(): continue
                if key == bronie[14] and var15.get(): continue
                if key == bronie[15] and var16.get(): continue
                if key == bronie[16] and var17.get(): continue
                if key == bronie[17] and var18.get(): continue
                if key == bronie[18] and var19.get(): continue
                if key == bronie[19] and var20.get(): continue
                if key == bronie[20] and var21.get(): continue
                if key == bronie[21] and var22.get(): continue

                filtered_lista.append(item)

            print("Aktualna pula:", len(filtered_lista))

        tk.Label(self, text="Wyjmij rodzaj broni z puli losowań", bg="#252526", fg="white").grid(row=0, column=0, columnspan=2)
        tk.Checkbutton(self, text="Axes", variable=var1, bg="#252526", fg="white",  selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self, text="Bow", variable=var2, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self, text="Catalyst", variable=var3, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self, text="Crossbow", variable=var4, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Greatsword", variable=var5, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=5, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Sword", variable=var6, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=6, column=0, sticky="w")
        tk.Checkbutton(self, text="Dagger", variable=var7, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=7, column=0, sticky="w")
        tk.Checkbutton(self, text="Fist", variable=var8, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=8, column=0, sticky="w")
        tk.Checkbutton(self, text="Flames", variable=var9, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=9, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Bow", variable=var10, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=10, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Sword", variable=var11, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=11, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Axe", variable=var12, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=12, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Hammer", variable=var13, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=13, column=0, sticky="w")
        tk.Checkbutton(self, text="Halberd", variable=var14, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(self, text="Hammer", variable=var15, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=2, column=1, sticky="w")
        tk.Checkbutton(self, text="Katana", variable=var16, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self, text="Thrusting Sword", variable=var17, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=4, column=1, sticky="w")
        tk.Checkbutton(self, text="Short sword", variable=var18, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=5, column=1, sticky="w")
        tk.Checkbutton(self, text="Spear", variable=var19, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=6, column=1, sticky="w")
        tk.Checkbutton(self, text="Talisman", variable=var20, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=7, column=1, sticky="w")
        tk.Checkbutton(self, text="Ultra Greatsword", variable=var21, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=8, column=1, sticky="w")
        tk.Checkbutton(self, text="Whip", variable=var22, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white", command=ChooseWeapon).grid(row=9, column=1, sticky="w")





class ds2BronieFrame(tk.Frame):
    def __init__(self, container, lista):
        super().__init__(container,
    bg="#252526",
    bd=2,
    relief=tk.RIDGE)

        titleLabel.config(text="Dark Souls 2", bg= "#0f0f0f", fg="white")
        folder = resource_path('weapons_pngs/ds2Weapons')

        bronie = []
        for images in os.listdir(folder):
            bronie.append(images)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()
        var4 = tk.BooleanVar()
        var5 = tk.BooleanVar()
        var6 = tk.BooleanVar()
        var7 = tk.BooleanVar()
        var8 = tk.BooleanVar()
        var9 = tk.BooleanVar()
        var10 = tk.BooleanVar()
        var11 = tk.BooleanVar()
        var12 = tk.BooleanVar()
        var13 = tk.BooleanVar()
        var14 = tk.BooleanVar()
        var15 = tk.BooleanVar()
        var16 = tk.BooleanVar()
        var17 = tk.BooleanVar()
        var18 = tk.BooleanVar()
        var19 = tk.BooleanVar()
        var20 = tk.BooleanVar()
        var21 = tk.BooleanVar()
        var22 = tk.BooleanVar()
        var23 = tk.BooleanVar()
        var24 = tk.BooleanVar()
        var25 = tk.BooleanVar()

        def ChooseWeapon():
            global filtered_lista

            filtered_lista = []

            for item in lista:
                key = list(item.keys())[0]

                if key == bronie[0] and var1.get(): continue
                if key == bronie[1] and var2.get(): continue
                if key == bronie[2] and var3.get(): continue
                if key == bronie[3] and var4.get(): continue
                if key == bronie[4] and var5.get(): continue
                if key == bronie[5] and var6.get(): continue
                if key == bronie[6] and var7.get(): continue
                if key == bronie[7] and var8.get(): continue
                if key == bronie[8] and var9.get(): continue
                if key == bronie[9] and var10.get(): continue
                if key == bronie[10] and var11.get(): continue
                if key == bronie[11] and var12.get(): continue
                if key == bronie[12] and var13.get(): continue
                if key == bronie[13] and var14.get(): continue
                if key == bronie[14] and var15.get(): continue
                if key == bronie[15] and var16.get(): continue
                if key == bronie[16] and var17.get(): continue
                if key == bronie[17] and var18.get(): continue
                if key == bronie[18] and var19.get(): continue
                if key == bronie[19] and var20.get(): continue  
                if key == bronie[20] and var21.get(): continue  
                if key == bronie[21] and var22.get(): continue  
                if key == bronie[22] and var23.get(): continue  
                if key == bronie[23] and var24.get(): continue  
                if key == bronie[24] and var25.get(): continue  

                filtered_lista.append(item)

            print("Aktualna pula:", len(filtered_lista))

        tk.Label(self, text="Wyjmij rodzaj broni z puli losowań", bg="#252526", fg="white").grid(row=0, column=0, columnspan=2)
        tk.Checkbutton(self, text="Axes", variable=var1, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self, text="Bow", variable=var2, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self, text="Staves", variable=var3, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self, text="Crossbow", variable=var4, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Greatsword", variable=var5, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=5, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Sword", variable=var6, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=6, column=0, sticky="w")
        tk.Checkbutton(self, text="Dagger", variable=var7, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=7, column=0, sticky="w")
        tk.Checkbutton(self, text="Fist", variable=var8, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=8, column=0, sticky="w")
        tk.Checkbutton(self, text="Flames", variable=var9, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=9, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Bow", variable=var10, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=10, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Sword", variable=var11, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=11, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Axe", variable=var12, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=12, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Hammer", variable=var13, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=13, column=0, sticky="w")
        tk.Checkbutton(self, text="Halberd", variable=var14, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(self, text="Hammer", variable=var15, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=2, column=1, sticky="w")
        tk.Checkbutton(self, text="Katana", variable=var16, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self, text="Lances", variable=var17, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=4, column=1, sticky="w")
        tk.Checkbutton(self, text="Thrusting Sword", variable=var18, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=5, column=1, sticky="w")
        tk.Checkbutton(self, text="Reapers", variable=var19, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=6, column=1, sticky="w")
        tk.Checkbutton(self, text="Short sword", variable=var20, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=7, column=1, sticky="w")
        tk.Checkbutton(self, text="Spear", variable=var21, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=8, column=1, sticky="w")
        tk.Checkbutton(self, text="Talisman", variable=var22, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=9, column=1, sticky="w")
        tk.Checkbutton(self, text="Twinblades", variable=var23, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=10, column=1, sticky="w")
        tk.Checkbutton(self, text="Ultra Greatsword", variable=var24, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=11, column=1, sticky="w")
        tk.Checkbutton(self, text="Whip", variable=var25, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=12, column=1, sticky="w")


class ds3BronieFrame(tk.Frame):
    def __init__(self, container, lista):
        super().__init__(container,
    bg="#252526",
    bd=2,
    relief=tk.RIDGE)

        titleLabel.config(text="Dark Souls 3", bg= "#0f0f0f", fg="white")
        folder = resource_path('weapons_pngs/ds3Weapons')

        bronie = []
        for images in os.listdir(folder):
            bronie.append(images)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()
        var4 = tk.BooleanVar()
        var5 = tk.BooleanVar()
        var6 = tk.BooleanVar()
        var7 = tk.BooleanVar()
        var8 = tk.BooleanVar()
        var9 = tk.BooleanVar()
        var10 = tk.BooleanVar()
        var11 = tk.BooleanVar()
        var12 = tk.BooleanVar()
        var13 = tk.BooleanVar()
        var14 = tk.BooleanVar()
        var15 = tk.BooleanVar()
        var16 = tk.BooleanVar()
        var17 = tk.BooleanVar()
        var18 = tk.BooleanVar()
        var19 = tk.BooleanVar()
        var20 = tk.BooleanVar()
        var21 = tk.BooleanVar()
        var22 = tk.BooleanVar()
        var23 = tk.BooleanVar()
        var24 = tk.BooleanVar()

        def ChooseWeapon():
            global filtered_lista

            filtered_lista = []

            for item in lista:
                key = list(item.keys())[0]

                if key == bronie[0] and var1.get(): continue
                if key == bronie[1] and var2.get(): continue
                if key == bronie[2] and var3.get(): continue
                if key == bronie[3] and var4.get(): continue
                if key == bronie[4] and var5.get(): continue
                if key == bronie[5] and var6.get(): continue
                if key == bronie[6] and var7.get(): continue
                if key == bronie[7] and var8.get(): continue
                if key == bronie[8] and var9.get(): continue
                if key == bronie[9] and var10.get(): continue
                if key == bronie[10] and var11.get(): continue
                if key == bronie[11] and var12.get(): continue
                if key == bronie[12] and var13.get(): continue
                if key == bronie[13] and var14.get(): continue
                if key == bronie[14] and var15.get(): continue
                if key == bronie[15] and var16.get(): continue
                if key == bronie[16] and var17.get(): continue
                if key == bronie[17] and var18.get(): continue
                if key == bronie[18] and var19.get(): continue
                if key == bronie[19] and var20.get(): continue  
                if key == bronie[20] and var21.get(): continue
                if key == bronie[21] and var22.get(): continue
                if key == bronie[22] and var23.get(): continue
                if key == bronie[23] and var24.get(): continue  

                filtered_lista.append(item)

            print("Aktualna pula:", len(filtered_lista))

        tk.Label(self, text="Wyjmij rodzaj broni z puli losowań", bg="#252526", fg="white").grid(row=0, column=0, columnspan=2)
        tk.Checkbutton(self, text="Axes", variable=var1, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self, text="Bow", variable=var2, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self, text="Chimes", variable=var3, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self, text="Crossbow", variable=var4, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Greatsword", variable=var5, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=5, column=0, sticky="w")
        tk.Checkbutton(self, text="Curved Sword", variable=var6, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=6, column=0, sticky="w")
        tk.Checkbutton(self, text="Dagger", variable=var7, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=7, column=0, sticky="w")
        tk.Checkbutton(self, text="Fist", variable=var8, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=8, column=0, sticky="w")
        tk.Checkbutton(self, text="Flames", variable=var9, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=9, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Bow", variable=var10, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=10, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Sword", variable=var11, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=11, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Axe", variable=var12, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=12, column=0, sticky="w")
        tk.Checkbutton(self, text="Great Hammer", variable=var13, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=13, column=0, sticky="w")
        tk.Checkbutton(self, text="Halberd", variable=var14, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(self, text="Hammer", variable=var15, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=2, column=1, sticky="w")
        tk.Checkbutton(self, text="Katana", variable=var16, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self, text="Thrusting Sword", variable=var17, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=4, column=1, sticky="w")
        tk.Checkbutton(self, text="Reapers", variable=var18, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=5, column=1, sticky="w")
        tk.Checkbutton(self, text="Short sword", variable=var19, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=6, column=1, sticky="w")
        tk.Checkbutton(self, text="Spear", variable=var20, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=7, column=1, sticky="w")
        tk.Checkbutton(self, text="Staves", variable=var21, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=8, column=1, sticky="w")
        tk.Checkbutton(self, text="Talisman", variable=var22, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=9, column=1, sticky="w")
        tk.Checkbutton(self, text="Ultra Greatsword", variable=var23, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=10, column=1, sticky="w")
        tk.Checkbutton(self, text="Whip", variable=var24, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=11, column=1, sticky="w")


class bbBronieFrame(tk.Frame):
    def __init__(self, container, lista):
        super().__init__(container,
    bg="#252526",
    bd=2,
    relief=tk.RIDGE)

        titleLabel.config(text="Bloodborne", bg= "#0f0f0f", fg="white")
        folder = resource_path('weapons_pngs/bbWeapons')

        bronie = []
        for images in os.listdir(folder):
            bronie.append(images)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()


        def ChooseWeapon():
            global filtered_lista

            filtered_lista = []

            for item in lista:
                key = list(item.keys())[0]

                if key == bronie[0] and var1.get(): continue
                if key == bronie[1] and var2.get(): continue
                if key == bronie[2] and var3.get(): continue


                filtered_lista.append(item)

            print("Aktualna pula:", len(filtered_lista))

        tk.Label(self, text="Wyjmij rodzaj broni z puli losowań", bg="#252526", fg="white").grid(row=0, column=0, columnspan=2)
        tk.Checkbutton(self, text="Firearms", variable=var1, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self, text="Hunter Tools", variable=var2, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self, text="Trick Weapons", variable=var3, bg="#252526", fg="white", selectcolor="#252526", activebackground="#252526", activeforeground="white",command=ChooseWeapon).grid(row=3, column=0, sticky="w")



def RandomWeap():
    source = filtered_lista 

    if not source:
        return "Brak broni", ""

    staraLista = random.choice(source)
    a = staraLista.keys()
    nowaLista = list(a)
    key = nowaLista[0]
    print(staraLista[key])
    randWeapon = staraLista[key]
    print(f"Wylosowana broń: {randWeapon}")
    return randWeapon[0], randWeapon[1]

rand, weap = RandomWeap()

p = resource_path("weapons_pngs/nosw.png")
def update_label():
    rand, weap = RandomWeap()

    if not rand or not weap:
        label.config(text="Brak broni w puli!")
        i = Image.open(p)
        im = ImageTk.PhotoImage(i)
        image_label.config(image=im, width=100, height=100)
        image_label.photo = im
        return

    imag = Image.open(weap)
    img = ImageTk.PhotoImage(imag)
    image_label.config(image=img)
    label.config(text=rand)
    image_label.photo = img


root = tk.Tk()
root.title("Dark Souls Random Weapon Picker")
root.geometry('480x460')
root.configure(bg = "#0f0f0f")
root.resizable(False, False)

titleLabel = tk.Label(root, text="Dark Souls 1", bg= "#0f0f0f", fg="white", width=25)
titleLabel.grid(row=0, column=0)

titleLabel.config(font=("Arial", 25))

darkSoulFrame = tk.Frame(root, bg="#0f0f0f", height=70)
darkSoulFrame.grid(row=1, column=0, sticky="ew")
darkSoulFrame.grid_columnconfigure((0,1,2,3), weight=1)

mainFrame = tk.Frame(root, bg="#1e1e1e")
mainFrame.grid(row=2, column=0, sticky="nsew", padx=15, pady=15)

mainFrame.grid_columnconfigure(0, weight=1)  
mainFrame.grid_columnconfigure(1, weight=1)  
mainFrame.grid_rowconfigure(0, weight=1)


frame = ds1BronieFrame(mainFrame, ds1lista)
frame.grid(row=0, column=0, sticky="nsew", padx=(0,10))

showFrame = tk.Frame(mainFrame, bg="#252526", bd=2, relief=tk.RIDGE)
showFrame.grid(row=0, column=1, sticky="nsew")

showFrame.grid_rowconfigure(0, weight=1)
showFrame.grid_columnconfigure(0, weight=1)

darkSoulButton = tk.Button(darkSoulFrame, text="Dark Souls 1", width=12, command=lambda: SwitchGames("Dark Souls 1", ds1BronieFrame))
darkSoulButton.grid(row=0, column= 0, padx = 2, pady = 1)

darkSoulButton2 = tk.Button(darkSoulFrame, text="Dark Souls 2", width=12, command=lambda: SwitchGames("Dark Souls 2", ds2BronieFrame))
darkSoulButton2.grid(row=0, column= 1, padx = 2, pady = 1)

darkSoulButton3 = tk.Button(darkSoulFrame, text="Dark Souls 3", width=12, command=lambda: SwitchGames("Dark Souls 3", ds3BronieFrame))
darkSoulButton3.grid(row=0, column= 2, padx = 2, pady = 1)

bloodborneButton = tk.Button(darkSoulFrame, text="Bloodborne", width=12, command=lambda: SwitchGames("Bloodborne", bbBronieFrame))
bloodborneButton.grid(row=0, column= 3, padx = 2, pady = 1)


newList = []
nazwa = ""

image_label = tk.Label(showFrame, width=100, height=100)
image_label.grid(row=0, column= 0, columnspan = 2, rowspan = 4, padx = 5, pady = 5)

imag = Image.open(weap)
img = ImageTk.PhotoImage(imag)
image_label.config(image=img)
image_label.photo = img


label = tk.Label(showFrame, bg="#252526", fg = "white", text=rand, width=25)
label.grid(row=4, column= 0, sticky=tk.W)

button = tk.Button(showFrame, text="Losuj", width=25, command=update_label)
button.grid(row=5, column= 0, sticky=tk.W)


root.mainloop()

