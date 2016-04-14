import SOAPpy
import pickle

logevent = {}
isi = []
final = []

with open('ip.txt','r') as bukafile:
	ipini = str(bukafile.read()).split('\n')
	#print ipini
	panjang = len(ipini)
	#print panjang
bukafile.close()

iter = 0
while(iter < panjang-1):
	server = SOAPpy.SOAPProxy("http://"+str(ipini[iter])+":8080/")
#server = SOAPpy.SOAPProxy("http://localhost:8080/")
	#server.config.debug = 1
	start = server.hello()

	isi = pickle.loads(start)
	for i in isi:
		final.append(i)
	#cek = "http://localhost:"+str(ipini[iter])+"/"
	#print cek
	#print isi
	iter += 1

#print final
#print len(isi)
for t in final:
	#print t
	split = t.split()
	event = split[3] + " " + split[4]
	if event not in logevent:
		logevent[event] = 1
	else:
		logevent[event] += 1

for event in logevent:
	print event, logevent[event]