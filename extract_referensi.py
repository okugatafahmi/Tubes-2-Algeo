import os
from extractor import batch_extractor

def extract_referensi():
    path = 'data/referensi/'
    f = open('data.txt','w')
    for folder in sorted(os.listdir(path)):
        img_folder = os.path.join(path,folder)
        print(img_folder)
        res = batch_extractor(img_folder)
        print(len(res))
        
        for k,v in res.items():
            f.write(k)
            f.write('\n')
            for val in v:
                f.write(str(val)+' ')
            f.write('\n')
    f.close()