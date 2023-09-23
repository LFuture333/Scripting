import pyrealsense2 as rs

import numpy as np

import cv2



#Create a pipeline 
pipeline =  rs.pipeline()


# Config the pipeline to strea 
# Different resolutions of color and depth streams
config = rs.config()


#Get Device product line for setting a supporting resolution

pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))


for s in device.sensors:
    print(s)