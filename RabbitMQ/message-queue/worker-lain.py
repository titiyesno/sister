#!/usr/bin/env python
import pika
import time
import threading
import os.path
import sys

path = '/home/tities/var/log/cups/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.startswith('error_log')])
logevent = {}
        
class MyThread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i
        self.process = None

    def run(self):
        global logevent
        self.process = 1
        nama_file = ""
        iter = self.i
        while (iter < num_files) :
            if iter == 0 :
                nama_file = path + "error_log"
            else :
                nama_file = path + "error_log." + str(iter)
            with open(nama_file,'r') as f:
                for line in f:
                    message = line.strip('\n')
                    split = message.split()
                    event = split[3]+" "+split[4]
    #print event
    #panjang = len(logevent)
    #print panjang
                    if event not in logevent:
        #print "belum"
                        logevent[event] = 1
                    else:
                        #print "sudah"
                        logevent[event] += 1
                f.close()
            iter = iter+1
        print logevent

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_q', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    if body == 'Start':
        for i in range(0, 1):
            t = MyThread(i)
            t.start()
    #print(" [x] Received %r" % body)
    #time.sleep(body.count(b'.'))
    #print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_q')

try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)