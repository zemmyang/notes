"""
Copy files from source to destination and check
"""

import hashlib
from glob import glob
from tqdm import tqdm
import shutil

SOURCE_DIR = r'D:\FOLDER'
DEST_DIR = r"C:\DESTINATION"

SOURCE_LIST = glob(f"{SOURCE_DIR}/*")

print("Copying files")

for s in tqdm(SOURCE_LIST):
    shutil.copy2(s, DEST_DIR)

DEST_LIST = glob(f"{DEST_DIR}/*")

print("Number of files match:", len(SOURCE_LIST) == len(DEST_LIST))
print(f"Checking {len(SOURCE_LIST)} files")

for s, d in tqdm(zip(SOURCE_LIST, DEST_LIST)):
    with open(s, 'rb') as src, open(d, 'rb') as dst:
        src_md5 = hashlib.md5(src.read()).hexdigest()
        dst_md5 = hashlib.md5(dst.read()).hexdigest()
        if src_md5 == dst_md5:
            pass
        else:
            print(f"Error in {s} / {d}")
            break

print("FILE CHECKS DONE")
