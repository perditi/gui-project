from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QCheckBox, QPushButton, QTextEdit
from PyQt6.QtCore import Qt
import os

## MENU BUTTONS

def about_button(app):
    about_button = QAction("About...", app)
    
    about_button.triggered.connect(about_button_pressed)
    return about_button

def about_button_pressed(s):
    print("About button pressed")


## APP BUTTONS ETC.

def file_select1(app):
    file_txt1 = QTextEdit()
    return file_txt1

def browse_files_button(app, action):
    browse_files = QPushButton("Browse...")
    browse_files.clicked.connect(action)
    return browse_files

def folder_select1(app):
    folder_txt1 = QTextEdit()
    return folder_txt1

def browse_folders_button(app, action):
    browse_folders = QPushButton("Browse...")
    browse_folders.clicked.connect(action)
    return browse_folders

def raw_mics_checkbox(app, action):
    raw_mics = QCheckBox("raw mics")
    raw_mics.setCheckState(Qt.CheckState.Unchecked)

    raw_mics.stateChanged.connect(action)
    return raw_mics

def ec_mics_checkbox(app, action):
    ec_mics = QCheckBox("EC mics")
    ec_mics.setCheckState(Qt.CheckState.Unchecked)

    ec_mics.stateChanged.connect(action)
    return ec_mics

def raw_speakers_checkbox(app, action):
    raw_speakers = QCheckBox("raw speakers")
    raw_speakers.setCheckState(Qt.CheckState.Unchecked)

    raw_speakers.stateChanged.connect(action)
    return raw_speakers

def ec_speakers_checkbox(app, action):
    ec_speakers = QCheckBox("EC speakers")
    ec_speakers.setCheckState(Qt.CheckState.Unchecked)

    ec_speakers.stateChanged.connect(action)
    return ec_speakers

    # ^^ all of these default to unchecked, later can add a preferences file that saves config so it defaults to what you had it last
