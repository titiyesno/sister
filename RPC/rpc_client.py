import xmlrpclib
import logging
import threading
import os.path

banyak_file = len(os.listdir("cups"))

with open('ip.txt','r') as bukafile:
	ipini = str(bukafile.read()).split('\n')
	print ipini
	panjang = len(ipini)

class MyThread(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i

	def run(self):
		logging.debug(str(self.i) + ' running')
		proxy = xmlrpclib.ServerProxy("http://ipini[self.i]:8000/")
		nama_file = ""
		linecount = ""
		iter = self.i
		while (iter < banyak_file) :
			if iter == 0 :
				nama_file = "cups/error_log"
			else :
				nama_file = "cups/error_log." + str(iter)
			fileobj = open(nama_file)
			linecount = proxy.is_even(fileobj)
			iter=iter+3
		print linecount
		for key, value in linecount.iteritems() :
			print key, value

for i in range(0, panjang):
	t = MyThread(i)
	t.start()

#proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
#print "3 is even: %s" % str(proxy.is_even(3))
#print "4 is even: %s" % str(proxy.is_even(4))
