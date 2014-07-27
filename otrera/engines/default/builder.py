#!/usr/bin/env python
# Program for building characters
# For now it just prints character info to the console
# We need to give this script the ability to save characters as JSON blobs.

from attStats import *
from levels import *
from items import *
from character import Character
import json

def level_zero_character_builder():
	zero_character = Character()
	print "Give me some stats, bro\n"
	base_character = get_base_attributes(zero_character)
	print "\nOK! Let's get those stats!\n"
	print "---------------------------------------------------\n"
	base_character.stats = get_stats(base_character.attributes)
	return base_character

def custom_level_naked_character_builder():
	charac = level_zero_character_builder()
	charac.level = int(raw_input("What is the character's level?: "))
	charac.character_class = raw_input("What is the character's class?: ").lower().strip()
	level_mods = get_level_mods(charac.character_class, charac.level)
	charmap = charac.att_Map()
	for key in charmap:
		charmap[key] = charmap[key]+ int(level_mods[key])
	charac.update_atts(charmap)
	stats = get_stats(charmap)
	charac.update_stats(stats)
	return charac

def fully_equipped_character_builder():
	full_charac = custom_level_naked_character_builder()
	print "Cool! Lets add some equipment"
	inventory_list = raw_input("Give me a list of inventory separated by commas: ")
	inv_list = inventory_list.split(",")
	full_charac.inventory = get_inventory_from_string_list(inv_list)
	full_charac.adjust_evade()
	final_charac = user_sets_equipment(full_charac, full_charac.inventory)
	return final_charac

def complete_character_builder():
	charac = fully_equipped_character_builder()
	print "Score! Lets complete the character by choosing skills"
	eligible_skills = get_class_skills(charac)
	eligible_skills.extend(get_attribute_skills(charac))
	charac = user_picks_skills(charac, eligible_skills)
	return charac

def user_sets_equipment(charac, inventory):
	print "Here is your inventory: "
	for item in inventory:
		print item.name
	print "Name the item you wish to equip"
	w = raw_input("Select your weapon: ").lower()
	a = raw_input("Select your armor: ").lower()
	charac.equip_weapon_from_string(w)
	charac.equip_armor_from_string(a)
	charac.get_equipment_mods()
	return charac

def user_picks_skills(charac, eligible_skills):
	print "Here are your eligible skills:"
	for thing in eligible_skills:
		print thing.name
	print "You may select %s skills (character level)\n" % str(charac.level)
	selected = raw_input("Enter a comma-separated list: ")
	list_names = selected.split(",")
	skill_names = []
	for item in list_names:
		item = item.lstrip()
		skill_names.append(item)
	for item in eligible_skills:
		if item.name in skill_names:
			charac.add_skill(item)
	return charac

def get_base_attributes(charac):
	charac.name = raw_input("Name your character: ")
	DEX = int(raw_input("Dexterity: "))
	ART = int(raw_input("Artistry: "))
	MGT = int(raw_input("Might: "))
	DIV = int(raw_input("Divine: "))
	INT = int(raw_input("Intelligence: "))
	CON = int(raw_input("Constitution: "))
	charac.attributes = {
			"DEX":DEX,"ART":ART,"MGT":MGT,"DIV":DIV,"INT":INT,"CON":CON
			}
	return charac

def publish_character(charac):
	print "Character Name: %s" % charac.name
	print "MaxHP = %s" % str(stats["maxHP"])
	print "Evade = %s" % str(stats["Evade"])
	print "Hit = %s" % str(stats["Hit"])
	print "Accuracy = %s" %str(stats["Accuracy"])
	print "Physical Defense = %s" % str(stats["Physical Defense"])
	print "Physical Attack = %s" % str(stats["Physical Attack"])
	print "Magical Defense = %s" % str(stats["Magical Defense"])
	print "Magical Attack = %s" % str(stats["Magical Attack"])
	print "Resistance = %s" % str(stats["Resistance"])
	print "Carry Strength = %s" % str(stats["Carry Strength"])
	print "Casting Speed = %s" % str(stats["Casting Speed"])
	print "Spell Failure = %s" % str(stats["Spell Failure"])
	print "Craft = %s" % str(stats["Craft"])

def publish_charac_combat_stats(charac):
	print "Here is your character's combat profile:"
	print "-------------------------------------------------\n"
	print "PWR = %s %s" % (charac.equipment["weapon"].base_pwr, charac.stats["Physical Attack"])
	print "Armor Durability = %s" % str(charac.equipment["armor"].durability)
	print "Armor Defense = %s" % charac.equipment["armor"].defense
	print "Carry Weight = %s" % str(charac.carry_weight)
	print "Equipment Bonuses = %s" % (charac.equipment["mods"])
	print "NOTE: Evade score now accounts for Carry Weight penalty (adjusted for strength)"

def publish_charac_skills(charac):
	print "--------------------------------------------------\n"
	print "Here is a list of your character's skills: "
	for item in charac.skills:
		print item.name
	return

def publish_complete_character(charac):
	publish_character(charac)
	publish_charac_combat_stats(charac)
	publish_charac_skills(charac)

def choose_program():
	print "Welcome to the Mythology Character Builder!\n"
	print "---------------------------------------------------"
	print "Press '1' to build a level 0 character"
	print "Press '2' to build a custom level character"
	print "Press '3' to build a custom level character with equipment"
	print "Press '4' to build a complete character with skills and equipment"
	print "Press any other key to exit"
	user_input = raw_input("Enter a number and press 'enter': ")
	if user_input == "1":
		character = level_zero_character_builder()
		publish_character(character)
	elif user_input == "2":
		character = custom_level_naked_character_builder()
		publish_character(character)
	elif user_input == "3":
		character = fully_equipped_character_builder()
		publish_character(character)
		publish_charac_combat_stats(character)
	elif user_input == "4":
		charac = complete_character_builder()
		publish_complete_character(charac)
	else:
		return

def main():
	choose_program()

if __name__=="__main__":
	main()
