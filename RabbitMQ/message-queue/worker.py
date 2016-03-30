#!/usr/bin/env python
import pika
import time
import sys
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

logevent = {}
isi = []

def callback(ch, method, properties, body):
    #print "%r" % (body,)
    global logevent
    isi = pickle.loads(body)
    for i in isi:
        #print i
        split = i.split()
        event = split[3] + " " + split[4]
        #print event
        if event not in logevent:
            logevent[event] = 1
        else:
            logevent[event] += 1
    print logevent
    
    channel.queue_declare(queue='baliklagi', durable=True)
    channel.basic_publish(exchange='',
                      routing_key='baliklagi',
                      body=pickle.dumps(logevent),
                      properties=pika.BasicProperties(
                      delivery_mode = 2, # make message persistent
                      ))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')


try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)
