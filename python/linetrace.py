"""Script to generate turbulence-like field trace lines.

SRC:
https://lodev.org/cgtutor/randomnoise.html
https://engineeredjoy.com/blog/perlin-noise/
"""
import matplotlib.pyplot as plt
from noise import pnoise3
import numpy as np
from PIL import Image
from tqdm import tqdm


def arr_to_rgb(arr):
    f = np.empty((*arr.shape, 3), np.int8)
    for i in range(3):
        f[:, :, i] = arr
    return f


def arr_to_rgba(arr):
    f = np.zeros((*arr.shape, 4), dtype=np.int8)
    f[:, :, 3] = 255 - arr
    return f


def turbulent_lines(
    shape=(200, 200),
    scale=100,
    octaves=6,
    persistence=0.5,
    lacunarity=2.0,
    seed=None,
    frames=10,
    xperiod=5.0,
    yperiod=10.0,
    power=5.0,
):
    if not seed:
        seed = np.random.randint(0, 100)
        print("seed was {}.".format(seed))

    for frame in tqdm(range(frames)):
        arr = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                xyvalue = i * xperiod / shape[0] + j * yperiod / shape[1]
                noise = power * pnoise3(
                    i / scale,
                    j / scale,
                    frame / (scale * 3),
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base=seed,
                )
                xyvalue += noise
                sinvalue = 255 if abs(np.sin(xyvalue * np.pi)) <= 0.95 else 0
                arr[i][j] = sinvalue

        # max_arr = np.max(arr)
        # min_arr = np.min(arr)
        # norm_me = lambda x: (x - min_arr) / (max_arr - min_arr)
        # norm_me = np.vectorize(norm_me)
        # arr = norm_me(arr)
        # img = Image.fromarray(arr_to_rgb(arr), "RGB")
        # img.save(f"test_frame_{frame:03d}.png")

        img = Image.fromarray(arr_to_rgba(arr), "RGBA")
        img.save(f"frames/A_frame_{frame:03d}.png")
    return True


frames = 500
glob_scl = 1.0 / 8
data = turbulent_lines(
    shape=(1000, 1000),
    power=1.0,
    xperiod=glob_scl * 25,
    yperiod=glob_scl * 50,
    frames=frames,
)