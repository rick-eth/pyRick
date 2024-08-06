# -*- coding: utf-8 -*-

# Imports

from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

#Functions

def get_selected_elements(uidoc):
    """This functions will return elements that are currently selected in revit UI
    :param uidoc: uidoc where elements are selected
    :return: list od selected elements """

    selected_elements = []
    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)

    return selected_elements
