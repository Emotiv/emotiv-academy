# Brain-Computer Interface Controlled DJI RoboMaster

Developed in collaboration with the Imagination Center at the Glenrose Rehabilitation Hospital.  
[Imagination Centre Website](https://www.imagination-centre.ca/)

## Overview

This project enables real-time control of a DJI RoboMaster robot using brain-computer interface (BCI) signals from an EMOTIV headset. Leverage mental commands to move the robot in multiple directions, offering hands-free, intuitive operation.

A step-by-step tutorial video is available [here](https://www.youtube.com/watch?v=9G00Tl1ymNI).

## Features

- **DJI RoboMaster compatible:** Seamless integration with the DJI RoboMaster platform.
- **Real-time BCI control:** Send mental commands (push, pull, left, right) to the robot via EMOTIV headset.
- **Dynamic UI:** PyQt6-powered interface provides live feedback, including command output and power indicator.
- **Customizable key mapping:** Easily configure which mental command triggers which robot movement.
- **Cortex API integration:** Robust connection for EEG streaming and command detection.
- **Profile management:** Dynamically input and switch user profiles from the UI.

## Requirements

- Python 3.7 or higher (recommended: Python 3.9)
- EMOTIV headset ([purchase here](https://www.emotiv.com/))
- [Cortex Service](https://www.emotiv.com/developer/) (Windows/macOS only)
- PyQt6: `pip install PyQt6`
- websocket-client: `pip install websocket-client`
- python-dispatch: `pip install python-dispatch`

## Getting Started

1. **EMOTIV Hardware:** Obtain an EMOTIV headset from the [EMOTIV store](https://www.emotiv.com/).
2. **Install Cortex:** [Download and install Cortex](https://www.emotiv.com/developer/) for Windows or macOS.
3. **Accept Policies:** Log in via the EMOTIV Launcher and accept the latest Terms of Use, Privacy Policy, and EULA (GDPR compliance).
4. **Create Cortex App:** In [My Account](https://account.emotiv.com/my-account/cortex-apps/), create a Cortex app and obtain your client ID and secret. [Register here](https://id.emotivcloud.com/eoidc/account/registration/) if you don't have an account.
5. **Login in Launcher:** Log in with your Emotiv ID in the EMOTIV Launcher.
6. **Train a Profile:** Open the EmotivBCI application, create a training profile, and train at least one Mental Command action to a usable accuracy level.
7. **Authorize Application:** The first time you run this app, authorize it in the EMOTIV Launcher.

---

## Project Structure

- [`main.py`](./main.py): Main application entry. Fill in your Cortex client credentials and trained profile name to get started. You can now set the profile name dynamically in the UI.
- [`cortex.py`](./cortex.py): Wrapper library for the EMOTIV Cortex API.
- [`live_advance.py`](./live_advance.py): Handles EEG data streaming, PyQt6 signal binding, and live UI updates.
- [`config.json`](./config.json): Stores key mapping and profile information.

## Usage

1. Install requirements:
    ```bash
    pip install PyQt6 websocket-client python-dispatch
    ```
2. Fill in your Cortex client ID and secret in `main.py`:
    ```python
    your_app_client_id = 'YOUR_CLIENT_ID'
    your_app_client_secret = 'YOUR_CLIENT_SECRET'
    ```
3. Run the application:
    ```bash
    python main.py
    ```

4. In the UI:
    - Enter your trained profile name.
    - Optionally, adjust the key mappings for push, pull, left, and right actions.
    - Click **Start** to begin streaming and controlling the robot.
    - Watch the command output and power indicator for live feedback.

## Troubleshooting

- **Connection Issues:** Ensure the Cortex service is running and you are logged in via the EMOTIV Launcher.
- **No command detected:** Retrain your profile in EmotivBCI and ensure the selected action(s) are active and accurate.
- **PyQt6 Errors:** Make sure you are using an appropriate Python version and have installed all dependencies.

## Resources

- [Cortex API Data Subscription Documentation](https://emotiv.gitbook.io/cortex-api/data-subscription)
- [EMOTIV Developer Portal](https://www.emotiv.com/developer/)
- [YouTube Tutorial](https://www.youtube.com/watch?v=9G00Tl1ymNI)

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

---

If you need additional help or run into issues, please consult the [EMOTIV support site](https://www.emotiv.com/pages/contact) or open a GitHub issue in this repository.
