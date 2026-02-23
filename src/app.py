from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QStatusBar, QHBoxLayout, QVBoxLayout
# Only needed for access to command line arguments
import sys
import buttons

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        status_bar = QStatusBar()

        menu = self.menuBar()
        file_menu = menu.addMenu("&File") #The ampersand defines a quick key to jump to this menu when pressing Alt
        edit_menu = menu.addMenu("&Edit")
        about_menu = menu.addMenu("?")
        about_menu.addAction(buttons.about_button(self))

        layout = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()
        layout.addLayout(left)
        layout.addLayout(right)

        # Set the central widget of the Window.
        filler_button = QPushButton("filler button")
        right.addWidget(filler_button)

        left.addWidget(buttons.raw_mics_checkbox(self))
        
        self.setWindowTitle("Unnamed App")
        self.setStatusBar(QStatusBar(self))
        self.setFixedSize(QSize(400,300))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
print("goodbveee")