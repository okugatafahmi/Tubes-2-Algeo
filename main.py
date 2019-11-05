import numpy as np
from function import cos_similarity,jarak

def ReadData():
    data = open('data.txt','r')
    acuan = 0
    dict_img = dict()
    for l in data:
        line = l.strip()
        if (acuan==0):
            img_name = line
        else:
            temp = line.split(' ')
            vector = []
            for val in temp:
                vector.append(float(val))
            vector = np.array(vector)
            dict_img[img_name]=vector
        acuan = (acuan+1)%2
    data.close()
    return dict_img

def match(vector_extract,data,tipe):
# mencocokkan v dengan list data berdasarkan tipe pencocokan
# v : array of float (vector hasil ekstrak suatu foto uji)
# data : dict('namaFile',array of float) (data referensi)
# tipe : 0 berarti dengan cosine, 1 dengan euclidean
# return nya adalah dict('namaFile',nilai pencocokan)
    res = []
    i = 0
    for k,v in data.items():
        if (tipe == 0):
            hasil_match = cos_similarity(vector_extract,v)
        elif (tipe == 1):
            hasil_match = jarak(vector_extract,v)
        res.append((k,hasil_match))
    return res
