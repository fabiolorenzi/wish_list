import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, "/var/www/wish-list")
project_folder = os.path.expanduser("/var/www/wish-list")
load_dotenv(os.path.join(project_folder, ".env"))


activate_this = "/var/www/wish-list/venv/bin/activate_this.py"
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

from app import app as application