from random import randint, choice

class Cliente:
	ids = []
	floor = 0
	build = 0

	def __init__(self):
		self.floor = 2
		self.build = 3

	def rand(self):
		id = randint(100, 399)
		i = randint(0,1)	
		p = "P" + str(randint(1, self.build))
		a = "A" + str(randint(1, self.floor))
		if len(self.ids) == 0:
			i=1
		return self.encode(i, id, p, a)

	def encode(self, i, id, p, a):
		if(i):
		  self.ids.append([id, p, a])
		  mensagem = "E:" + str(id) + ":" + str(p) + ":" + str(a)
		  return mensagem, p, a

		else:
		  id, p, a = choice(self.ids)
		  self.ids.remove([id, p, a])
		  mensagem = "S:" + str(id) + ":" + str(p) + ":" + str(a)
		  return mensagem, p, a
