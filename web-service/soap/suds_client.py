#!/usr/bin/env python

from suds.client import Client

#proxy = {'http':'tities13%40mhs.if.its.ac.id:087752814545@proxy.its.ac.id:8080'}

client = Client('http://localhost:8080/ParsingLog/soap/description')

print client.service.add()
#print 'Pembulatan ke atas  : 5.6      =', client.service.ceiler(5.6)
#print 'Pembulatan ke bawah : 5.6      =', client.service.floorer(5.6)
#print 'Perpangkatan        : 2^3      =', client.service.power(2.0,3.0)
#print 'Perakaran           : 8 akar 3 =', client.service.sqrter(8.0,3.0)
#print 'Faktorial           : 12       =', client.service.factorializer(12)
#print 'Sinus   (derajat)   : sin 30   =', client.service.sinus(30.0)
#print 'Cosinus (derajat)   : cos 30   =', client.service.cosinus(30.0)
#print 'Tangen  (derajat)   : tan 30   =', client.service.tangent(30.0)
