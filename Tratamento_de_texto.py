produtos = ["ABC123", "abc012", " ABS111", "AbB222"]

def modify_text(texto):
	texto = "abc012"
	texto = texto.upper()   #Letra maiúscula
	texto = texto.strip()	#Tira os espaços antes e depois do texto
	return texto

for i, produto in enumerate(produtos):
	produtos[i] = modify_text(produto)
print(produtos)
