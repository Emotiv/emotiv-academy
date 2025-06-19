## Spotify BCI

Control Spotify playback **using your brain** with Emotiv's EEG headset. This project enables pause/resume of music via trained mental commands or facial expressions (e.g., clench or smile).

---

### 🎧 Overview

- **EEG Devices Supported**: [Emotiv Insight / EpocX / MN8 / etc.](https://www.emotiv.com/pages/emotiv-insight-leading-mind-control-bci-technology-b)
- **Backend**: Python + Flask
- **Spotify Integration**: Web API authentication and playback control
- **Control Options**: Mental commands & facial expressions (e.g., 'push', 'pull', 'clench', 'smile')
- **Command Mapping**: Push/clench = Pause, Pull/smile = Resume
- **Live mental command feedback** (optional)

---

### 📺 Tutorial

Watch the step-by-step video guide on Emotiv Academy's YouTube:
[![Watch here](https://www.youtube.com/watch?v=-mUKNqEfIxo)](https://www.youtube.com/watch?v=-mUKNqEfIxo&ab_channel=EmotivAcademy)

---

### 🚀 Features

- Control Spotify playback with mental commands or facial expressions
- Lightweight Flask server for easy local control
- Visual debug interface for real-time command feedback (optional)
- Simple, educational integration of Emotiv BCI with a popular web API

---

### 🛠️ Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/Emotiv/emotiv-academy.git
cd emotiv-academy
```

#### 2. Install Dependencies
```bash
pip install flask requests websocket-client python-dispatch
```

#### 3. Create Applications

- **Spotify App**: via [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

#### 4. Before You Start

- Get an [Emotiv headset](https://www.emotiv.com/)
- [Download and install Cortex service](https://www.emotiv.com/developer/) (Windows/macOS only)
- Accept EMOTIV policies via EMOTIV Launcher
- Login to EMOTIV Launcher
- Open **EmotivBCI** app, create a profile, train **both** "push" and "pull" Mental Command actions until they reach usable accuracy
- Authorize this project in the Launcher

#### 5. Fill in Your Credentials in `spotify_bci.py`
```python
spotify_client_id = 'your-spotify-client-id'
spotify_client_secret = 'your-spotify-client-secret'
emotiv_app_client_id = 'your-emotiv-client-id'
emotiv_app_client_secret = 'your-emotiv-client-secret'
profile_name_load = 'your-trained-profile-name'
```

#### 6. Run the App
```bash
python spotify_bci.py
```

#### 7. Open in Browser
```
http://127.0.0.1:5000
```
Click **Login with Spotify** and authorize access.

---

### 📦 Dependencies

- Python >= 3.8 (Recommended: 3.9)
- Flask
- requests
- websocket-client
- python-dispatch
- Emotiv Cortex SDK (ensure `cortex.py` is in the same directory)

---

### ⚠️ Notes

- Requires trained EmotivBCI profile with usable accuracy for "push" and "pull"
- You can choose mental (`com`) or facial expression (`fac`) mode in the code
