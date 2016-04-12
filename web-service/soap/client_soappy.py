import SOAPpy
import pickle

server = SOAPpy.SOAPProxy("http://localhost:5000/")
start = server.hello()
logevent = {}
isi = []
isi = pickle.loads(start)
#print len(isi)
for i in isi:
        #print i
    split = i.split()
    event = split[3] + " " + split[4]
    #print event
    if event not in logevent:
        logevent[event] = 1
    else:
        logevent[event] += 1

for event in logevent:
	print event, logevent[event]