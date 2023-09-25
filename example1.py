#!/usr/bin/env python3
# by rvpmin
# GNU/GPL License

import numpy as np

data_list = np.arange(1,11,1)

for x in data_list:
    print("value:", x)

x = "hola"
z = 0

try:
    z = int(x) + 1
    print("ok")
except:
    print("Error in sum of z")

#x= np.cos(x)
print(z)
