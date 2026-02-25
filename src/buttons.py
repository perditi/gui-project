from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt

## MENU BUTTONS

def about_button(app):
    about_button = QAction("About...", app)
    
    about_button.triggered.connect(about_button_pressed)
    return about_button

def about_button_pressed(s):
    print("About button pressed")


## APP BUTTONS

def raw_mics_checkbox(app):
    raw_mics = QCheckBox("raw mics")
    raw_mics.setCheckState(Qt.CheckState.Unchecked)

    raw_mics.stateChanged.connect(show_state)
    return raw_mics

def ec_mics_checkbox(app):
    ec_mics = QCheckBox("EC mics")
    ec_mics.setCheckState(Qt.CheckState.Unchecked)

    ec_mics.stateChanged.connect(show_state)
    return ec_mics

def raw_speakers_checkbox(app):
    raw_speakers = QCheckBox("raw speakers")
    raw_speakers.setCheckState(Qt.CheckState.Unchecked)

    raw_speakers.stateChanged.connect(show_state)
    return raw_speakers

def ec_speakers_checkbox(app):
    ec_speakers = QCheckBox("EC speakers")
    ec_speakers.setCheckState(Qt.CheckState.Unchecked)

    ec_speakers.stateChanged.connect(show_state)
    return ec_speakers

# ^^ all of these default to unchecked, later can add a preferences file that saves config so it defaults to what you had it last

def show_state(s):
    print(s == Qt.CheckState.Checked.value)
