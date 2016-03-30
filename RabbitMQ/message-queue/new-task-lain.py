#!/usr/bin/env python
import pika
import sys
import pickle
import time

log = {}
counter = 0
start = time.time()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_q', durable=True)

for i in range(0,2):
	message = "Start"
	channel.basic_publish(exchange='',
	                      routing_key='task_q',
	                      body=message,
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2, # make message persistent
	                      ))
	print(" [x] Sent %r" % message)

channel.queue_declare(queue='balik', durable=True)

def callback(ch, method, properties, body):
	global counter
	global start
	temp = {}
	temp = pickle.loads(body)
	counter += 1
	for key in temp:
		if key not in log:
			log[key] = temp[key]
		else:
			log[key] += temp[key]
	if counter == 2:
		for key in log:
			print key, log[key]
	#print pickle.loads(body)
		end = time.time()
		elapsed = end - start
		print elapsed
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='balik')

channel.start_consuming()


connection.close()