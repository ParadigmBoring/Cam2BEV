# -*- coding: utf-8 -*-
"""
Created on Fri May 27 02:20:10 2022

@author: 17096
"""

import numpy as np
import utils
palette = utils.parse_convert_xml("one_hot_conversion/convert_3+occl_carla.xml")
dist = utils.get_class_distribution("../data/zedcam_F/track1/train/bev+occlusion", (512, 256), palette)
weights = np.log(np.reciprocal(list(dist.values())))
print(weights)