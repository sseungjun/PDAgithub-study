import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
token_path = os.path.join(BASE_DIR, 'config', 'token.json')

with open(token_path, 'r') as f:
    cfg = json.load(f)

print(f"🔑 Your API token is: {cfg['API_TOKEN']}")
