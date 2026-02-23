from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt

## MENU BUTTONS

def about_button(app):
    about_button = QAction("About...", app)

    def about_button_pressed():
        print("About button pressed")
    
    about_button.triggered.connect(about_button_pressed)
    return about_button



## APP BUTTONS

def raw_mics_checkbox(app):
    raw_mics = QCheckBox("raw mics")
    raw_mics.setCheckState(Qt.CheckState.Unchecked)

    def raw_mics_show_state():
        print()

    raw_mics.stateChanged.connect(show_state)
    return raw_mics

def show_state(s):
    print(s == Qt.CheckState.Checked.value)