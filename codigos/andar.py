import zmq
import sys
import time
#from cliente import Cliente
from servidor import Servidor

PREDIOS = 10

port = "6000"
topico = ""
if len(sys.argv) > 2:
	#port =  sys.argv[1]
	predio = sys.argv[1]
	topico = sys.argv[2]
	#int(port)
	int(predio)
	int(topico)

port = str(int(port) + PREDIOS*int(predio))

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, str("A" + str(topico)))

servidor = Servidor()

while True:
	tmp = socket.recv()

	if "-" in tmp:
		mensagem = tmp.split("-")[1]

	conf = servidor.decode(mensagem)
	print(conf + " - " + mensagem)

#	time.sleep(1)

