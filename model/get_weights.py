import numpy as np
import utils

palette = utils.parse_convert_xml("one_hot_conversion/convert_3+occl_carla.xml")
dist = utils.get_class_distribution("../data/zedcam_F/train/bev+occlusion", (512, 256), palette)
weights = np.log(np.reciprocal(list(dist.values())))
print(weights)
