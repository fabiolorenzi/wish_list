import os
import shutil

shutil.rmtree(os.path.join("__pycache__"))
shutil.rmtree(os.path.join("models/__pycache__"))
shutil.rmtree(os.path.join("routes/__pycache__"))
shutil.rmtree(os.path.join("tools/__pycache__"))

if os.path.isdir("__migration__"):
    shutil.rmtree(os.path.join("migrations/__pycache__"))