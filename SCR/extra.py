import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"Data_excel\frames.csv")
print(data.head)

print(data.Image_ID)

img = plt.imread(""+ data.Image_ID)
print(img)
