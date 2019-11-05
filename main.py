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


def match(v,data,tipe):
# mencocokkan v dengan list data berdasarkan tipe pencocokan
# v : array of float (vector hasil ekstrak suatu foto uji)
# data : dict('namaFile',array of float) (data referensi)
# tipe : 0 berarti dengan cosine, 1 dengan euclidean
# return nya adalah dict('namaFile',nilai pencocokan)
    vref = ReadData()
    if (tipe == 0):
        hasil_match = cos_similarity(v,vref)
        if (hasil_match < 20):
            #show(hasil)
    else if (tipe == 1):
        hasil_match = jarak(v,vref)
        if (hasil_match < 5):
            #show(hasil)
