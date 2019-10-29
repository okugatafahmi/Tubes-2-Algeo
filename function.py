def dot(V1,V2):
	hasil = 0
	for i in range (0,len(V1)):
		hasil += V1[i]*V2[i]
	return hasil
	
def cos_similarity(V1,V2):
	return ((dot(V1,V2))/(panjang(V1)*panjang(V2)))

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