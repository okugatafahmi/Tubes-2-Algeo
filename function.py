def dot(V1,V2):
	hasil = 0
	for i in range (0,len(V1)):
		hasil += V1[i]*V2[i]
	return hasil
	
def cos_similarity(V1,V2):
	return ((dot(V1,V2))/(panjang(V1)*panjang(V2)))

def panjang(V):
    hasil=0
    for val in V:
        hasil += val*val
    return hasil**0.5

def minus(V1,V2):
# Mengurangi V1 dengan V2. Prekondisi: dimensi(V1)=dimensi(V2)
    return V1-V2

def jarak(V1,V2):
    hasil = panjang(minus(V1,V2))
    return hasil