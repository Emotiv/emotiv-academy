# Brain-Computer Interface Controlled Spotify Player

Developed by Emotiv Academy.  
Control Spotify playback—pause and resume music—using your brain with an Emotiv EEG headset.

## Overview

This project enables real-time Spotify playback control using mental commands or facial expressions detected by the Emotiv headset. The system maps "push" or "clench" to pause, and "pull" or "smile" to resume music. It uses a lightweight Flask server, integrates with the Spotify Web API, and provides visual feedback for command recognition.

A step-by-step tutorial video is available [here](https://www.youtube.com/watch?v=-mUKNqEfIxo).

## Features

- **Spotify Web API integration**: Play/pause music with your brain.
- **Real-time BCI control**: Use mental commands or facial expressions for hands-free operation.
- **Live feedback UI**: Visual debug interface shows detected commands (optional).
- **Educational Codebase**: Simple Python + Flask code, ideal for learning BCI-Web API integration.
- **Cortex API integration**: Robust connection for EEG streaming and command detection.
- **Customizable mapping**: Easily change which commands trigger which Spotify actions.

## Requirements

- Python 3.8+ (recommended: Python 3.9)
- Emotiv headset ([purchase here](https://www.emotiv.com/))
- [Cortex Service](https://www.emotiv.com/developer/) (Windows/macOS only)
- Flask: `pip install flask`
- requests: `pip install requests`
- websocket-client: `pip install websocket-client`
- python-dispatch: `pip install python-dispatch`

## Getting Started

1. **Clone this repository:**
    ```bash
    git clone https://github.com/Emotiv/emotiv-academy.git
    cd emotiv-academy/Spotify_BCI
    ```

2. **Install dependencies:**
    ```bash
    pip install flask requests websocket-client python-dispatch
    ```

3. **Create applications:**
    - **Spotify App**: [Create one here](https://developer.spotify.com/dashboard) and note your client ID/secret.
    - **Emotiv Cortex App**: [Register here](https://account.emotiv.com/my-account/cortex-apps/).

4. **Setup hardware and software:**
    - Get an Emotiv headset.
    - Download and install Cortex service.
    - Log in and accept EMOTIV policies via the Launcher.
    - Train "push" and "pull" (or facial expressions) in EmotivBCI until accuracy is sufficient.

5. **Configure credentials:**
    - Open `spotify_bci.py` and enter your Spotify and Emotiv app credentials:
      ```python
      spotify_client_id = 'your-spotify-client-id'
      spotify_client_secret = 'your-spotify-client-secret'
      emotiv_app_client_id = 'your-emotiv-client-id'
      emotiv_app_client_secret = 'your-emotiv-client-secret'
      profile_name_load = 'your-trained-profile-name'
      ```
    - *Note: Make sure this trained profile was created using the same headset you intend to connect.*

6. **(Optional) Specify which headset to connect:**
    In `spotify_bci.py`, set the headset ID if you want to target a specific device.
    Leave it empty (`''`) to auto-connect to the first available headset.
    ```python
    headset_Id = ''
    ```

7. **Run the app:**
    ```bash
    python spotify_bci.py
    ```

8. **Open in your browser and authorize:**
    ```
    http://127.0.0.1:5000
    ```
    Click **Login with Spotify** and authorize access.

## Project Structure

- `spotify_bci.py`: Main application entry point.
- `cortex.py`: Cortex API wrapper for EEG data and command recognition.
- `templates/`: (If present) Flask HTML templates for visual feedback.

## Troubleshooting

- **Connection issues:** Ensure Cortex service is running and you are logged in via the EMOTIV Launcher.
- **No command detected:** Retrain your profile in EmotivBCI for better accuracy.
- **Spotify login problems:** Double-check your Spotify app credentials and redirect URIs.

## Resources

- [Cortex API Data Subscription Documentation](https://emotiv.gitbook.io/cortex-api/data-subscription)
- [EMOTIV Developer Portal](https://www.emotiv.com/developer/)
- [YouTube Tutorial](https://www.youtube.com/watch?v=-mUKNqEfIxo)

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

If you need additional help, consult the [EMOTIV support site](https://www.emotiv.com/pages/contact) or open a GitHub issue.
