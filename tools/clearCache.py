import os
import shutil

# this file is to clean the cache and also the built js and css

shutil.rmtree(os.path.join("__pycache__"))
shutil.rmtree(os.path.join("models/__pycache__"))
shutil.rmtree(os.path.join("routes/__pycache__"))
shutil.rmtree(os.path.join("tools/__pycache__"))
shutil.rmtree(os.path.join("static/scss"))
shutil.rmtree(os.path.join("static/typescript"))
os.remove("static/index.js")
os.remove("static/index.js.map")

if os.path.isdir("__migration__"):
    shutil.rmtree(os.path.join("migrations/__pycache__"))