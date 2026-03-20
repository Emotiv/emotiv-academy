# Emotiv Cortex API Developer Guide Examples

This directory contains introductory Python examples demonstrating how to communicate with the Emotiv Cortex API via WebSockets. It illustrates both basic communication and the full authentication and data subscription flow required to get brain data from an Emotiv headset.

## Project Requirements

To run these examples, you need:

- **Python 3** installed on your system.
- Dependencies: `websocket-client` and `python-dispatch` (installable via pip).
- **Emotiv Launcher** installed with the Cortex Service running in the background.
- An **Emotiv Headset** (either a physical headset connected via Bluetooth/Dongle, or a virtual headset started in the Emotiv Launcher).
- `CLIENT_ID` and `CLIENT_SECRET`: Your Cortex API credentials obtained from your Emotiv account (required for the advanced flow).
- `rootCA.pem`: The Emotiv root certificate for secure WSS connections (already included in this directory).

## What the Code Does

This folder provides two progressive examples:

### 1. `cortex-get-cortex-info.py`
This is a basic introductory script that tests your connection to the Cortex Service. It:
- Establishes a secure WebSocket connection (WSS) to the local Cortex API using the provided `rootCA.pem`.
- Sends a simple, unauthenticated `getCortexInfo` JSON-RPC request.
- Receives and prints the response containing Cortex version details and exits.

### 2. `cortex_flow_example.py`
This is a comprehensive script demonstrating the end-to-end data subscription workflow:
- **requestAccess**: Sends credentials to gain access.
- **controlDevice**: Refreshes the device list.
- **queryHeadsets**: Finds available connected physical or virtual headsets.
- **connect**: Connects to the device if not already connected.
- **authorize**: Uses your client ID and secret to obtain a securely scoped `cortexToken`.
- **createSession**: Starts an active data session for the connected headset.
- **subscribe**: Subscribes to the `met` (mental performance metrics) stream.
- Continuously receives, formats, and prints the performance metrics backwards to the console in real-time until you stop the script (`Ctrl+C`).

## How to Run It

1. **Install Python Dependencies:**
   Open your terminal in this directory and run:
   ```bash
   pip install websocket-client python-dispatch
   ```

2. **Prepare the Emotiv Environment:**
   - Open Emotiv Launcher and ensure you are logged in.
   - Turn on your physical headset or start a virtual headset from the Launcher.

3. **Provide Your Credentials (For the Flow Example):**
   - Open `cortex_flow_example.py` in your text editor.
   - Replace the `CLIENT_ID` and `CLIENT_SECRET` variables at the top of the file with your actual Cortex API credentials.

4. **Run the Scripts:**
   Run the basic info check first to ensure your connection is working:
   ```bash
   python cortex-get-cortex-info.py
   ```
   
   If that succeeds, run the full authentication and streaming flow:
   ```bash
   python cortex_flow_example.py
   ```
   Press `Ctrl+C` in the terminal when you stop the data stream.
