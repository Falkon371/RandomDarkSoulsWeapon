import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

firearms = [
  "Cannon",
  "Church Cannon",
  "Evelyn",
  "Fist Of Gratia",
  "Flamesprayer",
  "Gatling Gun",
  "Hunter Blunderbuss",
  "Hunter Pistol",
  "Loch Shield",
  "Ludwigs Rifle",
  "Piercing Rifle",
  "Repeating Pistol",
  "Rosmarinus",
  "Hunter's Torch",
  "Torch",
  "Wooden Shield"
]

trick_weapons = [
  "Amygdalans Arm",
  "Beasthunter Saif",
  "Beast Claw",
  "Beast Cutter",
  "Blade Of Mercy",
  "Bloodletter",
  "Boom Hammer",
  "Burial Blade",
  "Chikage",
  "Church Pick",
  "Holy Moonlight Sword",
  "Hunter Axe",
  "Kirkhammer",
  "Kos Parasite",
  "Logarius Wheel",
  "Ludwigs Holy Blade",
  "Rakuyo",
  "Reiterpallasch",
  "Rifle Spear",
  "Saw Cleaver",
  "Saw Spear",
  "Simons Bowblade",
  "Stake Driver",
  "Threaded Cane",
  "Tonitrus",
  "Whirligig Saw"
]

hunter_tools = [
  "Accursed Brew",
  "Augur Of Ebrietas",
  "A Call Beyond",
  "Beast Roar",
  "Blacksky Eye",
  "Choir Bell",
  "Empty Phantasm Shell",
  "Executioner Gloves",
  "Madaras Whistle",
  "Messenger Gift",
  "Old Hunter Bone",
  "Tiny Tonitrus"
]

alltables = [firearms, hunter_tools, trick_weapons]


folder = resource_path("weapons_pngs/bbWeapons")

p = ""
bblista = []

count = 0
cr = 0

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
        bblista.append(slow)

    count += 1



