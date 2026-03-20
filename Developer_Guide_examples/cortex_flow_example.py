# pip install websocket-client
import json, ssl
from websocket import create_connection
URL = "wss://localhost:6868"

# Your credentials
CLIENT_ID = "paste your cliendId here"
CLIENT_SECRET = "paste your clientSecret here"
def main():
    # Use Emotiv Root CA (adjust the path if needed)
    sslopt = {"cert_reqs": ssl.CERT_REQUIRED, "ca_certs": "rootCA.pem"}
    ws = create_connection(URL, sslopt=sslopt, timeout=30)
    
    
    # --- Step 1: requestAccess (safe even if already granted) ---
    ws.send(json.dumps({
        "id": 1, "jsonrpc": "2.0", "method": "requestAccess",
        "params": { "clientId": CLIENT_ID, "clientSecret": CLIENT_SECRET}
    }))
    print("requestAccess →")
    print(json.dumps(json.loads(ws.recv()), indent=2))


    # --- Step 2: refresh device list ---
    ws.send(json.dumps({
        "id": 2,"jsonrpc": "2.0","method": "controlDevice",
        "params": {"command": "refresh"}
    }))
    print("controlDevice (refresh) →")
    print(json.dumps(json.loads(ws.recv()), indent=2))

    #wait for the headset to be connected before proceeding (listen for warning code 104)
    refresh_device_is_finished = False
    while not refresh_device_is_finished:
        print("Waiting for device refresh to complete...")
        msg = ws.recv()  # blocks until data arrives
        data = json.loads(msg)

        print(f"Raw message → {data}")
        warning = data.get("warning")

        if warning and warning.get("code") == 142:
            print("Device refresh completed.")
            refresh_device_is_finished = True


    # --- Step 3: queryHeadsets ---
    ws.send(json.dumps({
        "id": 3,"jsonrpc": "2.0","method": "queryHeadsets"
    }))

    resp4 = json.loads(ws.recv())
    print("queryHeadsets →")
    print(json.dumps(resp4, indent=2))
    headsets = resp4.get("result", [])

    if not headsets:
        print("\nNo headsets found. Turn one on or start a virtual headset in Launcher.")
        ws.close()
        return

    #select the first headset found (you can add logic to select a specific one if needed)
    hs = headsets[0]

    #get headset id and status for later use
    headset_id = hs.get("id")
    status = hs.get("status")
    print(f"\nUsing headset: {headset_id} (status: {status})")

    # --- Step 4: connect if needed ---
    #connect to the headset if it's not already connected (required for real headsets, virtual headsets may already be connected)
    if status != "connected":
        ws.send(json.dumps({
            "id": 4, "jsonrpc": "2.0", "method": "controlDevice",
            "params": {
                "command": "connect","headset": headset_id }
        }))
        print("controlDevice (connect) →")
        print(json.dumps(json.loads(ws.recv()), indent=2))

        device_connection_established = False
        while not device_connection_established:
            msg = ws.recv()  # blocks until data arrives
            if not msg:
                break
            data = json.loads(msg)
            #print(f"Raw message → {data}")
            warning = data.get("warning")
            if warning and warning.get("code") == 104:
                print("Headset is now connected.")
                device_connection_established = True
   

    # --- Step 5: authorize (get cortexToken) ---
    cortex_token_request_id = 5
    token_received = False

    ws.send(json.dumps({
        "id": cortex_token_request_id,
        "jsonrpc": "2.0",
        "method": "authorize",
        "params": {
            "clientId": CLIENT_ID,
            "clientSecret": CLIENT_SECRET
        }
    }))

    try:
        while token_received == False:
            msg = ws.recv()  # blocks until data arrives
            if not msg:
                break
            data = json.loads(msg)

            if data.get("id") == cortex_token_request_id:
                cortex_token = data.get("result", {}).get("cortexToken")
                token_received = True

                if not cortex_token:
                    print("\nNo cortexToken found (check approval/EULA in Launcher).")
                    ws.close()
                    return
    finally:                 
                print("Application authorized (token received).")


    # --- Step 6: create ACTIVE session (needed for full features) ---
    ws.send(json.dumps({
        "id": 6,
        "jsonrpc": "2.0",
        "method": "createSession",
        "params": {
            "cortexToken": cortex_token,
            "headset": headset_id,
            "status": "active"
        }
    }))

    resp7 = json.loads(ws.recv())

    print("createSession →")
    print(json.dumps(resp7, indent=2))

    #get the session id from the response (needed for data subscriptions)
    session_id = resp7.get("result", {}).get("id")

    if not session_id:
        print("\nNo session id returned.")
        ws.close()
        return

    print(f"\nSession ready: {session_id}")

    # --- Step 7: subscribe to performance metrics ---
    print("\nSubscribing to performance metrics (met)…")

    ws.send(json.dumps({
        "id": 7,
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "cortexToken": cortex_token,
            "session": session_id,
            "streams": ["met"]
        }
    }))

    subscribe_response = json.loads(ws.recv())
    print("subscribe (met) →")
    print(json.dumps(subscribe_response, indent=2))

    # Capture the column names returned in the subscription response.
    # We will use this to know exactly what metrics the current device provides.
    met_labels = []
    try:
        success = subscribe_response.get("result", {}).get("success", [])
        for stream in success:
            if stream.get("streamName") == "met":
                met_labels = stream.get("cols", [])
    except Exception:
        pass

    print("\nStreaming MET data. Press Ctrl+C to stop.\n")

    # --- RUN UNTIL USER PRESSES Ctrl+C ---
    try:
        while True:
            msg = ws.recv()  # blocks until data arrives
            if not msg:
                break

            data = json.loads(msg)
            #print(f"Raw message → {data}")

            if "sid" in data and "met" in data:
                t = data.get("time", "n/a")

                # Dynamically construct the output using the labels we received from Cortex.
                # This works automatically for any device, no matter what metrics it sends.
                if met_labels:
                    output_parts = []
                    
                    # Loop through each label and its corresponding value
                    for i in range(len(met_labels)):
                        label = met_labels[i]
                        val = data["met"][i]
                        
                        # Format the value properly
                        if ".isActive" in label or isinstance(val, bool):
                            # Boolean flags
                            formatted_val = str(bool(val))
                        elif isinstance(val, (int, float)):
                            # Numbers formatted to 2 decimal places
                            formatted_val = f"{val:.2f}"
                        else:
                            # Anything else
                            formatted_val = str(val)
                            
                        # Add to our list of output strings
                        output_parts.append(f"{label}: {formatted_val}")
                        
                    metrics_str = ", ".join(output_parts)
                    print(f"MET @ {t} → {metrics_str}")
                else:
                    # Fallback in case labels weren't captured correctly
                    print(f"MET @ {t} → raw data: {data['met']}")

    except KeyboardInterrupt:
        print("\n\nStopping (Ctrl+C)…")

    # --- Clean up: close the session ---
    print("Closing session…")

    ws.send(json.dumps({
        "id": 9,"jsonrpc": "2.0","method": "updateSession",
        "params": {
            "cortexToken": cortex_token, "session": session_id, "status": "close"}
    }))

    print(json.dumps(json.loads(ws.recv()), indent=2))
    ws.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()