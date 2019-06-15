import zmq
import sys
import time
from cliente import Cliente

#Conexao pub-sub
port = "6000"
if len(sys.argv) > 1:
	port =  sys.argv[1]
	int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

cliente = Cliente()

while True:
	message, p, a = cliente.rand()
	print(message, p, a)
	socket.send("%s-%s" % (p, message))
	time.sleep(1)

