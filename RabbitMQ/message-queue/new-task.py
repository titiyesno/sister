#!/usr/bin/env python
import pika
import sys
import os.path
import pickle
import time

start = time.time()

path = '/home/tities/var/log/cups/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
isi = []
log = {}
counter = 0
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

namafile = ""
iter = 0
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
	#print isi
	channel.basic_publish(exchange='',
						  routing_key='task_queue',
						  body=pickle.dumps(isi),
						  properties=pika.BasicProperties(
						  delivery_mode = 2, # make message persistent
						  ))
	#print " [x] Sent %r" % (nama_file,)
	iter=iter+1

def callback(ch, method, properties, body):
	#print pickle.loads(body)
	global counter
	global start
	temp = {}
	temp = pickle.loads(body)
	counter += 1
	#print counter
	#print temp
	#print type(temp)
	#panjang = len(temp)
	#print panjang
	for key in temp:
		if key not in log:
			log[key] = temp[key]
		else:
			log[key] += temp[key]
	#print temp
	if counter == num_files:
		for key in log:
			print key, log[key]
		end = time.time()
		elapsed = end - start
		print elapsed

	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='baliklagi')

channel.start_consuming()
connection.close()
