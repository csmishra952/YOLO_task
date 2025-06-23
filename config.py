
import os

# Base dataset path
BASE = '/content/dataset'
IMG = os.path.join(BASE, 'images')
LBL = os.path.join(BASE, 'labels')

# Create folders if they don't exist
for d in (BASE, IMG, LBL):
    os.makedirs(d, exist_ok=True)
