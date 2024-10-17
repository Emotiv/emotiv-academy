import json

def save_config(settings):
    config = {}
    config["push"] = settings[0]
    config["pull"] = settings[1]
    config["left"] = settings[2]
    config["right"] = settings[3]
    json.dump(config, open("config.json", "w"), indent=4, sort_keys=False)