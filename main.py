def ReadData():
    data = open('data.txt','r')
    acuan = 0
    arr = []
    for l in data:
        line = l.strip()
        if (acuan==0):
            img_name = line
        else:
            temp = line.split(' ')
            vector = []
            for val in temp:
                vector.append(float(val))
            arr.append([img_name,vector])
            break
        acuan = (acuan+1)%2
    data.close()
    return arr

def match(v,data,tipe)
# mencocokkan v dengan list data berdasarkan tipe pencocokan
# v : array of float (vector hasil ekstrak suatu foto uji)
# data : dict('namaFile',array of float) (data referensi)
# tipe : 0 berarti dengan cosine, 1 dengan euclidean
# return nya adalah dict('namaFile',nilai pencocokan)