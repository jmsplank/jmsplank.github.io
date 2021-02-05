import pyspedas
import numpy as np
import matplotlib.pyplot as plt
from pytplot import data_quants

trange = ["2015-10-07/11:40:00", "2015-10-07/11:50:00"]
probe = "1"
data_rate = "brst"
mms_fgm = pyspedas.mms.fgm(
    trange=trange, probe=probe, data_rate=data_rate, time_clip=True
)

B = data_quants["mms1_fgm_b_gse_brst_l2"].values[:, 3]
plt.plot(B)
plt.show()
