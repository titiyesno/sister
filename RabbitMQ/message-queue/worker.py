#!/usr/bin/env python
import pika
import time
import sys
#import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

logevent = {}

def callback(ch, method, properties, body):
    #print "%r" % (body,)
    global logevent
    split1 = body.split()
    #print split1
    event = split1[3]+" "+split1[4]
    #print event
    #panjang = len(logevent)
    #print panjang
    if event not in logevent:
    	#print "belum"
    	logevent[event] = 1
    else:
    	#print "sudah"
    	logevent[event] += 1
    #print event, "=======>",logevent[event]
    print logevent
    print "\n ======================================= \n"
    #time.sleep( body.count('.') )
    #print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)
