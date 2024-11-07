Developed in Collaboration with the Imagination Center at the Glenrose Rehabilitation Hospital. https://www.imagination-centre.ca/

# Brain Computer Interface Controlled DJI RoboMaster

You can see the step-by-step tutorial here: https://www.youtube.com/watch?v=9G00Tl1ymNI.

## Requirement
- This example works with Python >= 3.7
- Install websocket client via  `pip install websocket-client`
- Install python-dispatch via `pip install python-dispatch`

## Before you start

To run the existing example you will need to do a few things.

1. You will need an EMOTIV headset.  You can purchase a headset in our [online
   store](https://www.emotiv.com/)
2. Next, [download and install](https://www.emotiv.com/developer/) the Cortex
   service.  Please note that currently, the Cortex service is only available
   for Windows and macOS.
3. We have updated our Terms of Use, Privacy Policy and EULA to comply with
   GDPR. Please login via the EMOTIV Launcher to read and accept our latest policies
   in order to proceed using the following examples.
4. Next, to get a client id and a client secret, you must connect to your
   Emotiv account on
   [emotiv.com](https://www.emotiv.com/my-account/cortex-apps/) and create a
   Cortex app. If you don't have a EmotivID, you can [register
   here](https://id.emotivcloud.com/eoidc/account/registration/).
5. Then, if you have not already, you will need to login with your Emotiv id in
   the EMOTIV Launcher.
6. Finally, the first time you run these examples, you also need to authorize
   them in the EMOTIV Launcher.

## Cortex Library
- [`cortex.py`](./cortex.py) - the wrapper lib around EMOTIV Cortex API.

## Main
- [`main.py`](./main.py)
- Fill in your Cortex client secret, client ID and trained profile name from EmotivBCI to get started.

## Susbcribe Data
- [`live_advance.py`](./live_advance.py) shows data streaming from Cortex: EEG, motion, band power and Performance Metrics.
- For more details https://emotiv.gitbook.io/cortex-api/data-subscription


