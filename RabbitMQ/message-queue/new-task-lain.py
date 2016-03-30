#!/usr/bin/env python
import pika
import sys
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_q', durable=True)

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
	print pickle.loads(body)
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='balik')

channel.start_consuming()


connection.close()