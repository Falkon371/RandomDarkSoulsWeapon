import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


folder2 = resource_path('weapons_pngs/ds3Weapons')

daggers = [
    "Aquamarine Dagger",
    "Bandit's Knife",
    "Brigand Twindaggers",
    "Corvian Greatknife",
    "Dagger",
    "Handmaid's Dagger",
    "Harpe",
    "Mail Breaker",
    "Murky Hand Scythe",
    "Parrying Dagger",
    "Rotten Ghru Dagger",
    "Scholar's Candlestick",
    "Tailbone Short Sword"
]


straight_swords = [
    "Anri's Straight Sword",
    "Astora Straight Sword",
    "Barbed Straight Sword",
    "Broadsword",
    "Broken Straight Sword",
    "Cleric's Candlestick",
    "Dark Sword",
    "Gotthard Twinswords",
    "Irithyll Straight Sword",
    "Long Sword",
    "Lothric Knight Sword",
    "Lothric Straight Sword",
    "Morion Blade",
    "Ringed Knight Straight Sword",
    "Shortsword",
    "Sunlight Straight Sword",
    "Valorheart"
]

greatswords = [
    "Bastard Sword",
    "Black Knight Sword",
    "Claymore",
    "Drakeblood Greatsword",
    "Executioner's Greatsword",
    "Firelink Greatsword",
    "Flamberge",
    "Gael's Greatsword",
    "Greatsword of Judgement",
    "Hollowslayer Greatsword",
    "Moonlight Greatsword",
    "Onyx Blade",
    "Storm Ruler",
    "Twin Princess Greatsword",
    "Wolf Knight's Greatsword",
    "Wolnir's Holy Greatsword"
]

ultra_greatswords = [
    "Astora Greatsword",
    "Black Knight Greatsword",
    "Cathedral Knight Greatsword",
    "Farron Greatsword",
    "Fume Ultra Greatsword",
    "Greatsword",
    "Lorian's Greatsword",
    "Lothric Knight Greatsword",
    "Profaned Greatsword",
    "Ringed Knight Paired Greatswords",
    "Zweihander"
]

axes = [
    "Battle Axe",
    "Brigand Axe",
    "Butcher Knife",
    "Dragonslayer's Axe",
    "Eleonora",
    "Hand Axe",
    "Man Serpent Hatchet",
    "Millwood Battle Axe",
    "Thrall Axe",
    "Winged Knight Twinaxes"
]

greataxes = [
    "Black Knight Greataxe",
    "Demon's Greataxe",
    "Dragonslayer Greataxe",
    "Earth Seeker",
    "Great Machete",
    "Greataxe",
    "Yhorm's Great Machete"
]

hammers = [
    "Blacksmith Hammer",
    "Club",
    "Drang Hammers",
    "Heysel Pick",
    "Mace",
    "Morning Star",
    "Reinforced Club",
    "Warpick"
]

great_hammers = [
    "Dragon Tooth",
    "Gargoyle Flame Hammer",
    "Great Club",
    "Great Mace",
    "Great Wooden Hammer",
    "Large Club",
    "Ledo's Great Hammer",
    "Morne's Great Hammer",
    "Old King's Great Hammer",
    "Pickaxe",
    "Quakestone Hammer",
    "Smough's Great Hammer",
    "Spiked Mace",
    "Vordt's Great Hammer"
]

katanas = [
    "Bloodlust",
    "Black Blade",
    "Chaos Blade",
    "Darkdrift",
    "Frayed Blade",
    "Onikiri and Ubadachi",
    "Uchigatana",
    "Washing Pole"
]

curved_swords = [
    "Carthus Curved Sword",
    "Carthus Shotel",
    "Pontiff Knight Curved Sword",
    "Crescent Moon Sword",
    "Dancer's Enchanted Swords",
    "Demon's Scar",
    "Falchion",
    "Follower Sabre",
    "Painting Guardian's Curved Sword",
    "Rotten Ghru Curved Sword",
    "Scimitar",
    "Sellsword Twinblades",
    "Shotel",
    "Storm Curved Sword",
    "Warden Twinblades"
]

curved_greatswords = [
    "Carthus Curved Greatsword",
    "Exile Greatsword",
    "Harald Curved Greatsword",
    "Murakumo",
    "Old Wolf Curved Sword"
]

