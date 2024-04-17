# Treasure Generation Script
# Parameters: Hoard Tier
ht = 2

# Import
import random

# List
gemstone10gp = ["Azurite", "Banded Agate", "Blue Quartz", "Eye Agate", "Fire Agate", "Lapis Lazuli", "Moss Agate", "Obsidian", "Tiger Eye", "Turquoise"]
gemstone25gp = ["Andar", "Skydrop", "Sunstone", "Tchazer"]
gemstone50gp = ["Bloodstone", "Citrine", "Jasper", "Moonstone", "Onyx"]
gemstone100gp = ["Amber", "Amethyst", "Garnet", "Jade", "Jet", "Pearl", "Spinel", "Tourmaline"]
gemstone500gp = ["Alexandrite", "Aquamatrine", "Black Pearl", "Blue Spinel", "Peridot", "Topaz"]
gemstone1000gp = ["Black Opal", "Blue Sapphire", "Emerald", "Fire Opal", "Opal", "Star Ruby", "Star Sapphire", "Yellow Sapphire"]
gemstone5000gp = ["Black Sapphire", "Diamond", "Jacinith", "Ruby"]
artobjectjewlerylist = ["Badge/Brooch/Hairpin", "Earrings", "Armlet/Bangle", "Ring", "Ring", "Anklet/Bracelet/Bracer", "Amulet/Necklace/Pendant", "Circlet/Crown/Mask/Tiara"]
artobjectotherlist = ["Goblet", "Scepter", "Statuette"]
aomaterial = ["Darkwood", "Dragonbone", "Ivory", "Silver", "Electrum", "Gold", "Rose Gold", "White Gold", "Mithral", "Platinum"]
aoquality = ["Fine", "Elegant", "Opulent", "Glamourous", "Exquisite"]

# Functions
def get_gemstone(gold, gv):
	if gv == 10 and gold > 15000: gemvalue = 5000
	elif gv > 7 and gold > 10000: gemvalue = 1000
	elif gv == 10 and gold > 3000: gemvalue = 1000
	elif gv > 6 and gold > 5000: gemvalue = 500
	elif gv == 10 and gold > 1500: gemvalue = 500
	elif gv > 5 and gold > 1000: gemvalue = 100
	elif gv == 10 and gold > 300: gemvalue = 100
	elif gv > 4 and gold > 250: gemvalue = 50
	elif gv > 3 and gold > 100: gemvalue = 25
	elif gold > 25: gemvalue = 10
	else: gemvalue = 0
	return(gemvalue)

