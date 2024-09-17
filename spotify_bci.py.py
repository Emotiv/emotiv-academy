from cortex import Cortex

import requests
import urllib.parse

from flask import Flask, redirect, request, jsonify, session

'''
Play Spotify based on push mental command. Same as spotify_com_main.py except extra code is removed for demo.

Store authorization token as a global variable.

Inputs to Update:
    -the function called (play or pause) in the mental command function
    -"your_app_client_id" and "your_app_client_secret": Emotiv
    -"CLIENT_ID" and "CLIENT_SECRET": Spotify
'''

app = Flask(__name__) #initialize flask app
app.secret_key = '47839wnf89w4uqjpdku4cw8ucrj' #set secret key for app (arbitrary string). Space to keep access token, etc.


#Setting up constants for Spotify

CLIENT_ID = 'b531f85e65da4a7aaf9969e3f6b3eb28' #for spotify
CLIENT_SECRET = '0c68f77f5bf94c78bd493f80f220f54e'#for spotify
REDIRECT_URI = 'http://localhost:5000/callback' #set in the spotify app

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

loaded_profile = False #global var to set the load profile to only occur once

def run_emotiv():
    # Please fill your emotiv application clientId and clientSecret before running script
    your_app_client_id = 'uWcRTis7kBUmfLQb4kTuRkyS501M7HqyLzR0OXn2'
    your_app_client_secret = 'J9Xw3I7oireD39shQBJ8y9WJHSJHw2BQZm9whnByFifuj2HgnQm5jX6HkcIeHVkhYqHYW8F2JfoOB51nuZ333d6GacsGg0ZhYdDWzCktvh2twUz8wnByfOoo2LOPbjNd'

    s = Subscribe(your_app_client_id, your_app_client_secret)
    streams = ['com']
    s.start(streams)

#Welcome site that will then redirect to spotify

@app.route('/') #decorator that says this function should be called when user accesses route of application http://localhost:5000/
def index():
    #display message and go to login when clicked
    return "Welcome to Spotify BCI Control <a href='/login'>Login with Spotify</a>"

#Creating login endpoint to redirect to spotify login page

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-modify-playback-state user-read-playback-state' #scopes we need for permission

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI, #where it will direct to on login
        'show_dialog': True #if False (make False after debugging), even if we make request here then it assumes we don't need to login again. We want to force user to login to debug easier

    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}" #encode params with urllib

    return redirect(auth_url)


#Callback endpoint for Spotify user to come back to once they login to Spotify. Account for success and error

@app.route('/callback')
def callback():
    #check if Spotify gave us an error (defensive proramming)
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    #will give back code parameter if successful. We need to send code to get access token
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        #send request body to spotify
        response = requests.post(TOKEN_URL, data=req_body) #we want to send request body to the token url to get the access token. Response is the output
        token_info = response.json()

        global access_token_global #global variable so that we can still access after going to cortex
        access_token_global = token_info['access_token']

        run_emotiv() #enter client ID and client secret and run Subscribe function to get mental command outputs
        return redirect('/')
    
@app.route('/pause')
def pause():
    print('STARTING SPOTIFY PAUSE')
    
    headers = {
        'Authorization': f"Bearer {access_token_global}"
    }

    # Replace this with your specific device ID if "no device found" error. 
    #Instructions to Get Device Id: 1. uncomment the "devices" function 2. Set endpoint of "callback" to "devices"
    # device_id = 'YOUR_DEVICE_ID' # e.g., 6126575f618c948dcfd13e9431f84e37ae4f2157
    # url = f"{API_BASE_URL}me/player/play?device_id={device_id}"

    url = f"{API_BASE_URL}me/player/pause"

    response = requests.put(url, headers=headers) #play takes a PUT request

    # Check if the response was successful
    if response.status_code == 200:
        return "Playback paused successfully!"
    
    else:
        # Return the error details from Spotify
        pause = response.json()
        return jsonify(pause), response.status_code

@app.route('/play')
def play():

    print('STARTING SPOTIFY PLAY')

    #play music
    headers = {
        'Authorization': f"Bearer {access_token_global}"
    }

    # Replace this with your specific device ID if "no device found" error. 
    #Instructions to Get Device Id: 1. uncomment the "devices" function 2. Set endpoint of "callback" to "devices"
    # device_id = 'YOUR_DEVICE_ID' # e.g., 6126575f618c948dcfd13e9431f84e37ae4f2157
    # url = f"{API_BASE_URL}me/player/play?device_id={device_id}"

    url = f"{API_BASE_URL}me/player/play"

    response = requests.put(url, headers=headers) #play takes a PUT request

    # Check if the response was successful
    if response.status_code == 200:
        return "Playback started successfully!"
    
    else:
        # Return the error details from Spotify
        play = response.json()
        return jsonify(play), response.status_code
    
@app.route('/devices')
def devices():
    if 'access_token' not in session:
        return redirect('/login')
    
    headers = {
        'Authorization': f'Bearer {session["access_token"]}'
    }
    
    response = requests.get(API_BASE_URL + 'me/player/devices', headers=headers)
    devices = response.json()
    
    return jsonify(devices)

    
