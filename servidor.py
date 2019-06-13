class Servidor:
	registro = []
	politicas = {}
	politicas["max"] = 60 
	politicas["complexo"] = 0

	def show(self):
		for x in self.registro:
			print(x)

	def add(self, id, p, a):
		for x in self.registro:
			if x[0] == id:
				return EnvironmentError
				break
			self.registro.append([id, p, a])

	def remove(self, id):
		for x in self.registro:
			if(x[0] == id):
				self.registro.remove(x)
			else:
				return EnvironmentError


	def decode(self, s):
		if ":" in s:
			t = s.split(":")[0]
			id = s.split(":")[1]
			p = s.split(":")[2]
			a =s.split(":")[3]

		if t == "E" or t == "S" or t == "PW" or t == "C":
			id = int(id)
			p = int(p[1])
			a = int(a[1])
			return self.op(t, id, p, a)

		else:
			return "Error! Tipo nao reconhecido!"

	def op(self, t, id, p, a):
		auxiliar = "P" + str(p) + "A" + str(a)
		if t == "E":                                                 
			if auxiliar not in self.politicas:
				self.politicas[auxiliar] = 1

			if self.politicas[auxiliar] > self.politicas["max"]:
				if (id >= 100 and id < 200 ):
					self.add(id, p, a)
					return "OK"
				else:
					return "Acesso Negado, limite de lotacao atingido"
			else:
				self.add(id, p, a)
				return "OK"

		elif t == "S":
			self.remove(id)
			self.politicas[auxiliar] = self.politicas[auxiliar] - 1
			return "OK"

		elif t == "PW":
			self.politicas[auxiliar] = id
			return "Modificado com Sucesso!"

		elif t == "C":
			self.politicas["complexo"] = p * a * self.politicas["max"] 

