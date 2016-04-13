import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
server.config.debug = 1
print server.hello()
