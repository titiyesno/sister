import SOAPpy
import pickle
import os.path

def hello():
	path = '/home/tities/var/log/cups/'
	num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
	nama_file = ""
	iter = 0
	isi = []
	while (iter < num_files) :
		
		if iter == 0 :
			nama_file = path + "error_log"
		else :
			nama_file = path + "error_log." + str(iter)
		
		with open(nama_file,'r') as f:
			for line in f:
				message = line.strip('\n')
				isi.append(message)
			
		f.close()
		#print len(isi)
		iter=iter+1
	return pickle.dumps(isi)
server = SOAPpy.SOAPServer(("localhost", 5000))
server.registerFunction(hello)
server.serve_forever()
