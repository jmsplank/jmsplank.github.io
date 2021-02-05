from PIL import Image, ImageOps
import os
import numpy as np
from tqdm import tqdm

imgs = [d for d in os.listdir("./fastframe") if ".png" in d]

for i in tqdm(imgs):
    img = Image.open(f"fastframe/{i}").convert("L").split()[0]
    img = Image.eval(img, lambda x: 255 if x > 128 else 0)
    blank = Image.fromarray(np.zeros(img.size, dtype=np.int8), "L").split()[0]
    img2 = Image.merge("LA", [blank, img])
    # img2.putalpha(img)
    img2.save(f"fastframe/A_{i}")
