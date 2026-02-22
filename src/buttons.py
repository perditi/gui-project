from PyQt6.QtGui import QAction, QIcon

def about_button(app):
    about_button = QAction("About...", app)
    about_button.triggered.connect(about_button_pressed)
    return about_button

def about_button_pressed():
    print("About button pressed")