# Character objects
# This class covers player characters, NPC's, and enemies as well
# The different types of characters can be denoted with the 'tag' attribute

from attStats import *
from levels import *
from attMappings import *
from content import Content
import json
import sys

e = Content().data

class Character(object):

	def __init__(self, make=None):

		self.name = "John Smith"

		self.character_class = "Base"

		self.tag = ""

		self.level = 0

		self.skills = []

		self.weapon = "naked"

		self.armor = "naked"

		self.eqp_mods = []

#		self.equipment = {
#				"weapon" : "naked",
#				"armor" : "naked",
#				"mods" : []
#				}

		self.inventory = []

		self.carry_weight = 0

		self.DEX = 0
		self.ART = 0
		self.MGT = 0
		self.DIV = 0
		self.INT = 0
		self.CON = 0

		self.MaxHP = 1
		self.Evade = 0
		self.Hit = 0
		self.Accuracy = 0
		self.PhyDef = 0
		self.PhyAtk = 0
		self.MagDef = 0
		self.MagAtk = 0
		self.RES = 0
		self.CarryStrength = 0
		self.CastingSpeed = 0
		self.SpellFailure = 0
		self.Craft = 0

#		self.stats = {
#				"MaxHP":"1","Evade":"0","Hit":"0",
#				"Accuracy":"0","Physical Defense":"0",
#				"Physical Attack":"0","Magical Defense":"0",
#				"Magical Attack":"0","Resistance":"0",
#				"Carry Strength":"0","Casting Speed":"0",
#				"Spell Failure":"0","Craft":"0"
#				}

		if make is not None:
			self.load(make)

	def load(self, charac):
		k = e[charac]
		self.name = charac
		self.character_class = k["character_class"]
		self.tag = k["tag"]
		self.level = int(k["level"])
		self.skills = k["skills"]
		self.equipment = k["equipment"]
		self.inventory = k["inventory"]
		self.carry_weight = int(k["carry_weight"])
		self.attributes = k["attributes"]
		self.stats = k["stats"]

	def stat_Map(self):
		return {"MaxHP":self.MaxHP,"Evade":self.Evade,"Hit":self.Hit,
				"Accuracy":self.Accuracy,"PhyDef":self.PhyDef,
				"PhyAtk":self.PhyAtk,"MagDef":self.MagDef,"MagAtk":self.MagAtk,
				"Resistance":self.Resistance,"CarryStrength":self.CarryStrength,
				"CastingSpeed":self.CastingSpeed,"SpellFailure":self.SpellFailure,
				"Craft":self.Craft}

	def update_stats(self, stat_dict):
		self.MaxHP = stat_dict["MaxHP"]
		self.Evade = stat_dict["Evade"]
		self.Hit = stat_dict["Hit"]
		self.PhyAtk = stat_dict["PhyAtk"]
		self.PhyDef = stat_dict["PhyDef"]
		self.MagAtk = stat_dict["MagAtk"]
		self.MagDef = stat_dict["MagDef"]
		self.Resistance = stat_dict["Resistance"]
		self.CarryStrength = stat_dict["CarryStrength"]
		self.CastingSpeed = stat_dict["CastingSpeed"]
		self.SpellFailure = stat_dict["SpellFailure"]
		self.Craft = stat_dict["Craft"]

	def set_name(self, name):
		self.name = name

	def att_Map(self):
		return {"DEX":self.DEX,"MGT":self.MGT,"CON":self.CON,
				"DIV":self.DIV,"INT":self.INT,"ART":self.ART}

	def update_atts(self, att_dict):
		self.DEX = att_dict["DEX"]
		self.DIV = att_dict["DIV"]
		self.CON = att_dict["CON"]
		self.MGT = att_dict["MGT"]
		self.INT = att_dict["INT"]
		self.ART = att_dict["ART"]

	def equip_armor(self, armor):
		if armor not in self.inventory:
			return "Armor not in inventory"
		elif self.character_class not in e[armor.kind]["classes"]:
			print "%s class cannot equip %s armor type" % (self.character_class, armor.kind)
		else:
			self.armor = armor

	def equip_weapon(self, weapon):
		# Equips a weapon object. Performs some validation to ensure weapon is equipable
		if weapon not in self.inventory:
			return "Weapon not in inventory"
		elif self.character_class not in e[weapon.kind]["classes"]:
			print "%s class cannot equip %s weapon type" % (self.character_class, weapon.kind)
		else:
			self.weapon = weapon

	def equip_weapon_from_string(self, weapon_string):
		# Sometimes you want to equip a weapon knowing only the string name.
		for item in self.inventory:
			if item.name == weapon_string:
				self.equip_weapon(item)
		return "Weapon not found."

	def equip_armor_from_string(self, armor_string):
		for item in self.inventory:
			if item.name == armor_string:
				self.equip_armor(item)
		return "Armor not found."

	def add_skill(self, skill_obj):
		# Add skill to skill list. Perform validation to make sure character can use it.
		req = skill_obj.requirements
		attMap = self.att_Map()
		if int(req["Level"]) > self.level:
			print "Character level too low to acquire this skill"
			exit()
		elif req["Class"] != []:
			if self.character_class not in req["Class"]:
				print "Character is the wrong class to acquire this skill"
				exit()
		elif req["Attributes"] != []:
			for att in req["Attributes"]:
				if attMap[att[:3]] < int(att[3:]):
					print "Character does not meet attribute requirement for skill"
					exit()
		self.skills.append(skill_obj)

	def set_carry_weight(self):
		weight = 0
		for item in self.inventory:
			weight += int(item.weight)
		self.carry_weight = weight

	def adjust_evade(self):
		# Adjust for inventory weight and carry strength
		self.set_carry_weight()
		weight_penalty = self.carry_weight/10
		mgt_adjusted = weight_penalty - int(self.CarryStrength)
		evade = int(self.Evade) - mgt_adjusted
		self.Evade = evade

	def get_equipment_mods(self):
		mods = []
		if self.weapon.name in e.keys():
			mods.extend(self.weapon.spec_mods)
		elif self.armor.name in e.keys():
			mods.extend(self.armor.spec_mods)
		self.eqp_mods = mods
