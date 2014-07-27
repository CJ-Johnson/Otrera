# addContent.py uses this module to create new content by loading templates.
# The key "$THING Name" gets replaced with the object's actual name

templates = {
	"weapon" : { 
		"Weapon Name" : {
			"weight" : "1",
			"base_pwr" : "1",
			"durability" : "1",
			"kind" : "sword",
			"spec_mods" : []
			}
		},
	"armor" : {
		"Armor Name" : {
			"weight" : "1",
			"durability" : "1",
			"kind" : "leather",
			"capacity" : "1",
			"spec_mods" : []
			}
		},
	"item" : {
		"Item Name" : {
			"weight" : "1",
			"kind" : "usable",
			"effect" : "none",
			"special" : {},
			"durability" : "1"
			} 
		},
	"skill" : {
		"Skill Name" : {
			"category" : "none",
			"flavor" : "vanilla",
			"uses" : "1",
			"effect" : {
				"AOE" : "none",
				"Description" : "Random Text",
				"Element" : "none",
				"Power" : "none",
				"Range" : "0",
				"Inflicts" : "none",
				"Time" : "0"
				},
			"requirements" : {
				"Attributes" : [],
				"Class" : [],
				"Level" : "1"
				},
			"restrictions" : {
				"Equipment" : [],
				"Stats" : [],
				"Status" : []
				}
			}
		},
	"character" : {
			"Character Name" : {
				"character_class" : "",
				"tag" : "",
				"level" : "0",
				"skills" : [],
				"weapon" : "naked",
				"armor" : "naked",
				"mods" : []
				"inventory" : [],
				"carry_weight" : "0",
				"DEX":0,"ART":0,"MGT":0,
				"DIV":0,"INT":0,"CON":0
				"MaxHP":"1","Evade":"0","Hit":"0",
				"Accuracy":"0","PhyDef":"0",
				"PhyAtk":"0","MagDef":"0",
				"MagAtk":"0","Resistance":"0",
				"CarryStrength":"0","CastingSpeed":"0",
				"SpellFailure":"0","Craft":"0"
					}
				}
			},
	"class" : {
			"Class Name" : {
				"level_atts" : {
					"1":"","2":"","3":"","4":"","5":"",
					"6":"","7":"","8":"","9":"","10":""
					}
				}
			}
	}
