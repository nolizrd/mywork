import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

file_path = "C:/new/figure1.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
max_size=int(lines[0])
image_data = lines[2:]
max_length = 0 
for row in image_data:
    ones_count = row.count('1')
    if ones_count > max_length:
        max_length = ones_count
        
if max_length>0:
    resolutions = max_size / max_length
else: resolutions = 0

print(f"Номинальное разрешение (мм/пиксель):{resolutions}")
