import pandas as pd
import numpy as np
import os
import sys

my_path = os.chdir('/Users/colinobrien/Desktop/Repo/DS_5100/ds5100_prog_for_ds_jv')
COVID_data = pd.read_excel('MortalityDataWHR2021C2.xlsx')
print(COVID_data)
