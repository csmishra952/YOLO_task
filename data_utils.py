
import os
import shutil
from pathlib import Path

def setup_directories(base='/content/dataset'):
    img = os.path.join(base, 'images')
    lbl = os.path.join(base, 'labels')
    for d in (base, img, lbl):
        os.makedirs(d, exist_ok=True)
    return base, img, lbl
