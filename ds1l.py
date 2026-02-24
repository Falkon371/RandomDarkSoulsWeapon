import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

daggers = [    "Bandit's Knife",
               "Dagger",
               "Dark Silver Tracer",
               "Ghost Blade",
               "Parrying Dagger",
               "Parrying Dagger"
               ]

axes = ["Battle Axe",
        "Butcher Knife",
        "Crescent Axe",
        "Gargoyle Tail Axe",
        "Golem Axe",
        "Hand Axe"
        ]

bows = ["Black Bow of Pharis",
"Composite Bow",
"Darkmoon Bow",
"Longbow",
"Short Bow"
]

gb = ["Dragonslayer Greatbow", "Gough's Greatbow"]

crossbow = ["Avelyn", "Heavy Crossbow",
            "Light Crossbow", "Sniper Crossbow"]


curved_greatsword = ["Gravelord Sword",
                     "Murakumo",
                     "Server"]

curved_sword = ["Falchion",
                "Gold Tracer",
                "Jagged Ghost Blade",
                "Painting Guardian Sword",
                "Quelaag's Furysword",
                "Scimitar",
                "Shotel"]

fist = ["Caestus",
        "Claw",
        "Dark Hand",
        "Dragon Bone Fist"
]

gh = ["Demon's Great Hammer",
      "Dragon Tooth",
      "Grant",
      "Great Club",
      "Large Club",
      "Smough's Hammer"]

ga = ["Black Knight Greataxe",
      "Demon's Greataxe",
      "Dragon King Greataxe",
      "Greataxe",
      "Stone Greataxe"]

gs = ["Abyss Greatsword",
    "Bastard Sword",
    "Black Knight Sword",
    "Claymore",
    "Crystal Greatsword",
    "Flamberge",
    "Great Lord Greatsword",
    "Greatsword of Artorias (Cursed)",
    "Greatsword of Artorias",
    "Man-serpent Greatsword",
    "Moonlight Greatsword",
    "Obsidian Greatsword",
    "Stone Greatsword"
]

halb = [
    "Black Knight Halberd",
    "Gargoyle's Halberd",
    "Giant's Halberd",
    "Great Scythe",
    "Halberd",
    "Lifehunt Scythe",
    "Lucerne",
    "Scythe",
    "Titanite Catch Pole"
]

hammers = [
    "Blacksmith Hammer",
    "Blacksmith Giant Hammer",
    "Club",
    "Hammer of Vamos",
    "Mace",
    "Morning Star",
    "Pickaxe",
    "Reinforced Club",
    "Warpick"
]

katanas = ["Chaos Blade", 
           "Iaito",
           "Uchigatana",
           "Washing Pole"]

spear = ["Channeler's Trident",
         "Demon's Spear",
"Dragonslayer Spear",
"Four-Pronged Plow",
"Moonlight Butterfly Horn",
"Partizan",
"Pike",
"Silver Knight Spear",
"Spear",
"Winged Spear",
]

sword = ["Astora's Straight Sword",
         "Balder Side Sword",
         "Barbed Straight Sword",
         "Broadsword",
         "Broken Straight Sword",
         "Crystal Straight Sword",
         "Darksword",
         "Drake Sword",
         "Longsword",
         "Shortsword",
         "Silver Knight Straight Sword",
         "Straight Sword Hilt",
         "Sunlight Straight Sword"
         ]

thSword = ["Estoc",
           "Mail Breaker",
           "Rapier",
           "Ricard's Rapier",
           "Velka's Rapier"]

ugs = ["Black Knight Greatsword",
       "Demon Great Machete",
       "Dragon Greatsword",
       "Greatsword",
       "Zweihander"]

whip = ["Guardian Tail",
        "Notched Whip",
        "Whip"]

catalysts = [
  "Beatrices Catalyst",
  "Demons Catalyst",
  "Izalith Catalyst",
  "Logans Catalyst",
  "Manus Catalyst",
  "Oolacile Catalyst",
  "Oolacile Ivory Catalyst",
  "Sorcerers Catalyst",
  "Tin Banishment Catalyst",
  "Tin Crystallization Catalyst",
  "Tin Darkmoon Catalyst "
]

talismans = [
  "Canvas Talisman",
  "Darkmoon Talisman",
  "Ivory Talisman",
  "Sunlight Talisman",
  "Talisman",
  "Thorolund Talisman",
  "Velkas Talisman"
]

flames = ["Pyromancy flame"]

alltables = [axes, bows, catalysts, crossbow, curved_greatsword, curved_sword,
              daggers, fist, flames, gb, gs, ga, gh, halb, hammers, katanas, 
              thSword, sword, spear, talismans, ugs, whip]



p = ""
ds1lista = []

count = 0
cr = 0
folder = resource_path('weapons_pngs/ds1Weapons')

p = f"{folder}/talisman"
for y in os.listdir(p):
    print(f"{y}")


for images in os.listdir(folder):
    cr = 0
    all = alltables[count]
    path = os.path.join(folder, images)
    for i in os.listdir(path):
        n = os.path.join(path, i)   
        a = all[cr]
        tab = [a, n]
        slow = {images: tab}
        cr += 1
        ds1lista.append(slow)

    count += 1


for x in ds1lista:
    print(x)


