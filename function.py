import main.py

def dot(V1,V2):
	hasil = 0
	for i in range (0,len(V1)):
		hasil += V1[i]*V2[i]
	return hasil
	
def similarity(V1,V2):
	return ((dot(V1,V2))/(panjang(V1)*panjang(V2)))
