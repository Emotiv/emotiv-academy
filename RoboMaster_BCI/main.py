from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.uic import loadUi
import json
from save_config import save_config
from live_advance import LiveAdvance
import threading

your_app_client_id = '' # Enter your Cortex client ID here
your_app_client_secret = '' # Enter your Cortex client secret here
trained_profile_name = '' # Enter your trained profile name from EmotivBCI here
trained_cmd = 'push'

class WelcomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("MainWindow.ui", self)
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        self.settings = [config["push"], config["pull"], config["left"], config["right"]]
        print(self.settings)
        self.l = LiveAdvance(your_app_client_id, your_app_client_secret)

        self.PushCombo.setCurrentIndex(self.settings[0])
        self.PullCombo.setCurrentIndex(self.settings[1])
        self.LeftCombo.setCurrentIndex(self.settings[2])
        self.RightCombo.setCurrentIndex(self.settings[3])
        self.StartButton.clicked.connect(lambda: self.start_mapping())
        self.PauseButton.clicked.connect(lambda: self.pause_mapping())
        self.PullCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('pull', self.PullCombo.currentIndex()))
        self.PushCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('push', self.PushCombo.currentIndex()))
        self.LeftCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('left', self.LeftCombo.currentIndex()))
        self.RightCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('right', self.RightCombo.currentIndex()))

    def on_new_cmd(self, cmd):
        self.OutPutLabel.setText(f"Current Emotiv BCI output: {cmd['action']}, {cmd['power']}")

    def on_combobox_changed(self, name, value):
        if name == 'push':
            self.settings[0] = value
        elif name == 'pull':
            self.settings[1] = value
        elif name == 'left':
            self.settings[2] = value
        elif name == 'right':
            self.settings[3] = value
        save_config(self.settings)

    def start_mapping(self):
        print('start_mapping')
        liveThread = threading.Thread(target=self.l.start, args=[trained_profile_name])
        liveThread.start()

    def pause_mapping(self):
        print('pause mapping')


app = QtWidgets.QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setWindowIcon(QtGui.QIcon("logo.png")) #add a logo here
widget.setWindowTitle("Emotiv DJI Controller")
widget.resize(796,349)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")