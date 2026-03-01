from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QStatusBar, QHBoxLayout, QVBoxLayout, QFileDialog
# Only needed for access to command line arguments
import sys, os
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

        self.file_select1 = buttons.file_select1(self)
        self.folder_select1 = buttons.folder_select1(self)
        left.addWidget(self.file_select1)
        left.addWidget(buttons.browse_files_button(self, self.browse_for_file))
        left.addWidget(buttons.raw_mics_checkbox(self, self.show_state))
        left.addWidget(buttons.ec_mics_checkbox(self, self.show_state))
        left.addWidget(buttons.raw_speakers_checkbox(self, self.show_state))
        left.addWidget(buttons.ec_speakers_checkbox(self, self.show_state))
        left.addWidget(self.folder_select1)
        left.addWidget(buttons.browse_folders_button(self, self.browse_for_folder))
        
        self.setWindowTitle("Unnamed App")
        self.setStatusBar(QStatusBar(self))
        self.setFixedSize(QSize(400,300))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)

    def browse_for_file(self):
        print('browse button click')
        file_filter = "Binary files (*.bin; *.dat);;All Files (*.*)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=file_filter.split(';;')[0]
        )
        self.file_select1.setText(str(response[0]))

    def browse_for_folder(self):
        print('brwose folder btn')
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Select a folder'
        )
        print(response)

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