class Subscribe():
    """
    A class to subscribe data stream.

    Attributes
    ----------
    c : Cortex
        Cortex communicate with Emotiv Cortex Service

    Methods
    -------
    start():
        start data subscribing process.
    sub(streams):
        To subscribe to one or more data streams.
    on_new_data_labels(*args, **kwargs):
        To handle data labels of subscribed data 
        To handle mental command emitted from Cortex
    """
    def __init__(self, app_client_id, app_client_secret, **kwargs):
        """
        Constructs cortex client and bind a function to handle subscribed data streams
        If you do not want to log request and response message , set debug_mode = False. The default is True
        """
        print("Subscribe __init__")
        self.c = Cortex(app_client_id, app_client_secret, debug_mode=False, **kwargs)

        #associate events from Cortex with handler functions in class
        self.c.bind(create_session_done=self.on_create_session_done)
        self.c.bind(new_data_labels=self.on_new_data_labels)
        self.c.bind(new_com_data=self.on_new_com_data) #added
        self.c.bind(inform_error=self.on_inform_error)

    def start(self, streams, headsetId=''):
        """
        To start data subscribing process as below workflow
        (1)check access right -> authorize -> connect headset->create session
        (2) subscribe streams data

        'com' : Mental Command

    
        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']
        headsetId: string , optional
             id of wanted headet which you want to work with it.
             If the headsetId is empty, the first headset in list will be set as wanted headset
        Returns
        -------
        None
        """

        self.streams = streams

        if headsetId != '':
            self.c.set_wanted_headset(headsetId)

        self.c.open()

    def sub(self, streams):
        """
        To subscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power
        'com' : Mental Command

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot', 'com']

        Returns
        -------
        None
        """
        self.c.sub_request(streams)

    def unsub(self, streams):
        """
        To unsubscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']

        Returns
        -------
        None
        """
        self.c.unsub_request(streams)

    def on_new_data_labels(self, *args, **kwargs):
        """
        To handle data labels of subscribed data 
        Returns
        -------
        data: list  
              array of data labels
        name: stream name
        For example:
            eeg: ["COUNTER","INTERPOLATED", "AF3", "T7", "Pz", "T8", "AF4", "RAW_CQ", "MARKER_HARDWARE"]
            motion: ['COUNTER_MEMS', 'INTERPOLATED_MEMS', 'Q0', 'Q1', 'Q2', 'Q3', 'ACCX', 'ACCY', 'ACCZ', 'MAGX', 'MAGY', 'MAGZ']
            dev: ['AF3', 'T7', 'Pz', 'T8', 'AF4', 'OVERALL']
            met : ['eng.isActive', 'eng', 'exc.isActive', 'exc', 'lex', 'str.isActive', 'str', 'rel.isActive', 'rel', 'int.isActive', 'int', 'foc.isActive', 'foc']
            pow: ['AF3/theta', 'AF3/alpha', 'AF3/betaL', 'AF3/betaH', 'AF3/gamma', 'T7/theta', 'T7/alpha', 'T7/betaL', 'T7/betaH', 'T7/gamma', 'Pz/theta', 'Pz/alpha', 'Pz/betaL', 'Pz/betaH', 'Pz/gamma', 'T8/theta', 'T8/alpha', 'T8/betaL', 'T8/betaH', 'T8/gamma', 'AF4/theta', 'AF4/alpha', 'AF4/betaL', 'AF4/betaH', 'AF4/gamma']
        """
        data = kwargs.get('data')
        stream_name = data['streamName']
        stream_labels = data['labels']
        # print('{} labels are : {}'.format(stream_name, stream_labels))


    def on_new_com_data(self, *args, **kwargs):
        """
        To handle mental command data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array pow match the labels in the array labels return at on_new_com_data_labels
        """

        global loaded_profile

        if loaded_profile == False:

            status_load = "load"
            profile_name_load = 'SpotifyDemo' #Enter the profile name you want to use from EmotivBCI (train this profile first with a mental command!)

            self.profile_name = profile_name_load
            self.c.set_wanted_profile(profile_name_load)

            self.c.setup_profile(profile_name_load, status_load)

            loaded_profile = True

        # self.c.get_current_profile()

        actions = ['push'] #add more mental commands here if you want to add additional functionality
        self.c.set_mental_command_active_action(actions)
        data = kwargs.get('data')

        action = data.get('action') #accesing the action key in the incoming dictionary 
        power = data.get('power')
        time = data.get('time')

        # Print the command data
        print(f'Command Data - Action: {action}, Power: {power}, Time: {time}')

        if action == 'push' and power > 0.6: #you can adjust the threshold based on how easy/diffifult it is to activate the push command
            # Turn on play function in spotify
            with app.test_request_context():
                pause()


    # callbacks functions
    def on_create_session_done(self, *args, **kwargs):
        print('on_create_session_done')

        # subribe data 
        self.sub(self.streams)

    def on_inform_error(self, *args, **kwargs):
        error_data = kwargs.get('error_data')
        print(error_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) #Run Flask App