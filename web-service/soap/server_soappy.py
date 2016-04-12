import SOAPpy
def hello():
    return "Hello World"
server = SOAPpy.SOAPServer(("localhost", 5000))
server.registerFunction(hello)
server.serve_forever()