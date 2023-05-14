# read -> para arquivos simples (ex: senhas, tokens, informações únicas)
email = None
with open("teste-001.c", "r") as arquivo:
	email = arquivo.read()
print(email)

buffer = email.split('\n')

str_p = ""
for b in buffer:
	str_p = str_p + b
	
print(str_p)
