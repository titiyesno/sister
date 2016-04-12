import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:5000/")
print server.hello()