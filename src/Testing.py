#w é escrita, r é ler
arquivo = open("texto.txt", "w") #Cria ou abre o arquivo
arquivo.write("Ola mundo") #write coloca o texto do parentesis no arquivo
arquivo.close()#fecha o arquivo

arquivo = open("texto.txt", "r") #Abre o arquivo para ler
conteudo = arquivo.read() #Pega tudo o conteudo do arquivo e guarda na VAR conteudo
print(conteudo)
arquivo.close() #fecha o arquivo


arquivo = open("meu_texto.txt", "w")
arquivo.write("Estou aprendendo python")
arquivo.close()

arquivo = open("meu_texto.txt", "r")
lendo = arquivo.read()
print(lendo)
arquivo.close()


nome = input("Me da seu nome: ")
arquivo = open("nome.txt", "w")
arquivo.write(nome)
arquivo.close()

arquivo = open("nome.txt", "r")
mostra = arquivo.read()
print(mostra)
arquivo.close()
