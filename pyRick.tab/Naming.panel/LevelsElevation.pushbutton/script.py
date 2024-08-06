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
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector

#pyrevit

#Custom Imports

from Snippets._selection import get_selected_elements
from Snippets._convert

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
PATH SCRIPT = os.path.dirname(__file__)


#Symbols
symbol_start = "]"
symbold_end = "["



# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
#==========================================

def convert_internal_to_m(length):
    """Funtion to convert internal units to meters
    :param length: Length in internal revit units
    :return: Length in Meters, rounded to 2nd digit
    """
    rvt_year = int(app.VersionNumber)

    #RVT < 2022
    if rvt_year < 2022:
        return UnitUtils.Convert(length,
                                 DisplayUnitType.DUT_DECIMAL_FEET,
                                 DisplayUnitType.DUT_METERS) # Change to any other unit here..

    #RVT >= 2022
    else:
        return UnitUtils.ConvertFromInternalUnits(length, UnitTypeId.Meters)
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


#Get Levels Elevations

for lvl in all_levels:
    lvl_elevation = lvl.Elevation
    lvl_elevation_m = lvl_elevation /0.3048
# convert to meters + rounding

# check if elevation already exists

# Add/Update Levels Elevations

# Report Changes




