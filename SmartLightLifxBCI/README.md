# Smart Light Control with Emotiv BCI and Node-RED

Control a **LIFX smart light** using only your thoughts, powered by an **Emotiv EEG headset** and **Node-RED**. This brain-computer interface (BCI) project demonstrates how mental commands can directly influence smart home devices.

## Overview
- Use an **Emotiv headset**
- Captures mental commands like *Push*, *Pull*
- Integrates with **Node-RED** to process brain data
- Sends real-time control signals to **LIFX smart bulbs**

## Video Tutorial
🎥 Follow the official step-by-step guide on **Emotiv Academy YouTube**:
[Smart Light Control with BCI](https://www.youtube.com/watch?v=vdgzOriqC9Y&ab_channel=EmotivAcademy)

## Requirements
- Emotiv Cortex running on your computer
- Emotiv Insight, EpocX, or MN8 headset
- LIFX smart light connected to the same network
- Node-RED installed and configured

## Before You Start

To run the existing example, you will need to complete the following steps:

1. You will need an EMOTIV headset. You can purchase a headset in our [online store](https://www.emotiv.com/)
2. Next, [download and install](https://www.emotiv.com/developer/) the Cortex service. Note that Cortex is available for Windows and macOS.
3. We have updated our Terms of Use, Privacy Policy and EULA to comply with GDPR. Please login via the EMOTIV Launcher to read and accept our latest policies.
4. To get a Client ID and Client Secret, log in to your Emotiv account at [emotiv.com](https://www.emotiv.com/my-account/cortex-apps/) and create a Cortex app. If you don't have an EmotivID, [register here](https://id.emotivcloud.com/eoidc/account/registration/).
5. Make sure you are logged in with your Emotiv ID in the EMOTIV Launcher.
6. Open the EmotivBCI application and create a training profile with your headset. Train at least one Mental Command and ensure it reaches a usable accuracy.
7. The first time you run these examples, authorize them through the EMOTIV Launcher.

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
Before installing, navigate to the Node-RED user directory:

**On Windows:**
```bash
cd %USERPROFILE%\.node-red
```
**On macOS/Linux:**
```bash
cd ~/.node-red
```
Then install:
```bash
npm install node-red-contrib-emotiv-bci
```

### 3. Start Node-RED (first time)
```bash
node-red
```
Open your browser and go to: [http://127.0.0.1:1880/](http://127.0.0.1:1880/)

### 4. Install LIFX Light Control Node
In Node-RED:
- Go to **Manage Palette** → **Install**
- Search for: `node-red-contrib-lifx-api`
- Click **Install**

### 5. Connect Your Flow
- Import the pre-built flow from the project folder:
  - In Node-RED, click **Menu** (☰) → **Import**
  - Click the **select a file to import** button
  - Browse to and select the file: `SmartLightLifxBCI/Emotiv_Smart_Light_LIFX_BCI.json`
  - Click **Open**, then confirm the import to load the flow into your workspace

### 6. Configure Client ID and Secret
After installing the Emotiv BCI node, open the following file:

```bash
~/.node-red/node_modules/node-red-contrib-emotiv-bci/emotiv-bci/bci-config.js
```
*(On Windows: `C:\Users\<YourUsername>\.node-red\node_modules\node-red-contrib-emotiv-bci\emotiv-bci\bci-config.js`)*

Then add your **Client ID** and **Client Secret** into the appropriate fields inside that file.

### 7. Set Your Trained Profile Name

Before running the flow, double-click the `Profile Name` node in your imported Node-RED flow.

- Enter the exact name of the training profile you created in the EmotivBCI application.
- Click **Done** to save the node configuration.

This ensures that the flow will load and use your trained mental command profile correctly.
