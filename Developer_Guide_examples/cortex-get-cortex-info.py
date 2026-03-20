# pip install websocket-client
# pip install python-dispatch

import json
import ssl
from websocket import create_connection

CORTEX_URL = "wss://localhost:6868"
ROOT_CA_FILE = "rootCA.pem"

GET_CORTEX_INFO_REQUEST = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getCortexInfo"
}

def main():
    ssl_options = {
        "cert_reqs": ssl.CERT_REQUIRED,
        "ca_certs": "rootCA.pem"
    }

    websocket_connection = None

    try:
        # Open secure WebSocket connection to Cortex
        websocket_connection = create_connection(
            CORTEX_URL,
            sslopt=ssl_options,
            timeout=60
        )

        # Send JSON-RPC request
        request_json = json.dumps(GET_CORTEX_INFO_REQUEST)
        websocket_connection.send(request_json)

        # Receive a single response
        response_message = websocket_connection.recv()
        response_data = json.loads(response_message)

        print("Cortex response:")
        print(json.dumps(response_data))  # simple, no pretty printing

    except Exception as error:
        print("Failed to connect to Cortex or process the response:")
        print(error)

    finally:
        if websocket_connection is not None:
            websocket_connection.close()

if __name__ == "__main__":
    main()