def get_artobject(gold):
	# objecttype = random.randint(1, 3)
	av = 0
	objectcatagory = 1
	# Jewelery
	if objectcatagory == 1:
		objecttype = random.randint(1, 8) -1
		objectmat = random.randint(1, 10) -1
		objectquality = (random.randint(1, 6) + random.randint(1, 6))
		inlay = random.randint(1, 6)
		inlaymat = random.randint(1, 10) -1
		socket = random.randint(1, 6)
		socketstone = (random.randint(1, 6) + random.randint(1, 6)) -2
		av = (objecttype + 2 + objectquality) * 5
		
		if objectquality == 8: av = av * 2
		elif objectquality == 9: av = av * 3
		elif objectquality == 10: av = av * 4
		elif objectquality == 11: av = av * 5
		elif objectquality == 12: av = av * 6
		objectquality -= 8
		
		if objectmat == 4: av = av * 5 #Electrum
		elif objectmat == 5: av = av * 10 #Gold
		elif objectmat == 6: av = av * 15 #Rose Gold
		elif objectmat == 7: av = av * 20 #White Gold
		elif objectmat == 8: av = av * 50 #Mithral
		elif objectmat == 9: av = av * 100 #Platinum
		
		if objectquality > -1: objectdesc = "Art Object: " + aoquality[objectquality] + " " + aomaterial[objectmat] + " " + artobjectjewlerylist[objecttype]
		else: objectdesc = "Art Object: " + aomaterial [objectmat] + " " + artobjectjewlerylist[objecttype]
		
		if inlay == 1 and inlaymat > objectmat:
			if inlaymat < 3: #Silver
				inlaymat = 3
				av += 10
			elif inlaymat == 4: av += 50 #Electrum
			elif inlaymat < 7: av += 100 #Gold or Rose Gold
			elif inlaymat == 7: av += 200 #White Gold
			elif inlaymat == 8: av += 500 #Mithral
			elif inlaymat == 9: av += 1000 #Platinum
			objectdesc +=" inlaid with " + aomaterial[inlaymat]
		elif inlay == 1:
			if objectmat < 5 or objectquality < 0: inlaymat = random.randint(1, 4) + random.randint(1, 4) - 3
			else: inlaymat = random.randint(1, 4) + random.randint(1, 4) - 1
			if inlaymat < 2:
				x = random.randint(1, len(gemstone10gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone10gp[x]
				av += 25
			elif inlaymat == 2:
				x = random.randint(1, len(gemstone25gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone25gp[x]
				av += 50
			elif inlaymat == 3:
				x = random.randint(1, len(gemstone50gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone50gp[x]
				av += 100
			elif inlaymat == 4:
				x = random.randint(1, len(gemstone100gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone100gp[x]
				av += 200
			elif inlaymat == 5:
				x = random.randint(1, len(gemstone500gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone500gp[x]
				av += 1000
			elif inlaymat == 6:
				x = random.randint(1, len(gemstone1000gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone1000gp[x]
				av += 2000
			else:
				x = random.randint(1, len(gemstone5000gp)) - 1
				objectdesc +=" inlaid with crushed " + gemstone5000gp[x]
				av += 10000
		#if socket == 1:
		#	if objectmat > 7 and socketstone < 2: socketstone = 2 #Mithral & Platnium have higher value gems
		#	nos = random.randint(1, 100) - 50 #nos: Number of Stones
		#	if nos < 0: 
				
			
	# Objects
	# Clothes
	
	if av < (gold / 2):
		print(objectdesc, "(", av, "gp)")
	else: av = 0
	return (av)	
	

def get_consumables(h):
	itempower = 0
	for i in range(h): itempower += random.randint(1, 4)
	while itempower > 0:
		# Magic Item Rarity Roll
		if h == 1:
			r = random.randint(1, 4)
		elif h == 2:
			r = random.randint(1, 6)
		elif h == 3:
			r = random.randint(1, 8)
		else: r = random.randint(1, 10)
		# Determine Magic Item Rarity
		if r == 10 and itempower > 8:
			rarity = "Legendary"
			itempower -= 9
		elif r > 7 and itempower > 5:
			rarity = "Very Rare"
			itempower -= 6
		elif r > 5 and itempower > 3:
			rarity = "Rare"
			itempower -= 4
		elif r > 2 and itempower > 2:
			rarity = "Uncommon"
			itempower -= 2
		else:
			rarity = "Common"
			itempower -= 1
		# Determine Magic Item Type
		r = random.randint(1, 4) + random.randint(1, 4)
		if r == 2: itemtype = "Magic Dust, Deck of Cards"
		elif r == 3: itemtype = "Gems (Mind Crystal, Elemental Gemstone, etc)"
		elif r == 4: itemtype = "Ammunition (Arrows, Bolts, Bullets) x2d6"
		elif r == 5: itemtype = "Healing Potion"
		elif r == 6: itemtype = "Potion and Oils"
		elif r == 7: itemtype = "Scroll"
		else: itemtype = "Scroll or Spellwrought Tattoo"
		# Print Magic Item
		print("Magic Item:", rarity, itemtype)

def get_magicitems(h):
	itempower = 0
	for i in range(h): itempower += random.randint(1, 4)
	# print("Itempower:", itempower)
	while itempower > 0:
		# Magic Item Rarity Roll
		if h == 1:
			r = random.randint(1, 4)
		elif h == 2:
			r = random.randint(1, 6)
		elif h == 3:
			r = random.randint(1, 8)
		else: r = random.randint(1, 10)
		# Determine Magic Item Rarity
		if r == 10 and itempower > 8:
			rarity = "Legendary"
			itempower -= 9
		elif r > 7 and itempower > 5:
			rarity = "Very Rare"
			itempower -= 6
		elif r > 5 and itempower > 3:
			rarity = "Rare"
			itempower -= 4
		elif r > 2 and itempower > 2:
			rarity = "Uncommon"
			itempower -= 2
		else:
			rarity = "Common"
			itempower -= 1
		# Determine Magic Item Type
		r = random.randint(1, 6) + random.randint(1, 6)
		if r == 2: itemtype = "1 in 4: Cursed Item, Else: Wondrous Item (Bags, Utility Items, Spell Books, Stones)"
		elif r == 3: itemtype = "Wondrous Item (Bags, Utility Items, Spell Books, Stones)"
		elif r == 4: itemtype = "Ring"
		elif r == 5: itemtype = "Wondrous Item (Helms, Amulets, Cloaks, Ioun Stones, etc.)"
		elif r == 6: itemtype = "Spell Focus (Rod, Staff, Wand)"
		elif r == 7: itemtype = "Martial Melee Weapon"
		elif r == 8: itemtype = "Ranged Weapon or Simple Melee Weapon"
		elif r == 9: itemtype = "Wondrous Item (Belt, Boots, Bracers, Gauntlets, Gloves, etc.)"
		elif r == 10: itemtype = "Shield or Light Armor"
		elif r == 11: itemtype = "Medium Armor"
		else: itemtype = "Heavy Armor"
		# Print Magic Item
		intel = random.randint(1, 100)
		if intel == 100 or r == 7 and intel > 95: print("Magic Item: Intelligent", rarity, itemtype)
		else: print("Magic Item:", rarity, itemtype)

# Determine Total Value of Treasure Hoard
gold = 0
n = 1
d100 = random.randint(1, 100)
if ht == 1:
	while n < 5:
		gold += (random.randint(1, 6) * 10) + random.randint(1, 6)
		n += 1
	if d100 < 7: gold += 0
	elif d100 < 32: gold += ((random.randint(1, 6) + random.randint(1, 6)) * 10)
	elif d100 < 67: gold += ((random.randint(1, 4) + random.randint(1, 4)) * 25)
	else: gold += ((random.randint(1, 6) + random.randint(1, 6)) * 50)
elif ht == 2:
	while n < 11:
		gold += (random.randint(1, 6) * 100)
		n += 1
	if d100 < 5: gold += 0
	elif d100 < 30: gold += ((random.randint(1, 4) + random.randint(1, 4)) * 25)
	elif d100 < 55: gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 50)
	elif d100 < 87: gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 100)
	else: gold += ((random.randint(1, 4) + random.randint(1, 4)) * 250)
elif ht == 3:
	while n < 9:
		gold += (random.randint(1, 6) * 1000)
		n += 1
	if d100 < 4: gold += 0
	elif d100 < 31: gold += ((random.randint(1, 4) + random.randint(1, 4)) * 250)
	elif d100 < 55: gold += ((random.randint(1, 4) + random.randint(1, 4)) * 750)
	elif d100 < 77: gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 500)
	else: gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 1000)
else:
	while n < 4:
		gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 1000)
		gold += ((random.randint(1, 6) + random.randint(1, 6)) * 10000)
		n += 1
	if d100 < 3: gold += 0
	elif d100 < 41: gold += ((random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 1000)
	elif d100 < 71: gold += ((random.randint(1, 10)) * 2500)
	elif d100 < 91: gold += ((random.randint(1, 4)) * 7500)
	else: gold += ((random.randint(1, 8)) * 5000)
		
# Spell Components
# Gemstones (10, 25, 50, 100, 500, 1000, 5000)
gems = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) - random.randint(1, 20)
if gems > 0:
	print("### GEMSTONES ###")
	for i in range(gems):
		gv = random.randint(1, 10)
		gv = get_gemstone(gold, gv)
		if gv > 0:
			gold -= gv
			if gv == 10:
				x = random.randint(1, len(gemstone10gp)) - 1
				gem = gemstone10gp[x]
			elif gv == 25:
				x = random.randint(1, len(gemstone25gp)) - 1
				gem = gemstone25gp[x]
			elif gv == 50:
				x = random.randint(1, len(gemstone50gp)) - 1
				gem = gemstone50gp[x]
			elif gv == 100:
				x = random.randint(1, len(gemstone100gp)) - 1
				gem = gemstone100gp[x]
			elif gv == 500:
				x = random.randint(1, len(gemstone500gp)) - 1
				gem = gemstone500gp[x]
			elif gv == 1000:
				x = random.randint(1, len(gemstone1000gp)) - 1
				gem = gemstone1000gp[x]
			else:
				x = random.randint(1, len(gemstone5000gp)) - 1
				gem = gemstone5000gp[x]
			print("Gemstone:", gem, ";", gv, "gp")
	print(" ")

# Art Objects
artobjects = random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) - random.randint (1, 20)
if artobjects > 0:
	print("### ART OBJECTS ###")
	for i in range(artobjects):
		av = get_artobject(gold)
		gold -= av
	print("")
	
# Remaining Gold
print("Coins:", gold, "gp")
print("")

# Generate Consumable Magic Items
print("### CONSUMABLE ITEMS ###")
get_consumables(ht)
print("")
# Generate Magic Items
print("### MAGIC ITEMS ###")
get_magicitems(ht)
print("")

##########
# Generate Additional Consumable Magic Items to Purchase with Remaining Gold
print("### Additional Consumables to Purchase for Treasure Hoard ###")
if ht > 2: ht = 2
else: ht = 1
get_consumables(ht)
print("")
# Generate Additional Magic Items to Purchase with Remaining Gold
print("### Additional Magic Items to Purchase for Treasure Hoard ###")
get_magicitems(ht)
