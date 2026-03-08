from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QStatusBar, QHBoxLayout, QVBoxLayout, QFileDialog, QLayout, QLabel, QTabWidget
# Only needed for access to command line arguments
import pyqtgraph as pg
import sys, os
from datetime import datetime
import buttons

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graph_windows = {}

        parse_window_layout = QHBoxLayout()
        parse_settings = QVBoxLayout()
        plot_window_layout = QVBoxLayout()
        plot_settings = QVBoxLayout()
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)


        status_bar = QStatusBar(self)

        # MENU
        menu = self.menuBar()
        file_menu = menu.addMenu("&File") #The ampersand defines a quick key to jump to this menu when pressing Alt
        edit_menu = menu.addMenu("&Edit")
        about_menu = menu.addMenu("?")

        file_menu.addAction(buttons.preferences_button(self))
        about_menu.addAction(buttons.about_button(self))

        #layout = QHBoxLayout()

        # PARSE WINDOW
        self.file_select1 = buttons.file_select1(self) # text box
        self.folder_select1 = buttons.folder_select1(self) # text box
        self.raw_mic_chk = buttons.raw_mics_checkbox(self, self.show_state)
        self.ec_mic_chk = buttons.ec_mics_checkbox(self, self.show_state)
        self.raw_spkr_chk = buttons.raw_speakers_checkbox(self, self.show_state)
        self.ec_spkr_chk = buttons.ec_speakers_checkbox(self, self.show_state)

        file_select_layout = QHBoxLayout()
        file_select_layout.addWidget(self.file_select1)
        file_select_layout.addWidget(buttons.browse_files_button(self, self.browse_for_file))
        parse_settings.addLayout(file_select_layout)
        parse_settings.addWidget(self.raw_mic_chk)
        parse_settings.addWidget(self.ec_mic_chk)
        parse_settings.addWidget(self.raw_spkr_chk)
        parse_settings.addWidget(self.ec_spkr_chk)
        folder_select_layout = QHBoxLayout()
        folder_select_layout.addWidget(self.folder_select1)
        folder_select_layout.addWidget(buttons.browse_folders_button(self, self.browse_for_folder))
        parse_settings.addLayout(folder_select_layout)

        parse_window_layout.addLayout(parse_settings)
        parse_window_layout.addWidget(buttons.parse_button(self, self.parse))
        
        # PLOT WINDOW
        

        plot_window_layout.addLayout(plot_settings)
        plot_window_layout.addWidget(buttons.plot_button(self, self.open_graph_window))

        


        self.setWindowTitle("Unnamed App")
        self.setStatusBar(status_bar)
        self.setMinimumSize(QSize(500,300)) # width, height
        parse_window = QWidget()
        parse_window.setLayout(parse_window_layout)
        plot_window = QWidget()
        plot_window.setLayout(plot_window_layout)
        tabs.addTab(parse_window, "Parse")
        tabs.addTab(plot_window, "Plot")
        self.setCentralWidget(tabs)

    def parse(self):
        print("parse byutton pressed")
        print(f"source: {self.file_select1.text()}")
        print()

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
        new_key = datetime.now()
        print(f'adding {new_key}')
        new_window = GraphWindow(self, new_key)
        self.graph_windows[new_key] = new_window
        new_window.show()
        print(f"now we have {len(self.graph_windows)} windows")

    def closeEvent(self, event):
        print("closing app")
        num_closed = 0
        for key in list(self.graph_windows.keys()):
            self.graph_windows[key].close()
            num_closed += 1
        if num_closed == 0:
            print("no graph windows to close")
        else:
            print(f"closed {num_closed} grpah windows")

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

        self.graph = pg.PlotWidget()
        self.graph.setBackground('w')
        pen = pg.mkPen(color=(0,0,0))
        layout.addWidget(self.graph)
        x = [a for a in range(100)]
        y = [-1*((b*b) - (100*b)) for b in x]
        self.graph.plot(x,y, pen=pen)

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