import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

# Feature extractor
def extract_features(image_path, vector_size = 32):
    image = imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc


def batch_extractor(images_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    return result

def panjang(V):
    res=0
    for val in V:
        res += val*val
    return res

def minus(V1,V2):
# Mengurangi V1 dengan V2. Prekondisi: panjang(V1)=panjang(V2)
    V3=V1
    for i in range(0,len(V1)):
        V3[i] -= V2[i]
    return V3


res = batch_extractor('data/referensi/AaronPaul')
arr = {}
for nm_file,array in res.items():
    
    print(nm)
#
#     print(v)
#     print(type(v))
#     arr=v
#     break
# print
# print(len(arr))
# new_arr = (arr,arr)
# for val in new_arr:
#     print(val)
