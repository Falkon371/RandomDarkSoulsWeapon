import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



axes = [
"Bandit Axe",
"Battle Axe",
"Bound Hand Axe",
"Butchers Knife",
"Dragonslayers Crescent Axe",
"Gyrm Axe",
"Hand Axe",
"Infantry Axe"
]

bow = [
"Bell Keeper Bow",
"Bow of Want",
"Composite Bow",
"Dragonrider Bow",
"Hunters Blackbow",
"Long Bow",
"Sea Bow",
"Short Bow"
]

crossbow = [
"Avelyn",
"Heavy Crossbow",
"Light Crossbow",
"Sanctum Crossbow",
"Sanctum Repeating Crossbow",
"Shield Crossbow"
]

curved_greatswords = [
"Arced Sword",
"Curved Nil Greatsword",
"Dragon Greatsword",
"Murakumo"
]

curved_swords = [
"Eleum Loyce",
"Falchion",
"Manikin Sabre",
"Melu Scimitar",
"Monastery Scimitar",
"Red Rust Scimitar",
"Scimitar",
"Shotel",
"Spider Fang",
"Warped Sword"
]

dagger = [
"Bandits Knife",
"Black Flamestone Dagger",
"Blue Dagger",
"Broken Thief Sword",
"Dagger",
"Manikin Knife",
"Mythas Bent Blade",
"Parrying Dagger",
"Retainers Short Sword",
"Royal Dirk",
"Shadow Dagger",
"Thief Dagger",
"Umbral Dagger"
]

fist_claws = [
"Bone Fist",
"Caestus",
"Claw",
"Malformed Claws",
"Manikin Claws",
"Work Hook"
]

greatbows = [
"Alonne Greatbow",
"Dragonslayer Greatbow",
"Possessed Armor Greatbow",
"Twin Headed Greatbow"
]

greatsword = [
"Bastard Sword",
"Black Dragon Greatsword Icon",
"Black Knight Greatsword",
"Bluemoon Greatsword",
"Charred Loyce Greatsword",
"Claymore",
"Defender Greatsword",
"Drakeblood Greatsword",
"Drangleic Sword",
"Flamberge",
"Greatsword of the Forlorn",
"Key to the Embedded",
"Loyce Gs",
"Majestic Greatsword Icon",
"Mastodon Greatsword Ds2",
"Mirrah Greatsword",
"Moonlight Greatsword",
"Old Knight Greatsword",
"Old Mirrah Greatsword",
"Royal Greatsword",
"Rulers Sword",
"Thorned Greatsword",
"Watcher Greatsword"
]

great_axes = [
"Bandit Greataxe",
"Black Dragon Greataxe",
"Black Knight Greataxe",
"Crescent Axe",
"Drakekeepers Greataxe",
"Giant Stone Axe",
"Greataxe",
"Gyrm Greataxe",
"Lion Greataxe"
]

great_hammer = [
"Archdrake Mace",
"Demons Great Hammer",
"Dragon Tooth",
"Drakekeepers Great Hammer",
"Drakekeepers Warpick",
"Giant Warrior Club",
"Great Club",
"Gyrm Great Hammer",
"Iron King Hammer",
"Large Club",
"Malformed Shell",
"Malformed Skull",
"Old Knight Hammer",
"Pickaxe",
"Sacred Chime Hammer",
"Sanctum Mace",
"Smelter Hammer"
]

halberd = [
"Black Knight Halberd",
"Blue Knights Halberd",
"Dragonriders Halberd",
"Halberd",
"Helix Halberd",
"Lucerne",
"Mastodon Halberd",
"Old Knight Halberd",
"Old Knight Pike",
"Roaring Halberd",
"Santiers Spear",
"Scythe",
"Syans Halberd",
"Wrathful Axe"
]

hammers = [
"Aldia Hammer",
"Barbed Club",
"Black Dragon Warpick",
"Blacksmiths Hammer",
"Club",
"Craftsmans Hammer",
"Handmaids Ladle",
"Homunculus Mace",
"Mace",
"Mace of the Insolent",
"Morning Star",
"Reinforced Club"
]

katanas = [
"Berserker Blade",
"Bewitched Alonne Sword",
"Blacksteel Katana",
"Chaos Blade",
"Darkdrift",
"Manslayer",
"Uchigatana",
"Washing Pole"
]

lances = [
"Charriot Lance",
"Grand Lance",
"Heide Greatlance",
"Heide Lance",
"Rampart Golem Lance"
]

piercing_swords = [
"Black Scorpion Stinger",
"Chaos Rapier",
"Espada Ropera",
"Estoc",
"Ice Rapier",
"Mail Breaker",
"Rapier",
"Ricards Rapier",
"Spiders Silk"
]

reaper = [
"Bone Scythe",
"Crescent Sickle",
"Full Moon Sickle",
"Great Machete",
"Great Scythe",
"Scythe of the Forlorn",
"Scyther of Nahr Alma",
"Scythe of Want",
"Silverblack Sickle"
]

shortsword = [
"Ashen Warrior Sword",
"Black Dragon Sword",
"Blue Flame",
"Broadsword",
"Broken Straight Sword",
"Drakekeepers Sword",
"Foot Soldier Sword",
"Fume Sword",
"Heide Knight Sword",
"Ivory Straight Sword",
"Longsword",
"Possessed Armor Sword",
"Puzzling Stone Sword",
"Red Rust Sword",
"Shortsword",
"Sun Sword",
"Varangian Sword",
"Yellow Quartz Longsword"
]

spear = [
"Channelers Trident",
"Dragonslayer Spear",
"Gargoyle Bident",
"Heide Spear",
"Partizan",
"Pates Spear",
"Pike",
"Pilgrims Spontoon",
"Silverblack Spear",
"Spear",
"Spitfire Spear",
"Stone Soldier Spear",
"Winged Spear",
"Yorghs Spear"
]

twinblades = [
"Curved Twinblade",
"Dragonrider Twinblade",
"Red Iron Twinblade",
"Sorcerers Twinblade",
"Stone Twinblade",
"Twinblade"
]

ultra_greatsword = [
"Aged Smelter Sword",
"Black Knight Ultra Greatsword",
"Crypt Blacksword",
"Drakekeepers Ultra Greatsword",
"Drakewing Ultra Greatsword",
"Fume Ultra Greatsword",
"Greatsword",
"Ivory King Ultra Greatsword",
"Kings Ultra Greatsword",
"Lost Sinners Sword Lg",
"Old Knight Ultra Greatsword",
"Pursuers Ultra Greatsword",
"Smelter Sword",
"Zweihander"
]

whip = [
"Bloodied Whip",
"Notched Whip",
"Old Whip",
"Spotted Whip",
"Whip"
]

folder2 = resource_path('weapons_pngs/ds2Weapons')

sd = []

for x in os.listdir(folder2):
    path = f"{folder2}/{x}"
    for y in os.listdir(path):
        s = y.split('.')[0]
        
        slow = {x:s}
        sd.append(slow)

print(len(sd))

alltab = [axes, bow, crossbow, curved_greatswords,
          curved_swords, dagger, fist_claws, greatbows, greatsword, great_axes,
          great_hammer, halberd,
          hammers, katanas, lances, piercing_swords,
          reaper, shortsword, spear, twinblades, ultra_greatsword,
          whip]

bronie = []
count = 0
cr = 0
ds2lista = []

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
        ds2lista.append(slow)

    count += 1
    
for x in ds2lista:
    print(x)