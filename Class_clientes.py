class Cliente():
	def __init__(self, nome, email, plano):
		self.nome = nome
		self.email = email
		self.planos_validos = ['basico','premium']
		if plano in self.planos_validos:	
			self.plano = plano
		else:
			raise Exception('Plano inválido')

	def mudar_plano(self, novo_plano):
		if novo_plano in self.planos_validos:
			self.plano = novo_plano
		else:
			print('Plano inválido!')

	def ver_filme(self, filme, filme_plano):
		if self.plano == filme_plano:
			print(f'Ver filme {filme}.')
		elif self.plano == 'premium':
			print(f'Ver filme {filme}')
		elif filme_plano not in self.planos_validos:
			print('Insira um plano válido para visualização do filme!')
		elif self.plano == 'basico' and filme_plano == 'premium':
			print(f'Faça a atualização do seu plano para asisstir a {filme}!')

	

cliente1 = Cliente('Eduardo','eduardomagno01@gmail.com','basico')
print(cliente1.plano)
cliente1.mudar_plano('premium')
print(cliente1.plano)
cliente1.mudar_plano('basico')
print(cliente1.plano)
cliente1.ver_filme('O senhor dos anéis','premium')
