import os
import json

DATA_FILE = "data.json"

def load_all_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_all_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def save_data(username, encrypted_message):
    data = load_all_data()
    data[username] = encrypted_message
    save_all_data(data)

def load_data(username):
    data = load_all_data()
    return data.get(username, None)
