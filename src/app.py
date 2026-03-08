from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QStatusBar, QHBoxLayout, QVBoxLayout, QFileDialog, QLayout, QLabel
# Only needed for access to command line arguments
import sys, os
import buttons

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graph_windows = {}
        self.graph_windows_num = 0

        status_bar = QStatusBar(self)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File") #The ampersand defines a quick key to jump to this menu when pressing Alt
        edit_menu = menu.addMenu("&Edit")
        about_menu = menu.addMenu("?")
        about_menu.addAction(buttons.about_button(self))

        layout = QHBoxLayout()

        left = QVBoxLayout()
        #left.setHorizontalSizeConstraint()
        layout.addLayout(left)
        
        right = QVBoxLayout()
        layout.addLayout(right)

        # Set the central widget of the Window.
        filler_button = QPushButton("filler button")
        filler_button.clicked.connect(self.open_graph_window)
        right.addWidget(filler_button)

        self.file_select1 = buttons.file_select1(self)
        self.folder_select1 = buttons.folder_select1(self)
        file_select_layout = QHBoxLayout()
        file_select_layout.addWidget(self.file_select1)
        file_select_layout.addWidget(buttons.browse_files_button(self, self.browse_for_file))
        left.addLayout(file_select_layout)
        left.addWidget(buttons.raw_mics_checkbox(self, self.show_state))
        left.addWidget(buttons.ec_mics_checkbox(self, self.show_state))
        left.addWidget(buttons.raw_speakers_checkbox(self, self.show_state))
        left.addWidget(buttons.ec_speakers_checkbox(self, self.show_state))
        folder_select_layout = QHBoxLayout()
        folder_select_layout.addWidget(self.folder_select1)
        folder_select_layout.addWidget(buttons.browse_folders_button(self, self.browse_for_folder))
        left.addLayout(folder_select_layout)
        
        self.setWindowTitle("Unnamed App")
        self.setStatusBar(status_bar)
        self.setMinimumSize(QSize(500,300)) # width, height
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
        self.folder_select1.setText(str(response))

    def open_graph_window(self):
        print(f'adding {self.graph_windows_num}')
        new_key = self.graph_windows_num
        new_window = GraphWindow(self, new_key)
        self.graph_windows[new_key] = new_window
        self.graph_windows_num += 1
        new_window.show()
        print(f"now we have {len(self.graph_windows)} windows")

    def closeEvent(self, event):
        print("closing app")
        for key in list(self.graph_windows.keys()):
            self.graph_windows[key].close()

class GraphWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, app, key, title=''):
        super().__init__()
        self.setWindowTitle(title)
        self.app = app
        self.key = key

        layout = QVBoxLayout()
        self.label = QLabel(f"Another Window {key}")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def closeEvent(self, event):
        print(f"removing {self.key}")
        del self.app.graph_windows[self.key]
        print(f"now we have {len(self.app.graph_windows)} windows")

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
window.setFocus()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
print("goodbveee")