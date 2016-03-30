import rpyc
#import cPickle as pickle

logevent = {}

class MyService(rpyc.Service):
	global logevent
	def exposed_line_counter(self, fileobj) :
		for line in fileobj:	
			split1 = line.split()
			event = split1[3]+" "+split1[4]
			if event not in logevent:
				logevent[event] = 1
			else:
				logevent[event] +=1	 
		return logevent	

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port=18861)
t.start()
