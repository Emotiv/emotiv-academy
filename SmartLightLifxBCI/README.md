# Smart Light Control with Emotiv BCI and Node-RED

Control a **LIFX smart light** using your thoughts, powered by an **Emotiv EEG headset** and **Node-RED**. This brain-computer interface (BCI) project demonstrates how mental commands can directly control smart devices.

## Overview

This project enables real-time control of LIFX smart lights via BCI signals from an EMOTIV headset.

- **Emotiv Headset**: Captures mental commands like *Push*, *Pull*.
- **Node-RED**: Processes brain data and manages automation.
- **LIFX Smart Bulbs**: Receive real-time control signals via Node-RED.

A step-by-step video tutorial is available:  
[Smart Light Control with BCI (YouTube)](https://www.youtube.com/watch?v=vdgzOriqC9Y&ab_channel=EmotivAcademy)

## Features

- **LIFX Integration:** Seamless control of LIFX smart bulbs.
- **Real-time BCI:** Send mental commands to your lights via Emotiv headset.
- **Customizable Flows:** Edit Node-RED flows for your automation needs.
- **Easy Setup:** Pre-built Node-RED flow included.
- **Cortex API:** Robust connection for EEG streaming and command detection.
- **Profile management:** Use your own trained mental command profiles.

## Requirements

- Emotiv Cortex running on your computer ([download here](https://www.emotiv.com/developer/))
- Emotiv Insight, EpocX, or MN8 headset ([purchase here](https://www.emotiv.com/))
- LIFX smart light connected to the same network
- Node-RED installed and configured
- Node-RED Emotiv BCI and LIFX nodes

## Getting Started

1. **EMOTIV Hardware:** Obtain an EMOTIV headset from the [EMOTIV store](https://www.emotiv.com/).
2. **Install Cortex:** [Download and install Cortex](https://www.emotiv.com/developer/) for Windows or macOS.
3. **Accept Policies:** Log in via the EMOTIV Launcher and accept the latest Terms of Use, Privacy Policy, and EULA (GDPR compliance).
4. **Create Cortex App:** In [My Account](https://account.emotiv.com/my-account/cortex-apps/), create a Cortex app and obtain your client ID and secret. [Register here](https://id.emotivcloud.com/eoidc/account/create).
5. **Login in Launcher:** Log in with your Emotiv ID in the EMOTIV Launcher.
6. **Train a Profile:** Open the EmotivBCI application, create a training profile, and train at least one Mental Command to a usable accuracy level.
7. **Authorize Application:** The first time you run these examples, authorize them in the EMOTIV Launcher.

---

## Installation Guide

### 1. Install Node-RED

**On macOS:**
```bash
sudo npm install -g --unsafe-perm node-red
```
**On Windows:**
```bash
npm install -g --unsafe-perm node-red
```

### 2. Install Emotiv BCI Node

Navigate to the Node-RED user directory:

- **Windows:** `cd %USERPROFILE%\.node-red`
- **macOS/Linux:** `cd ~/.node-red`

Install the node:
```bash
npm install node-red-contrib-emotiv-bci
```

### 3. Start Node-RED

```bash
node-red
```
Visit [http://127.0.0.1:1880/](http://127.0.0.1:1880/) in your browser.

### 4. Install LIFX Light Control Node

In Node-RED:
- Go to **Manage Palette** → **Install**
- Search for: `node-red-contrib-lifx-api`
- Click **Install**

### 5. Import the Pre-Built Flow

- In Node-RED, click **Menu** (☰) → **Import**
- Click **select a file to import**
- Browse to and select `SmartLightLifxBCI/Emotiv_Smart_Light_LIFX_BCI.json`
- Click **Open**, then confirm the import

### 6. Configure Cortex Credentials

Edit your credentials in:

- **macOS/Linux:** `~/.node-red/node_modules/node-red-contrib-emotiv-bci/emotiv-bci/bci-config.js`
- **Windows:** `C:\Users\<YourUsername>\.node-red\node_modules\node-red-contrib-emotiv-bci\emotiv-bci\bci-config.js`

Add your **Client ID** and **Client Secret**.

### 7. Set Your Trained Profile Name

- Double-click the `Profile Name` node in Node-RED.
- Enter the exact name of your training profile.
- Click **Done**.

---

## Troubleshooting

- **Connection Issues:** Ensure the Cortex service is running and you are logged in via the EMOTIV Launcher.
- **No command detected:** Retrain your profile in EmotivBCI and ensure the selected action(s) are active and accurate.
- **Node-RED errors:** Make sure Node-RED and all dependencies are correctly installed.

## Resources

- [Cortex API Data Subscription Documentation](https://emotiv.gitbook.io/cortex-api/data-subscription)
- [EMOTIV Developer Portal](https://www.emotiv.com/developer/)
- [YouTube Tutorial](https://www.youtube.com/watch?v=vdgzOriqC9Y&ab_channel=EmotivAcademy)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

If you need help, please consult the [EMOTIV support site](https://www.emotiv.com/pages/contact) or open a GitHub issue.
