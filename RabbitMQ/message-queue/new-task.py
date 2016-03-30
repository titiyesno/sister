#!/usr/bin/env python
import pika
import sys
import threading
import os.path
#import pickle

path = '/home/tities/distributed-systems/RabbitMQ/message-queue/var/log/cups/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
#isi = []

class MyThread(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i
		self.process = None

	def run(self):
		#global isi
		self.process = 1
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()

		channel.queue_declare(queue='task_queue', durable=True)

		namafile = ""
		iter = self.i
		while (iter < 2) :
			if iter == 0 :
				nama_file = path + "error_log"
			else :
				nama_file = path + "error_log." + str(iter)

			with open(nama_file,'r') as f:
				for line in f:
					message = line.strip('\n')
					#isi.append(message)
					channel.basic_publish(exchange='',
						                  routing_key='task_queue',
						                  body=message,
						                  properties=pika.BasicProperties(
						                  delivery_mode = 2, # make message persistent
						                 ))
				f.close()
#message = ' '.join(sys.argv[1:]) or "Hello World!"
			print " [x] Sent %r" % (nama_file,)
			iter=iter+1
		connection.close()

for i in range(0, 1):
	t = MyThread(i)
	t.start()