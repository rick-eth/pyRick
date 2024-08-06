# -*- coding: utf-8 -*-

__title__ = "Add Levels Elevation" #Name of the button displayed in REVIT UI
__doc__ = """Date    = 20.04.2022
_____________________________________________________________________
Description:
This is a tool will add/update your level name to have its elevation.
_____________________________________________________________________
How-to: (Example)
-> Click on the button
-> Change Settings(optional)
-> Rename Levels
_____________________________________________________________________
Last update:
- [06.08.2024] - 1.0 RELEASE
_____________________________________________________________________
To-Do:
- Check Revit 2022
- Add ... Feature
_____________________________________________________________________
Author: Ricardo Braga""" # Button description shown in Revit UI

__author__ = "Ricardo Braga"
# __helpurl__ "www.youtube.com" #TODO: Update URL
__highlight__ = "new"
__min_revit_ver__ = "2022"
__max_revit_ver__ = "2022"
# __context__ = ["Walls", "Floors", "Roofs"] #Make your button avaliable only when certain categories are selected

# IMPORTS
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==========================================

# Regular + Autodesk
import os, sys,math, datetime, time
from Autodesk.Revit.DB import * # import everything from DB (very good for beginners and development)
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector, BuiltInCategory

#pyrevit

#Custom Imports
from Snippets._selection import get_selected_elements
from Snippets._convert import convert_internal_to_m



# .Net Imports

import clr
clr.AddReference("System")
from System.Collections.Generic import List #List<ElementType>() <- it's special type of list that RevitAPI often requires



# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==========================================
# from pyrevit.revit import uidoc, doc, app # Alternative

doc = __revit__.ActiveUIDocument
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
#PATH SCRIPT = os.path.dirname(__file__)


#Symbols
symbol_start = "]"
symbol_end = "["



# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
#==========================================


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
#==========================================






# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==========================================




#Get all levels
all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()


#Get Levels Elevations + convert to meters + rounding


for lvl in all_levels:
    lvl_elevation = lvl.Elevation
    lvl_elevation_m = round (convert_internal_to_m(lvl.Elevation))
    lvl_elevation_m_str = "+" +  str(lvl_elevation_m) if lvl.Elevation > 0 else str(lvl_elevation_m)

    # Check if elevation already exists

    # ELEVATION EXISTS

    # ELEVATION DOES NOT EXIST (new)
    elevation_value = symbol_start + lvl_elevation_m - str + symbol_end
    new_name = lvl.Name + elevation_value

    t = Transaction(doc, __title__)

    t.Start()
    try:
        lvl.Name = new_name
        print("Renamed: {} -> {}".format(lvl.name, new_name))

    except:
        print("Could not change Level's Name...")

    t.Commit()


# Add/Update Levels Elevations

# Report Changes




