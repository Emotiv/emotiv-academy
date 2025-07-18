import sys
import os
from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
import json
from save_config import save_config
from live_advance import LiveAdvance
import threading

from PyQt6.QtWidgets import QMessageBox

your_app_client_id = ''  # Enter your Cortex client ID here
your_app_client_secret = ''  # Enter your Cortex client secret here

# Specify the headset ID to connect to.
# Leave it as an empty string ('') to automatically connect to the first available headset in the list.
headsetId = ''

class WelcomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()

        self.config_path = os.path.join(os.path.dirname(__file__), "config.json")
        if your_app_client_id == '':
            raise ValueError('Empty your_app_client_id. Please fill in your_app_client_id before running the example.')
        if your_app_client_secret == '':
            raise ValueError('Empty your_app_client_secret. Please fill in your_app_client_secret before running the example.')

        ui_path = os.path.join(os.path.dirname(__file__), "MainWindow.ui")
        uic.loadUi(ui_path, self)

        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(self.config_path, "r") as config_file:
            config = json.load(config_file)

        self.settings = [config["push"], config["pull"], config["left"], config["right"]]
        print(self.settings)
        self.live = LiveAdvance(your_app_client_id, your_app_client_secret)
        if "profile_name" in config:
            self.profileEdit.setText(config["profile_name"])

        self.PushCombo.setCurrentIndex(self.settings[0])
        self.PullCombo.setCurrentIndex(self.settings[1])
        self.LeftCombo.setCurrentIndex(self.settings[2])
        self.RightCombo.setCurrentIndex(self.settings[3])

        self.StartButton.clicked.connect(self.start_mapping)
        self.PauseButton.clicked.connect(self.pause_mapping)
        self.live.command_signal.connect(self.on_new_cmd)

        self.PullCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('pull', self.PullCombo.currentIndex()))
        self.PushCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('push', self.PushCombo.currentIndex()))
        self.LeftCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('left', self.LeftCombo.currentIndex()))
        self.RightCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('right', self.RightCombo.currentIndex()))

    def on_new_cmd(self, cmd):
        action = cmd.get('action', 'None')
        power = cmd.get('power', 0)

        self.OutPutLabel.setText(f"Current Emotiv BCI output: {action}")
        value = int(power * 100)
        self.powerBar.setValue(value)
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
        profile_name = self.profileEdit.text().strip()
        if not profile_name:
            QtWidgets.QMessageBox.warning(self, "Missing Profile Name", "Please enter a trained profile name before starting.")
            return

        print(f'Starting with profile: {profile_name}')
        with open(self.config_path, "r") as config_file:
            config = json.load(config_file)
        config["profile_name"] = profile_name
        with open(self.config_path, "w") as config_file:
            json.dump(config, config_file, indent=4)
        liveThread = threading.Thread(target=self.live.start, args=[profile_name, headsetId])
        liveThread.start()

    def pause_mapping(self):
        print('pause data stream')
        self.live.pause()


app = QtWidgets.QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setWindowIcon(QtGui.QIcon("logo.png"))  # add a logo here
widget.setWindowTitle("Emotiv DJI Controller")
widget.resize(796, 349)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")
