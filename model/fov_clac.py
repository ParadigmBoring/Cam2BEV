# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:25:59 2022

@author: 17096
"""

import numpy as np
# Prepare
w, h = 968*2, 484*2
fx, fy = 3872,3872

# Go
fov_x = np.rad2deg(2 * np.arctan2(w, 2 * fx))
fov_y = np.rad2deg(2 * np.arctan2(h, 2 * fy))

print("Field of View (degrees):")
print(f"  {fov_x = :.1f}\N{DEGREE SIGN}")
print(f"  {fov_y = :.1f}\N{DEGREE SIGN}")