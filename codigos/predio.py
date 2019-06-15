import zmq
import sys
import time
#from cliente import Cliente
from servidor import Servidor

PREDIOS = 10

port = "6000"
topico = ""
if len(sys.argv) > 1:
	#port =  sys.argv[1]
	topico = sys.argv[1]
	#int(port)
	int(topico)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, str("P" + str(topico)))

context_pub = zmq.Context()
socket_pub = context_pub.socket(zmq.PUB)

count = 0
a = 1
while(a):
	try:
		a = socket_pub.bind("tcp://*:%s" % port)
	except:
		if(count > PREDIOS):
			sys.exit("Error! Socket.bind")
		port = str(int(port) + PREDIOS*int(topico))
		count+=1

servidor = Servidor()

while True:
	tmp = socket.recv()
	
	if "-" in tmp:
		mensagem = tmp.split("-")[1]

	conf = servidor.decode(mensagem)
	print(conf + " - " + mensagem)
	
	if ":" in mensagem:
		a = mensagem.split(":")[3]
		
	socket_pub.send("%s-%s" % (a, mensagem))
#	time.sleep(1)

