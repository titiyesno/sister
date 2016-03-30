import rpyc
import threading
import os.path
import time

path = '/home/administrator/sister/distributed-systems/RMI/var/log/cups/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
hasil = {}

with open('ip.txt','r') as bukafile:
	ipini = str(bukafile.read()).split('\n')
	print ipini
	panjang = len(ipini)

class MyThread(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i
		self.process = None

	def run(self):
		self.process = 1
		proxy = rpyc.connect(ipini[self.i], 18861, config={'allow_public_attrs': True})
		nama_file = ""
		linecount = ""
		iter = self.i
		while (iter < num_files) :
			if iter == 0 :
				nama_file = path + "error_log"
			else :
				nama_file = path + "error_log." + str(iter)
			fileobj = open(nama_file)
			linecount = proxy.root.line_counter(fileobj)
			#print nama_file
			iter=iter+3
		print linecount, ipini[self.i]
		print hasil
		for key in linecount :
			print("{} = {}".format(key, linecount[key]))
			#print type(key), type(linecount[key])
			
			#if key not in linecount :
			#	hasil[key] = linecount[key]
			#	print("{} = {}".format(key, linecount[key]))
			#else :
			#	hasil[key] += linecount[key]
				#print("{} = {}".format(key, linecount[key]))
		#print hasil


for i in range(0, panjang):
	t = MyThread(i)
	t.start()
