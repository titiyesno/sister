#!/usr/bin/env python
import pika
import sys
import os.path
import pickle

path = '/home/tities/var/log/cups/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
#isi = []
log = {}
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

namafile = ""
iter = 0
while (iter < 1) :
	if iter == 0 :
		nama_file = path + "error_log"
	else :
		nama_file = path + "error_log." + str(iter)
	with open(nama_file,'r') as f:
		for line in f:
			message = line.strip('\n')
			channel.basic_publish(exchange='',
						          routing_key='task_queue',
						          body=message,
						          properties=pika.BasicProperties(
						          delivery_mode = 2, # make message persistent
						         ))
	f.close()
	print " [x] Sent %r" % (nama_file,)
	iter=iter+1

def callback(ch, method, properties, body):
	#print pickle.loads(body)

	temp = {}
	temp = pickle.loads(body)
	#print type(temp)
	panjang = len(temp)
	#print panjang
	length.append(panjang)
	print length
	'''for key in temp:
		if key not in log:
			log[key] = temp[key]
		else:
			log[key] += temp[key]'''
	#print temp
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='baliklagi')

channel.start_consuming()
connection.close()
