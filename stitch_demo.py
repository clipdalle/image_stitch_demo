import cv2
import numpy as np
from stitching import Stitcher
import os
from pathlib import Path

def stitch_images(image_paths):
    # 读取所有图片
    images = []
    for path in image_paths:
        # 将Path对象转换为字符串
        path_str = str(path)
        img = cv2.imread(path_str)
        if img is not None:
            images.append(img)
    
    # 创建拼接器
    stitcher = Stitcher()
    
    # 执行拼接
    result = stitcher.stitch(images)
    
    return result
 
def list_dir_paths(dir_path, suffix='*.jpg'):
    return list(Path(dir_path).rglob(suffix))

if __name__ == "__main__":
    # 获取所有图片路径
    image_mountains = list_dir_paths('samples/mountain', suffix='*.jpg')

    # 拼接mountain图片
    mountain_result = stitch_images(image_mountains)
    cv2.imwrite('mountain_result.jpg', mountain_result)
    print("Mountain images stitched successfully!")