spears = [
    "Arstor's Spear",
    "Dragonslayer Spear",
    "Dragonslayer Swordspear",
    "Drang Twinspears",
    "Follower Javelin",
    "Four-Pronged Plow",
    "Gargoyle Flame Spear",
    "Golden Ritual Spear",
    "Greatlance",
    "Lothric Knight Long Spear",
    "Lothric War Banner",
    "Partizan",
    "Pike",
    "Ringed Knight Spear",
    "Rotten Ghru Spear",
    "Saint Bident",
    "Soldering Iron",
    "Spear",
    "Tailbone Spear",
    "Winged Spear",
    "Yorshka's Spear"
]

halberds = [
    "Black Knight Glaive",
    "Crescent Axe",
    "Crucifix of the Mad King",
    "Glaive",
    "Gundyr's Halberd",
    "Halberd",
    "Immolation Tinder",
    "Lucerne",
    "Red Hilted Halberd",
    "Splitleaf Greatsword",
    "Winged Knight Halberd"
]

whips = [
    "Notched Whip",
    "Rose of Ariandel",
    "Spotted Whip",
    "Whip",
    "Witch's Locks"
]

bows = [
    "Black Bow of Pharis",
    "Composite Bow",
    "Darkmoon Longbow",
    "Dragonrider Bow",
    "Longbow",
    "Short Bow",
    "White Birch Bow"
]

greatbows = [
    "Dragonslayer Greatbow",
    "Millwood Greatbow",
    "Onislayer Greatbow"
]

crossbows = [
    "Arbalest",
    "Avelyn",
    "Repeating Crossbow",
    "Heavy Crossbow",
    "Knight's Crossbow",
    "Light Crossbow",
    "Sniper Crossbow"
]


piercingSword = [
    "Crow Quills",
    "Crystal Sage's Rapier",
    "Estoc",
    "Irithyll Rapier",
    "Rapier",
    "Ricard's Rapier"
]

reaper = [
    "Friede's Great Scythe",
    "Great Corvian Scythe",
    "Great Scythe",
    "Pontiff Knight Great Scythe"
]

fist = [
    "Caestus",
    "Claw",
    "Crow Talons",
    "Dark Hand",
    "Demon's Fist",
    "Manikin Claws"
]

chimes = [
  "Caithas Chime",
  "Clerics Sacred Chime",
  "Crystal Chime",
  "Priests Chime",
  "Sacred Chime Of Filianore",
  "Saint-Tree Bellvine",
  "Yorshkas Chime"
]

staves = [
  "Archdeacon Great Staff",
  "Court Sorcerers Staff",
  "Heretics Staff",
  "Izalith Staff",
  "Man-grubs Staff",
  "Medicants Staff",
  "Murky Longstaff",
  "Preacher's Right Arm",
  "Sages Crystal Staff",
  "Sorcerers Staff",
  "Storytellers Staff",
  "Witchtree Branch"
]

talismans = [
  "Canvas Talisman",
  "Saints Talisman",
  "Sunless Talisman",
  "Sunlight Talisman",
  "Talisman",
  "White Hair Talisman"
]

flames = ["Demon's Scar", "Pyromancer's Parting Flame", "Pyromancy Flame"]

alltab = [axes, bows, chimes, crossbows, curved_greatswords, curved_swords,
        daggers, fist, flames, greatbows, greatswords, greataxes, great_hammers, halberds,
        hammers, katanas, piercingSword, reaper, straight_swords,
        spears, staves, talismans, ultra_greatswords, whips]



p = ""
ds3lista = []

count = 0
cr = 0

bronie = []

p = f"{folder2}/talisman"
for y in os.listdir(p):
    print(f"{y}")

for images in os.listdir(folder2):
    cr = 0
    all = alltab[count]
    path = os.path.join(folder2, images)
    for i in os.listdir(path):
        n = os.path.join(path, i)   
        a = all[cr]
        tab = [a, n]
        slow = {images: tab}
        cr += 1
        ds3lista.append(slow)

    count += 1


for x in ds3lista:
    print(x)

pt = f'weapons_pngs/ds2Weapons'

for x in bronie:
    print(f"X: {x}")
