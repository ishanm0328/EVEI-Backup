import json
import os.path

CONF_FILE='config.json'

def get_config():
    if path.exists(CONF_FILE):
        with open(CONF_FILE, 'r') as file:
            return json.load(file)
    else:
        return set_default_config()

def get_default_config():
    config = {}
    config['follow'] = False
    config['play'] = False
    config['steering'] = {}
    config['steering']['min'] = 0.0
    config['steering']['max'] = 5.0
    config['steering']['channel'] = 'a'
    config['throttle'] = {}
    config['throttle']['min'] = 0.0
    config['throttle']['max'] = 5.0
    config['throttle']['channel'] = 'b'
    config['serial'] = {}
    config['serial']['baud'] = 9600
    return config    

def save_config(config):
    with open(CONF_FILE, 'w') as file:
        json.dump(config, file)
