# Brain Computer Interface Controlled DJI RoboMaster

Developed in Collaboration with the Imagination Center at the Glenrose Rehabilitation Hospital. https://www.imagination-centre.ca/

## Project Highlights
- Compatible with DJI RoboMaster robot
- Real-time Brain-Computer Interface (BCI) control via EMOTIV headset
- Built with Python and PyQt6 graphical user interface
- Visual training feedback with dynamic command output and power indicator
- Mental command mapping for robotic motion: push, pull, left, right
- Integrates with Cortex API for EEG streaming and command detection

You can see the step-by-step tutorial here: https://www.youtube.com/watch?v=9G00Tl1ymNI.

## Requirement
- This example works with Python >= 3.7
- Recommended Python version: 3.9
- UI built using PyQt6
- Install websocket client via  `pip install websocket-client`
- Install python-dispatch via `pip install python-dispatch`
- Install PyQt6 via `pip install PyQt6`

## Before you start

To run the existing example you will need to do a few things.

1. You will need an EMOTIV headset.  You can purchase a headset in our [online store](https://www.emotiv.com/)
2. Next, [download and install](https://www.emotiv.com/developer/) the Cortex service.  Please note that currently, the Cortex service is only available for Windows and macOS.
3. We have updated our Terms of Use, Privacy Policy and EULA to comply with GDPR. Please login via the EMOTIV Launcher to read and accept our latest policies in order to proceed using the following examples.
4. Next, to get a client id and a client secret, you must connect to your Emotiv account on [emotiv.com](https://www.emotiv.com/my-account/cortex-apps/) and create a Cortex app. If you don't have a EmotivID, you can [register here](https://id.emotivcloud.com/eoidc/account/registration/).
5. Then, if you have not already, you will need to login with your Emotiv id in the EMOTIV Launcher.
6. Open the EmotivBCI application and create a training profile with your headset. Start training at least one Mental Command action and make sure it reaches a usable level of accuracy.
7. Finally, the first time you run these examples, you also need to authorize them in the EMOTIV Launcher.

---

## Cortex Library
- [`cortex.py`](./cortex.py) - the wrapper lib around EMOTIV Cortex API.

## Main
- [`main.py`](./main.py)
- Fill in your Cortex client secret, client ID and trained profile name from EmotivBCI to get started.
- Now supports dynamic profile name input through the PyQt6 UI.

## Susbcribe Data
- [`live_advance.py`](./live_advance.py) shows data streaming from Cortex: EEG, motion, band power and Performance Metrics.
- Now includes PyQt6 signal binding for live UI updates.
- For more details https://emotiv.gitbook.io/cortex-api/data-subscription
