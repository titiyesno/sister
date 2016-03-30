#!/usr/bin/env python
import pika
import time
import os.path
import sys
import pickle

logevent = {}

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_q', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    if body == 'Start':
        global logevent
        path = '/home/tities/var/log/cups/'
        num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
        nama_file = ""
        iter = 0
        while (iter < num_files) :
            if iter == 0 :
                nama_file = path + "error_log"
                #print nama_file
            else :
                nama_file = path + "error_log." + str(iter)
                #print nama_file
            with open(nama_file,'r') as f:
                for line in f:
                    message = line.strip('\n')
                    split = message.split()
                    event = split[3]+" "+split[4]
                    #print event
                    if event not in logevent:
                        logevent[event] = 1
                    else:
                        logevent[event] += 1
                f.close()
            #print nama_file
            iter = iter+1
        print logevent
        channel.queue_declare(queue='balik', durable=True)
        channel.basic_publish(exchange='',
                              routing_key='balik',
                              body=pickle.dumps(logevent),
                              properties=pika.BasicProperties(
                              delivery_mode = 2, # make message persistent
                              ))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_q')

#connection.close()

try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)