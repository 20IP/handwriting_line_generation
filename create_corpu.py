import os
import numpy as np
import cv2
import pandas as pd
import random

with open('/home/datateam/projects/GEN_Handwritten/data/Cyrillic/hwt_style.txt', 'r') as rt:
    ct = rt.read()
rt.close()

ct = ct.split('\n')
ct = ct[:-1]

total_text = []
for i in ct:
    _, text, _ = i.split('\t')
    total_text.append(text)

df = pd.read_excel('/home/datateam/projects/GEN_Handwritten/data/Cyrillic/lookup.xlsx')
total_text += df['Data_value'].tolist()

new_shuf = []
len_list = len(total_text)
num_len = list(range(0, len_list-1))
for _ in range(2):
    random.shuffle(total_text)
    begin_id = 0
    while True:
        rdNum = random.choice([1,2,3,4,5,6])
        if begin_id > len(num_len):
            break
        new_shuf += [total_text[begin_id:begin_id+rdNum]]
        begin_id += rdNum
        
new_shuf = [' '.join(i) for i in new_shuf]

print(new_shuf[:5])

with open('/home/datateam/projects/GEN_Handwritten/data/Cyrillic/Cyrillic_copus.txt', 'w') as wt:
    for i in new_shuf:
        wt.write(i + '\n')
wt.close()