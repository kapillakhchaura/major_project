import os

working_dir = os.path.dirname(os.path.abspath(__file__))

REPORTS_DIR = os.path.join(working_dir, "reports")
INDEX_PATH = os.path.join(REPORTS_DIR, "index.json")
USERS_PATH = os.path.join(working_dir, "users.json")
SAVED_MODELS_DIR = os.path.join(working_dir, "saved_models")

DEFAULT_ADMIN = {"username": "admin", "password": "adminpass"}

os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(SAVED_MODELS_DIR, exist_ok=True)
